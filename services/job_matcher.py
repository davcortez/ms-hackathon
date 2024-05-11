"""
Matcher Module
"""

import re
import json
import google.generativeai as genai
from fastapi import HTTPException
import aiohttp
from internal.prompt_template import input_prompt
from internal.config import get_settings
from google.api_core import exceptions as api_errors
from schemas.job_match import JobMatchRequest, JobMatchResponse


settings = get_settings()

genai.configure(api_key=settings.gemini_api_key)

model_config = {"temperature": 0.3, "top_p": 1, "top_k": 32, "max_output_tokens": 4096}

GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={settings.gemini_api_key}"


async def generate_content_async(*, payload: JobMatchRequest):
    """Asynchronous service to call Gemini API"""
    async with aiohttp.ClientSession() as session:
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"{input_prompt}\n Job Description\n {payload.job_description} Resume \n {payload.resume_text}"
                        }
                    ]
                }
            ],
            "generationConfig": {
                "response_mime_type": "application/json",
                "temperature": 0.3,
                "maxOutputTokens": 4096,
                "topP": 1,
                "topK": 32,
            },
        }

        async with session.post(GEMINI_URL, json=payload) as response:
            response.raise_for_status()
            return await response.json()


def get_match(*, payload: JobMatchRequest):
    """Get the results of the match analysis between the
    job description and the resume text of the candidate

    Paramters
    -----------
    resume_text
        the text extracted from the candidate's resume
    job description
        the job description to be compared with the candidate's resume

    """
    model = genai.GenerativeModel("gemini-pro", generation_config=model_config)

    optimized_prompt = [
        input_prompt,
        "Job Description\n" + payload.job_description,
        "Resume \n" + payload.resume_text,
    ]

    try:
        response = model.generate_content(optimized_prompt)
    except (api_errors.InternalServerError, api_errors.ResourceExhausted) as error:
        raise HTTPException(status_code=400, detail=error.response["Error"])

    return JobMatchResponse(**_extract_json(response.text))


def _extract_json(text_response):
    """Extract the json from the generated text"""
    pattern = r"\{[^{}]*\}"

    matches = re.finditer(pattern, text_response)
    json_objects = []

    for match in matches:
        json_str = match.group(0)
        try:
            json_obj = json.loads(json_str)
            return json_obj
        except json.JSONDecodeError:
            extended_json_str = _extend_search(text_response, match.span())
            try:
                json_obj = json.loads(extended_json_str)
                return json_obj
            except json.JSONDecodeError:
                continue

    if json_objects:
        return json_objects
    else:
        return None


def _extend_search(text, span):
    """Extend search in the the generated text"""
    start, end = span
    nest_count = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            nest_count += 1
        elif text[i] == "}":
            nest_count -= 1
            if nest_count == 0:
                return text[start : i + 1]
    return text[start:end]
