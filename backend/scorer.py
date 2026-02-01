import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def score_answer(q, a):

    prompt = f"""
Score 0-10 for Accuracy, Clarity, Depth, Relevance.
Return JSON only.

Question: {q}
Answer: {a}

Format:
{{"accuracy":x,"clarity":x,"depth":x,"relevance":x}}
"""

    r = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(r.choices[0].message.content)
