def application_preparation_agent(
    fit_status,
    matched_skills,
    missing_skills,
    candidate_name="Candidate"
):
    if fit_status == "Not a Fit":
        return {
            "apply_decision": "DO_NOT_APPLY",
            "reason": "Skill match too low",
            "cover_letter": None
        }

    cover_letter = f"""
Dear Hiring Manager,

I am writing to apply for this role. My experience with
{', '.join(matched_skills)} aligns well with your requirements.

I am currently strengthening my knowledge in
{', '.join(missing_skills)} to further improve my expertise.

I would welcome the opportunity to contribute and grow with your team.

Best regards,
{candidate_name}
"""

    decision = "AUTO_APPLY" if fit_status == "Good Fit" else "REVIEW_BEFORE_APPLY"

    return {
        "apply_decision": decision,
        "cover_letter": cover_letter.strip()
    }
