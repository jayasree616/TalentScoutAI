def calculate_match_score(candidate, parsed_jd):
    required_skills = parsed_jd.get("must_have_skills", [])
    required_exp = parsed_jd.get("experience_required", 0)

    candidate_skills = candidate.get("skills", [])
    candidate_exp = candidate.get("experience", 0)

    # Skill Match
    matched_skills = len(
        set(skill.lower() for skill in required_skills)
        &
        set(skill.lower() for skill in candidate_skills)
    )

    skill_match_score = (
        matched_skills / max(len(required_skills), 1)
    ) * 40

    # Experience Match
    if candidate_exp >= required_exp:
        experience_score = 20
    elif candidate_exp >= required_exp - 1:
        experience_score = 15
    else:
        experience_score = 8

    # Communication Quality (mock score)
    communication_score = 10

    # Location relevance (simple demo score)
    location_score = 10

    total_score = round(
        skill_match_score +
        experience_score +
        communication_score +
        location_score,
        2
    )

    explanation = (
        f"Matched {matched_skills}/{len(required_skills)} required skills, "
        f"{candidate_exp} years experience, strong communication fit."
    )

    return total_score, explanation