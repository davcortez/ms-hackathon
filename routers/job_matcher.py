from fastapi import APIRouter, status
from schemas.job_match import JobMatchRequest, JobMatchResponse
from services.job_matcher import get_match


router = APIRouter(prefix="/v1", tags=["main"])


@router.post(
    "/job-matcher", status_code=status.HTTP_200_OK, response_model=JobMatchResponse
)
def get_match_response(payload: JobMatchRequest):
    """
    return the results of the matching between
    the job description and the candidate's resume
    """
    match_response = get_match(payload=payload)

    return match_response
