from services.job_matcher import get_match
from schemas.job_match import JobMatchRequest


def test_get_match_results(job_description, resume_text):
    """
    Test that the match between the job offer and the candidate occurs.
    """
    payload = JobMatchRequest(job_description=job_description, resume_text=resume_text)

    response = get_match(payload=payload)

    assert {
        "job_description_match",
        "matching_keywords",
        "profile_summary",
    } <= response.model_dump().keys()
