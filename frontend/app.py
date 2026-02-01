import streamlit as st
import requests

BACKEND = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Mock Interview")

st.title("AI Mock Interview")

# ---------------- Initialize session ----------------
if "question" not in st.session_state:
    st.session_state.question = None

if "started" not in st.session_state:
    st.session_state.started = False

# ---------------- Start Interview ----------------
jd = st.text_area("Paste Job Description")

resume = st.file_uploader("Upload Resume PDF", type=["pdf"])

if st.button("Start Interview"):

    if not jd or not resume:
        st.error("Please provide Job Description and Resume")
        st.stop()

    files = {"resume": resume}
    data = {"jd": jd}

    resp = requests.post(f"{BACKEND}/start", files=files, data=data)

    if resp.status_code != 200:
        st.error("Backend error")
        st.stop()

    st.session_state.question = resp.json()["question"]
    st.session_state.started = True

# ---------------- Show Question ----------------
if st.session_state.started:

    st.subheader("Question")
    st.write(st.session_state.question)

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):

        resp = requests.post(
            f"{BACKEND}/answer",
            data={"answer": answer},
        )

        if resp.status_code != 200:
            st.error("Backend error")
            st.stop()

        data = resp.json()

        # Score
        if "score" in data:
            st.subheader("Score")
            st.json(data["score"])

        # Feedback
        if "feedback" in data:
            st.subheader("Feedback")
            st.write(data["feedback"])

        # Interview finished?
        if data.get("finished"):

            st.success("Interview Completed!")

            rep = requests.get(f"{BACKEND}/final-report")
            if rep.status_code == 200:
                st.subheader("Final Report")
                st.json(rep.json())

            st.stop()

        # Next question
        st.session_state.question = data["next_question"]
