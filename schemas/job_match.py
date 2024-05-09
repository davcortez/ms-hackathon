from pydantic import BaseModel, Field


class JobMatchRequest(BaseModel):
    job_description: str = Field(
        min_length=200,
        example="Seeking skilled software engineer proficient in Python & cloud technologies to develop scalable applications for our dynamic team. Apply now!",
    )
    resume_text: str = Field(
        min_length=200,
        example="Experienced Python developer adept in cloud computing, skilled in problem-solving and team collaboration, seeking challenging opportunities.",
    )


class JobMatchResponse(BaseModel):
    job_description_match: str
    matching_keywords: list
    profile_summary: str
