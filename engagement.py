import random


def simulate_conversation(candidate, parsed_jd):
    interest_levels = {
        "high": 90,
        "medium": 70,
        "low": 50
    }

    selected = random.choice(
        list(interest_levels.keys())
    )

    interest_score = interest_levels[selected]

    role = parsed_jd.get(
        "role",
        "this role"
    )

    skills = parsed_jd.get(
        "must_have_skills",
        []
    )

    exp_required = parsed_jd.get(
        "experience_required",
        1
    )

    skill_text = ", ".join(skills[:3]) \
        if skills else "relevant technologies"

    transcript = f"""
AI Recruiter:
Hi {candidate.get('name', 'Candidate')}, your profile looks strong for our {role} position.

Candidate:
Thank you! I’m interested. Could you share more about the role?

AI Recruiter:
This role requires strong experience in {skill_text}, along with problem-solving and communication skills. We are specifically looking for candidates with around {exp_required}+ years of practical experience.

Candidate:
That aligns well with my projects and technical background. I would be interested in discussing the next steps.
"""

    if selected == "medium":
        transcript += """
Candidate:
I would also like to understand the team structure and work expectations.
"""

    if selected == "low":
        transcript += """
Candidate:
I am currently exploring multiple offers before making a final decision.
"""

    return interest_score, transcript