import PyPDF2
import re


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_name(text):
    lines = text.split("\n")

    for line in lines[:10]:
        line = line.strip()

        if len(line) > 3 and len(line.split()) <= 4:
            if not any(char.isdigit() for char in line):
                return line.upper()

    return "Unknown Candidate"


def extract_experience(text):
    text_lower = text.lower()

    patterns = [
        r'(\d+)\+?\s+years',
        r'(\d+)\+?\s+year',
        r'(\d+)\s+yrs',
        r'(\d+)\s+yr'
    ]

    for pattern in patterns:
        match = re.search(pattern, text_lower)

        if match:
            return float(match.group(1))

    # fresher fallback
    if "internship" in text_lower or "project" in text_lower:
        return 1

    return 1


def extract_skills(text):
    skill_keywords = [
        "Python", "Java", "JavaScript", "SQL",
        "HTML", "CSS", "MongoDB", "MySQL",
        "AWS", "Docker", "Kubernetes",
        "Machine Learning", "Deep Learning",
        "Flask", "Django", "React", "Node.js",
        "Express.js", "Git", "CI/CD",
        "Linux", "TensorFlow", "PyTorch",
        "OpenCV", "NLP", "Streamlit",
        "Generative AI", "Gemini API"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skill_keywords:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills[:15]


def parse_resume(uploaded_file):
    resume_text = extract_text_from_pdf(uploaded_file)

    candidate = {
        "name": extract_name(resume_text),
        "skills": extract_skills(resume_text),
        "experience": extract_experience(resume_text),
        "bio": "Profile generated using local resume parsing"
    }

    return candidate