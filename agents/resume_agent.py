# agents/resume_agent.py

SKILL_KEYWORDS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "computer vision",
    "tensorflow",
    "pytorch",
    "flask",
    "django",
    "docker",
    "aws",
    "git"
]

def extract_resume_skills(resume_text: str):
    """
    Extract skills from resume text using keyword matching.
    """
    resume_text = resume_text.lower()
    skills_found = []

    for skill in SKILL_KEYWORDS:
        if skill in resume_text:
            skills_found.append(skill)

    return list(set(skills_found))


def resume_agent(resume_text: str):
    """
    Resume Parsing Agent
    """
    skills = extract_resume_skills(resume_text)

    return {
        "skills": skills,
        "skill_count": len(skills)
    }
