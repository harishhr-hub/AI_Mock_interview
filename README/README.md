# AI Mock Interviewer

An AI-powered mock interview system that parses resumes, analyzes job descriptions, and conducts interactive interviews with real-time feedback and scoring using **Groq (Llama-3.1)**.

## Features

- **Resume Parsing**: Automatically extracts text from uploaded PDF resumes.
- **JD Analysis**: Tailors interview questions based on the provided Job Description.
- **Interactive Interview**: Sequential questioning with dynamic difficulty adjustment.
- **Real-time Feedback**: Get instant scores and feedback for every answer.
- **Final Report**: Generates a comprehensive performance report and PDF summary.

## Prerequisites

- **Python 3.8+**
- **Groq API Key**: Obtain one from [Groq Cloud Console](https://console.groq.com/).

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ai_mock_interviewer
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Running the Application

### 1. Start the Backend (FastAPI)
Open a terminal and run:
```bash
uvicorn backend.main:app --reload
```
The backend will be available at `http://127.0.0.1:8000`.

### 2. Start the Frontend (Streamlit)
Open another terminal (with the virtual environment activated) and run:
```bash
streamlit run frontend/app.py
```
The frontend will open in your browser at `http://localhost:8501`.

## Usage Guide

1. **Upload Resume**: Provide your resume in PDF format.
2. **Paste JD**: Input the Job Description you are preparing for.
3. **Start Interview**: Click the "Start Interview" button.
4. **Answer Questions**: Type your response to each question and click "Submit Answer".
5. **View Results**: Check your score and feedback after each round.
6. **Final Report**: Once finished, view your overall performance summary and download the PDF report.

## Project Structure

- `backend/`: FastAPI application, interviewer logic, and report generation.
- `frontend/`: Streamlit UI for user interaction.
- `requirements.txt`: Project dependencies.
- `.env`: API configuration.

## Demo Video
<video controls src="interviewer.py - ai_mock_interviewer - main settings - Visual Studio Code 2026-02-01 18-02-55.mp4" title="Demo Video"></video>


<video controls src="interviewer.py - ai_mock_interviewer - main settings - Visual Studio Code 2026-02-01 18-02-55.mp4" title="Demo Video"></video>

