import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


def parse_jd(job_description):
    prompt = f"""
You are an expert technical recruiter AI.

Carefully analyze this Job Description and extract ONLY:

1. Exact Job Role
2. Must-have Technical Skills
3. Required Experience in Years

IMPORTANT RULES:
- Do NOT invent skills
- Use only skills explicitly mentioned
- If Machine Learning is mentioned, include it
- If Cloud/AWS/GCP is mentioned, include it
- If Communication is mentioned, include it
- If experience is written like "2+ years", return 2
- Return ONLY valid JSON
- No markdown
- No explanation text

Output format:

{{
    "role": "",
    "must_have_skills": [],
    "experience_required": 0
}}

Job Description:
{job_description}
"""

    try:
        response = model.generate_content(prompt)

        cleaned = (
            response.text
            .strip()
            .replace("```json", "")
            .replace("```", "")
        )

        parsed = json.loads(cleaned)

        if not parsed.get("role"):
            parsed["role"] = "Software Developer"

        if not parsed.get("must_have_skills"):
            parsed["must_have_skills"] = ["Python"]

        if parsed.get("experience_required", 0) == 0:
            parsed["experience_required"] = 1

        return parsed

    except Exception as e:
        print("JD Parsing Error:", e)

        return {
            "role": "Python Developer",
            "must_have_skills": ["Python", "Machine Learning"],
            "experience_required": 2
        }