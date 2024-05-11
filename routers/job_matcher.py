import json
from fastapi import APIRouter, status, Security
from schemas.job_match import JobMatchRequest, JobMatchResponse
from services.job_matcher import generate_content_async
from internal.auth import get_token

router = APIRouter(prefix="/v1", dependencies=[Security(get_token)], tags=["main"])


@router.post(
    "/job-matcher", status_code=status.HTTP_200_OK, response_model=JobMatchResponse
)
async def get_match_response(payload: JobMatchRequest):
    """
    return the results of the matching between
    the job description and the candidate's resume
    """
    match_response = await generate_content_async(payload=payload)
    response = _extract_data_v2(data=match_response)

    return response


def _extract_data_v2(*, data):
    """Extract data form REST API Gemini"""
    candidates_data = {}
    for candidate in data["candidates"]:
        content = candidate["content"]["parts"][0]["text"]
        content_dict = json.loads(content)
        candidates_data["job_description_match"] = content_dict.get(
            "job_description_match"
        )
        candidates_data["matching_keywords"] = content_dict.get("matching_keywords")
        candidates_data["profile_summary"] = content_dict.get("profile_summary")

    return candidates_data
