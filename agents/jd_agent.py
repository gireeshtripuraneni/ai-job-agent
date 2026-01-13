SKILL_KEYWORDS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "computer vision", "tensorflow", "pytorch",
    "flask", "django", "docker", "aws", "git"
]

def extract_jd_skills(jd_text: str):
    jd_text = jd_text.lower()
    skills_found = []

    for skill in SKILL_KEYWORDS:
        if skill in jd_text:
            skills_found.append(skill)

    return list(set(skills_found))


def jd_agent(jd_text: str):
    skills = extract_jd_skills(jd_text)

    return {
        "required_skills": skills,
        "required_skill_count": len(skills)
    }
