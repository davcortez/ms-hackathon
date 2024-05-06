from fastapi import status


def test_get_match(client, job_description, resume_text):
    """
    Test that the match between the job offer and the candidate occurs.
    """
    response = client.post(
        "/v1/job-matcher",
        json={"job_description": job_description, "resume_text": resume_text},
    )

    assert response.status_code == status.HTTP_200_OK
    assert {
        "job_description_match",
        "missing_keywords",
        "profile_summary",
    } <= response.json().keys()
