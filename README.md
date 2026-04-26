# TalentScoutAI
# 🎯 AI-Powered Talent Scouting & Engagement Agent

## Smart Candidate Discovery + Resume Screening + Interest Analysis

---

# 📌 Problem Statement

Recruiters spend hours manually reviewing resumes, identifying suitable candidates, and following up to assess candidate interest.

This project solves that problem by building an AI-Powered Talent Scouting & Engagement Agent that:

* Accepts a Job Description (JD) as input
* Parses role, required skills, and experience requirements
* Accepts multiple candidate resumes (PDF Upload)
* Matches candidates against the JD
* Simulates recruiter-candidate engagement
* Generates Match Score + Interest Score
* Produces a ranked recruiter-ready shortlist

This helps recruiters reduce manual effort and make faster hiring decisions with explainable AI support.

---

# 🚀 Key Features

## ✅ Job Description Parsing

The recruiter enters a Job Description.

The system extracts:

* Job Role
* Required Skills
* Required Experience

### Example

### Input

Need Java Developer with Cloud Technologies and 2 years experience

### Output

* Role → Java Developer
* Skills → Java, Cloud
* Experience → 2 Years

---

## ✅ Resume Upload + Parsing

Recruiters can upload multiple PDF resumes directly.

The system extracts:

* Candidate Name
* Skills
* Experience
* Resume Summary

This avoids manually creating candidate profiles.

---

## ✅ Candidate Matching Engine

Each candidate is evaluated using:

* Skill Match
* Experience Match
* Cloud/Technology Relevance
* Resume Strength

This generates a Match Score with explainability.

---

## ✅ Simulated Recruiter Engagement

The system simulates recruiter-candidate interaction to assess candidate interest.

This generates the:

# Interest Score

### Example

AI Recruiter → We found your profile suitable for our Java Developer role.

Candidate → This role aligns well with my experience. I’d be excited to move forward.

---

## ✅ Ranked Recruiter Shortlist

Final output includes:

* Match Score
* Interest Score
* Final Score
* Ranked Candidate List
* Best Recommended Candidate
* Recommended Action (Schedule Interview)

This allows recruiters to act immediately.

---

# 🛠 Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI Layer

* Google Gemini API

## Resume Parsing

* PyPDF2

## Data Handling

* Pandas

## Deployment

* Streamlit Community Cloud

## Version Control

* Git + GitHub

---

# 🏗 System Architecture

```text
Recruiter Inputs Job Description
            ↓
Gemini JD Parser
            ↓
Resume Upload (PDF)
            ↓
Resume Parser (PyPDF2)
            ↓
Candidate Matching Engine
            ↓
AI Recruiter Engagement Simulation
            ↓
Match Score + Interest Score
            ↓
Final Ranked Shortlist
            ↓
Recruiter Decision Support
```

---

# 📊 Scoring Logic

## Match Score (70%)

Calculated using:

* Required Skill Match
* Experience Match
* Cloud Technology Relevance
* Technical Alignment

---

## Interest Score (30%)

Calculated using:

* Simulated Recruiter-Candidate Interaction
* Candidate Response Quality
* Candidate Engagement Willingness

---

## Final Score Formula

```python
Final Score = (Match Score × 0.7) + (Interest Score × 0.3)
```

This ensures fair and explainable ranking.

---

# 💻 Local Setup Instructions

## Step 1 — Clone Repository

```bash
git clone https://github.com/jayasree616/TalentScoutAI
cd TalentScoutAI
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 4 — Install Requirements

```bash
pip install -r requirements.txt
```

---

## Step 5 — Create `.env` File

Create a file named:

```text
.env
```

Add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## Step 6 — Run Project

```bash
streamlit run app.py
```

---

# 📁 requirements.txt

```txt
streamlit
pandas
python-dotenv
google-generativeai
PyPDF2
```

---

# 🌐 Live Project URL

https://talentscoutai-1118.streamlit.app/

---

# 🎥 Demo Video

(Add your demo video link here)

Example:

https://drive.google.com/your-demo-link

---

# 📸 Sample Input

## Job Description

Need Java Developer with Cloud Technologies and 2 years experience

---

# 📸 Sample Output

## Best Recommended Candidate

ARJUN REDDY

### Match Score

60

### Interest Score

70

### Final Score

74.0

### Recommended Action

Schedule Technical Interview

---

# Output

<img width="1853" height="898" alt="image" src="https://github.com/user-attachments/assets/88c34f15-0dde-4489-a737-ef19bf302cb8" />


<img width="1772" height="850" alt="image" src="https://github.com/user-attachments/assets/04d8a6a8-ba37-48c0-940d-9504d2961618" />


<img width="1822" height="854" alt="image" src="https://github.com/user-attachments/assets/48acbe46-a1a3-4d69-b50b-271cd32079aa" />



# 🔮 Future Scope

Future improvements can include:

* LinkedIn Candidate Discovery
* Real Email / WhatsApp Outreach
* ATS Integration
* Recruiter Feedback Loop
* Interview Scheduling Automation
* LLM-based Resume Summarization

---

# 👩‍💻 Author

Mandava Jayasree

Final Year Engineering Student

AI + Full Stack Development Enthusiast


---

# Thank You
