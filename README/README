AI Mock Interviewer
An AI-powered mock interview system that parses resumes, analyzes job descriptions, and conducts interactive interviews with real-time feedback and scoring using Groq (Llama-3.1).

Features
Resume Parsing: Automatically extracts text from uploaded PDF resumes.
JD Analysis: Tailors interview questions based on the provided Job Description.
Interactive Interview: Sequential questioning with dynamic difficulty adjustment.
Real-time Feedback: Get instant scores and feedback for every answer.
Final Report: Generates a comprehensive performance report and PDF summary.
Prerequisites
Python 3.8+
Groq API Key: Obtain one from Groq Cloud Console.
Installation
1. Clone the Repository
git clone <repository-url>
cd ai_mock_interviewer
2. Set Up Virtual Environment (Recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here
Running the Application
1. Start the Backend (FastAPI)
Open a terminal and run:

uvicorn backend.main:app --reload
The backend will be available at http://127.0.0.1:8000.

2. Start the Frontend (Streamlit)
Open another terminal (with the virtual environment activated) and run:

streamlit run frontend/app.py
The frontend will open in your browser at http://localhost:8501.

Usage Guide
Upload Resume: Provide your resume in PDF format.
Paste JD: Input the Job Description you are preparing for.
Start Interview: Click the "Start Interview" button.
Answer Questions: Type your response to each question and click "Submit Answer".
View Results: Check your score and feedback after each round.
Final Report: Once finished, view your overall performance summary and download the PDF report.
Project Structure
backend/: FastAPI application, interviewer logic, and report generation.
frontend/: Streamlit UI for user interaction.
requirements.txt: Project dependencies.
.env: API configuration.
Demo Video
