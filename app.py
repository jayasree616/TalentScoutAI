import streamlit as st
import json
import pandas as pd

from jd_parser import parse_jd
from matcher import calculate_match_score
from engagement import simulate_conversation
from scorer import final_score
from resume_parser import parse_resume


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="TalentScout AI",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI-Powered Talent Scouting & Engagement Agent")
st.subheader("Smart Candidate Discovery + Resume Screening + Interest Analysis")

st.markdown("---")


# --------------------------------------------------
# Resume Upload Section
# --------------------------------------------------

st.write("## 📄 Upload Candidate Resumes")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} resume(s) uploaded successfully")

st.markdown("---")


# --------------------------------------------------
# JD Input Section
# --------------------------------------------------

st.write("## 📝 Paste Job Description")

job_description = st.text_area(
    "Enter Job Description",
    height=250,
    placeholder="Example: Looking for Python Developer with Machine Learning and 1 year experience..."
)


# --------------------------------------------------
# Run Button
# --------------------------------------------------

if st.button("🚀 Run Talent Scout Agent"):

    if not job_description.strip():
        st.warning("Please enter a Job Description first.")
        st.stop()

    with st.spinner("Analyzing candidates using AI..."):

        # ------------------------------------------
        # Step 1: Parse JD
        # ------------------------------------------

        parsed_jd = parse_jd(job_description)

        st.write("## 📌 Parsed Job Description")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Role",
            parsed_jd.get("role", "Not Found")
        )

        col2.metric(
            "Experience Required",
            f"{parsed_jd.get('experience_required', 0)} Years"
        )

        col3.metric(
            "Required Skills Count",
            len(parsed_jd.get("must_have_skills", []))
        )

        st.info(
            f"Required Skills: {', '.join(parsed_jd.get('must_have_skills', []))}"
        )

        st.markdown("---")

        # ------------------------------------------
        # Step 2: Candidate Source
        # ------------------------------------------

        candidates = []

        if uploaded_files:
            st.info("Using uploaded resumes for candidate analysis...")

            for uploaded_file in uploaded_files:
                candidate = parse_resume(uploaded_file)
                candidates.append(candidate)

        else:
            st.warning("No resumes uploaded. Using backup candidate database.")

            with open("candidate_data.json", "r") as file:
                candidates = json.load(file)

        results = []

        # ------------------------------------------
        # Step 3: Candidate Matching
        # ------------------------------------------

        for candidate in candidates:

            match_score, explanation = calculate_match_score(
                candidate,
                parsed_jd
            )

            interest_score, transcript = simulate_conversation(candidate, parsed_jd)

            total = final_score(
                match_score,
                interest_score
            )

            # Better professional explanation
            strong_explanation = (
                f"{candidate.get('name', 'Candidate')} shows strong alignment "
                f"with the required role. Has experience in "
                f"{', '.join(candidate.get('skills', [])[:4])}. "
                f"Recommended for technical screening round."
            )

            results.append({
                "Candidate Name": candidate.get("name", "Unknown"),
                "Skills": ", ".join(candidate.get("skills", [])),
                "Experience": candidate.get("experience", 0),
                "Match Score": match_score,
                "Interest Score": interest_score,
                "Final Score": total,
                "Explanation": strong_explanation,
                "Conversation": transcript
            })

        # ------------------------------------------
        # Step 4: Sort Results
        # ------------------------------------------

        results.sort(
            key=lambda x: x["Final Score"],
            reverse=True
        )

        top_candidate = results[0]

        # ------------------------------------------
        # Step 5: Best Candidate Highlight
        # ------------------------------------------

        st.success("🏆 Best Recommended Candidate")

        st.subheader(
            f"{top_candidate['Candidate Name']} "
            f"(Final Score: {top_candidate['Final Score']})"
        )

        st.info(
            "Recommended Action: Schedule Technical Interview"
        )

        st.markdown("---")

        # ------------------------------------------
        # Step 6: Shortlisted Candidates Table
        # ------------------------------------------

        st.write("## ✅ Recruiter-Ready Shortlisted Candidates")

        top_df = pd.DataFrame(results)[
            [
                "Candidate Name",
                "Experience",
                "Match Score",
                "Interest Score",
                "Final Score"
            ]
        ]
        top_df.index = range(1, len(top_df) + 1)

        st.dataframe(
            top_df,
            width="stretch"
        )

        st.markdown("---")

        # ------------------------------------------
        # Step 7: Detailed Candidate Cards
        # ------------------------------------------

        for index, result in enumerate(results, start=1):

            st.subheader(
                f"#{index} 👤 {result['Candidate Name']}"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Match Score",
                result["Match Score"]
            )

            col2.metric(
                "Interest Score",
                result["Interest Score"]
            )

            col3.metric(
                "Final Score",
                result["Final Score"]
            )

            st.write("### Extracted Skills")
            st.success(result["Skills"])

            st.write("### Why this candidate?")
            st.info(result["Explanation"])

            with st.expander(
                "📩 View Simulated Recruiter Conversation"
            ):
                st.write(result["Conversation"])

            st.markdown("---")