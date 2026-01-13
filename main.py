# main.py

import os
from agents.fit_agent import fit_decision_agent
from agents.resume_agent import resume_agent
from agents.jd_agent import jd_agent
from agents.guidance_agent import guidance_agent
from agents.application_agent import application_preparation_agent



# Absolute path of the current file (main.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths to data files
resume_path = os.path.join(BASE_DIR, "data", "sample_resume.txt")
jd_path = os.path.join(BASE_DIR, "data", "sample_jd.txt")

# Debug prints (temporary)
print("Looking for resume at:", resume_path)
print("Looking for JD at:", jd_path)

with open(resume_path, "r") as f:
    resume_text = f.read()

with open(jd_path, "r") as f:
    jd_text = f.read()

resume_output = resume_agent(resume_text)
jd_output = jd_agent(jd_text)

print("\nResume Agent Output:")
print(resume_output)

print("\nJob Description Agent Output:")
print(jd_output)
fit_output = fit_decision_agent(
    resume_output["skills"],
    jd_output["required_skills"]
)

print("\nFit Decision Agent Output:")
print(fit_output)
guidance_output = guidance_agent(
    fit_output["missing_skills"],
    fit_output["fit_status"]
)

print("\nGuidance Agent Output:")
print(guidance_output)
application_output = application_preparation_agent(
    fit_output["fit_status"],
    fit_output["matched_skills"],
    fit_output["missing_skills"],
    candidate_name="Your Name"
)

print("\nApplication Preparation Agent Output:")
print(application_output)
