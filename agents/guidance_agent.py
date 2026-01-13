def guidance_agent(missing_skills, fit_status):
    learning_plan = {}
    resume_tips = []

    for skill in missing_skills:
        learning_plan[skill] = {
            "level": "Beginner → Intermediate",
            "steps": [
                f"Learn fundamentals of {skill}",
                f"Build a mini project using {skill}",
                f"Add {skill} project to resume"
            ]
        }

    if fit_status != "Good Fit":
        resume_tips.append(
            "Highlight quantified project outcomes (metrics, impact)"
        )
        resume_tips.append(
            "Align resume keywords with job description"
        )

    return {
        "learning_roadmap": learning_plan,
        "resume_improvements": resume_tips
    }
