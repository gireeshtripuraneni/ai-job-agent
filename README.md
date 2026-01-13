# 🤖 AI Job Application Agent

An AI-powered, agentic workflow that helps job seekers evaluate job fit, identify skill gaps, and prepare smarter applications using structured decision-making.

---

## 🚀 What This Project Does

This system analyzes a candidate’s resume and a job description to produce:

- Job–skill match percentage
- Fit classification (Good / Partial / Not a Fit)
- Matched and missing skills
- Personalized learning roadmap
- Resume improvement suggestions
- Tailored cover letter
- Human-in-the-loop application decision

---

## 🧠 Agent-Based Architecture

This project is built as a **multi-agent system**, where each agent has a clear responsibility:

1. **Resume Analysis Agent** – Extracts technical skills from resume text  
2. **JD Analysis Agent** – Parses required skills from job descriptions  
3. **Fit Decision Agent** – Computes match percentage and classifies fit  
4. **Guidance Agent** – Generates learning roadmap and improvement tips  
5. **Application Assistant Agent** – Creates a tailored cover letter  
6. **Final Output Agent** – Produces a clean, recruiter-ready summary  

---

## 🔁 Human-in-the-Loop Design

The system does **not auto-apply**.

A human reviewer must:
- Review the AI-generated outputs
- Approve or reject the application decision

This ensures safety, control, and real-world usability.

---

## 🛠 Tech Stack

- Python 3.10+
- Agent-oriented design
- Relay.app (workflow orchestration)
- Scikit-learn

---

## 📂 Project Structure

