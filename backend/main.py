from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, Form
from backend.interviewer import InterviewSession
from backend.scorer import score_answer
from backend.resume_parser import parse_resume

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from groq import Groq
import os
import shutil
import random

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()
session = None


# ---------------- START INTERVIEW ----------------

@app.post("/start")
async def start_interview(resume: UploadFile, jd: str = Form(...)):

    global session

    with open("resume.pdf", "wb") as f:
        shutil.copyfileobj(resume.file, f)

    resume_text = parse_resume("resume.pdf")

    session = InterviewSession(resume_text, jd)

    q = session.next_question()

    return {"question": q}


# ---------------- NEXT QUESTION ----------------

@app.post("/next")
async def next_question():

    global session

    q = session.next_question()

    if q is None:
        return {"done": True}

    return {"question": q}


# ---------------- ANSWER ----------------

@app.post("/answer")
async def answer(answer: str = Form(...)):

    global session

    q = session.questions[-1]

    score = score_answer(q, answer)

    avg = sum(score.values()) / len(score.values())
    session.scores.append(avg)

    session.update_difficulty(avg)

    # ---- Generate feedback FIRST ----
    feedback_prompt = f"""
Give short feedback for this answer.

Question: {q}
Answer: {answer}
Scores: {score}

Provide strengths and improvements in 2-3 lines.
"""

    fb = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": feedback_prompt}],
    )

    feedback = fb.choices[0].message.content.strip()

    # ---- If interview finished ----
    if session.is_finished():

        final_score = round(sum(session.scores) / len(session.scores) * 10, 2)
        decision = "PASS" if final_score >= 70 else "FAIL"
         
        print("BACKEND RESPONSE:", {
            "score": score,
            "feedback": feedback,
            "next_question": next_q,
        })

        
        return {
            "score": final_score,
            "recommendation": decision,
            "feedback": feedback,
            "next_question": "Interview completed.",
            "finished": True
        }

    # ---- Else continue ----
    next_q = session.next_question()

    return {
        "score": score,
        "feedback": feedback,
        "next_question": next_q,
        "finished": False
    }


# ---------------- QUICK REPORT ----------------

@app.get("/report")
def report():

    final = sum(session.scores) / len(session.scores) * 10
    level = "Strong" if final > 70 else "Average" if final > 40 else "Needs Improvement"

    return {
        "readiness_score": round(final, 2),
        "level": level
    }


# ---------------- FINAL REPORT + PDF ----------------

@app.get("/final-report")
def final_report():

    global session

    if not session or not session.scores:
        return {"error": "Interview not completed"}

    avg_score = round(sum(session.scores) / len(session.scores) * 10, 2)

    decision = "PASS" if avg_score >= 70 else "FAIL"

    strengths = "Good technical understanding and structured answers."
    weaknesses = "Needs improvement in depth and real-world examples."

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate("Interview_Report.pdf", pagesize=A4)

    content = [
        Paragraph("<b>Final Interview Report</b>", styles["Title"]),
        Paragraph(f"Score: {avg_score}", styles["Normal"]),
        Paragraph(f"Decision: {decision}", styles["Normal"]),
        Paragraph(f"Strengths: {strengths}", styles["Normal"]),
        Paragraph(f"Weaknesses: {weaknesses}", styles["Normal"]),
    ]

    doc.build(content)

    return {
        "average_score": avg_score,
        "decision": decision,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "pdf": "Interview_Report.pdf"
    }
