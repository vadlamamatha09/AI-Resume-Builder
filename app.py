import streamlit as st
from fpdf import FPDF

st.title("AI Resume & Portfolio Builder")

name = st.text_input("Enter your name")
education = st.text_input("Enter your education")
skills = st.text_input("Enter your skills (comma separated)")
projects = st.text_input("Enter your projects")
experience = st.text_input("Enter your experience")

if st.button("Generate Resume"):

    skill_list = skills.split(",")
    formatted_skills = ""
    for skill in skill_list:
        formatted_skills += f"- {skill.strip()}\n"

    resume_text = f"""
{name.upper()}

CAREER OBJECTIVE
Motivated and dedicated Information Technology student seeking opportunities to apply technical skills.

EDUCATION
{education}

TECHNICAL SKILLS
{formatted_skills}

PROJECTS
{projects}

EXPERIENCE
{experience}

DECLARATION
I hereby declare that the above information is true to the best of my knowledge.
"""

    st.text_area("Generated Resume", resume_text, height=300)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, resume_text)

    file_name = name.replace(" ", "_") + "_Resume.pdf"
    pdf.output(file_name)

    with open(file_name, "rb") as f:
        st.download_button("Download Resume PDF", f, file_name=file_name)
