import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    client = TestClient(app=app, headers={"Authorization": "Bearer 31a64525"})
    yield client


@pytest.fixture
def job_description():
    """Sample text for job offer"""
    return """
    **Position Title:** Mobile App Developer

    **Location:** Remote

    **Company:** XYZ Tech Solutions

    **About Us:**
    XYZ Tech Solutions is a rapidly growing tech company specializing in innovative mobile applications. We are dedicated to creating user-friendly and cutting-edge solutions that meet the needs of our clients. Our team is comprised of passionate individuals who thrive in a dynamic and collaborative environment.

    **Job Description:**
    As a Mobile App Developer at XYZ Tech Solutions, you will be responsible for the design, development, and maintenance of high-quality mobile applications. You will collaborate closely with our team of designers and developers to create engaging user experiences and implement new features. The ideal candidate is proficient in mobile app development frameworks, has a strong understanding of user interface design principles, and is able to work independently with minimal supervision.

    **Key Responsibilities:**
    - Develop and maintain mobile applications for iOS and Android platforms
    - Collaborate with designers to implement user interface designs
    - Write clean, maintainable code following best practices
    - Conduct code reviews and provide constructive feedback to team members
    - Stay up-to-date with the latest trends and technologies in mobile app development

    **Requirements:**
    - Bachelor's degree in Computer Science or a related field
    - 3+ years of experience in mobile app development
    - Proficiency in Swift, Kotlin, or other relevant programming languages
    - Strong understanding of mobile UI design principles and best practices
    - Experience with RESTful APIs and third-party libraries
    - Excellent problem-solving and communication skills
    - Ability to work independently and as part of a team
    - Familiarity with version control systems such as Git
    """


@pytest.fixture
def resume_text():
    """Sample text for a resume"""
    return """
    John Doe

    123 Main Street, Anytown, USA | (555) 123-4567 | john.doe@email.com

    Objective:
    Highly skilled Mobile App Developer with over 5 years of experience in designing and developing user-friendly mobile applications for iOS and Android platforms. Passionate about creating innovative solutions that enhance the user experience and drive business growth.

    Professional Experience:

    Senior Mobile App Developer
    ABC Tech Solutions, Anytown, USA
    July 2019 - Present

    - Developed and maintained multiple mobile applications for iOS and Android platforms, resulting in a 20% increase in user engagement.
    - Collaborated with cross-functional teams to design and implement new features, resulting in a 30% reduction in app crashes.
    - Conducted code reviews and provided mentorship to junior developers, resulting in improved code quality and team performance.
    - Implemented third-party APIs to integrate additional functionality into mobile applications, such as payment processing and location services.

    Mobile App Developer
    XYZ Software, Anytown, USA
    March 2016 - June 2019

    - Designed and developed mobile applications for clients in various industries, including healthcare and finance.
    - Optimized app performance and implemented new features based on user feedback, resulting in a 25% increase in app downloads.
    - Worked closely with designers to create intuitive user interfaces and seamless user experiences.
    - Collaborated with QA team to identify and fix bugs, ensuring a smooth app experience for end users.

    Education:

    Bachelor of Science in Computer Science
    Anytown University, Anytown, USA
    Graduated: May 2016

    Skills:

    - Proficient in Swift, Kotlin, and Java
    - Strong understanding of mobile UI design principles
    - Experience with RESTful APIs and third-party libraries
    - Excellent problem-solving and communication skills
    - Familiarity with version control systems such as Git

    Certifications:

    - Certified Mobile App Developer (CMAD)
    - Agile Certified Practitioner (ACP)
    """
