def fit_decision_agent(resume_skills, required_skills):
    resume_set = set(resume_skills)
    required_set = set(required_skills)

    matched_skills = list(resume_set & required_set)
    missing_skills = list(required_set - resume_set)

    match_ratio = len(matched_skills) / max(len(required_set), 1)

    if match_ratio >= 0.7:
        fit_status = "Good Fit"
    elif match_ratio >= 0.4:
        fit_status = "Partial Fit"
    else:
        fit_status = "Not a Fit"

    return {
        "fit_status": fit_status,
        "match_ratio": round(match_ratio, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
