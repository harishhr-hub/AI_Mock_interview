import os
import re
from groq import Groq


class InterviewSession:
    def __init__(self, resume, jd):
        self.resume = resume
        self.jd = jd

        self.level = "easy"
        self.count = 0
        self.max_q = 5

        self.questions = []     # <<< ADD THIS
        self.scores = []

        self.bonus_round = False

    def next_question(self):
        if self.count >= self.max_q:
            return None

        prompt = f"""
Ask ONE {self.level} technical interview question
based on this resume and job description.

Resume:
{self.resume}

Job Description:
{self.jd}
"""

        from groq import Groq
        import os

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )

        q = response.choices[0].message.content.strip()

        # ✅ STORE QUESTION
        self.questions.append(q)

        self.count += 1
        return q

    def update_difficulty(self, avg):
        if avg > 7:
            self.level = "hard"
        elif avg > 4:
            self.level = "medium"
        else:
            self.level = "easy"

    def is_finished(self):
        return self.count >= self.max_q

