from pydantic import BaseModel


class JobMatchRequest(BaseModel):
    job_description: str
    resume_text: str


class JobMatchResponse(BaseModel):
    job_description_match: str
    matching_keywords: list
    profile_summary: str
