import os
import json
import requests


class AIService:

    def __init__(self):

        self.api_key = os.getenv("OPENROUTER_API_KEY")

        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

        self.model = "inclusionai/ling-3.0-flash:free"

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "CareerPilot AI"
        }

    def clean_json(self, text):

        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]

        elif "```" in text:
            text = text.split("```")[1].split("```")[0]

        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            text = text[start:end + 1]

        return text.strip()

    def analyze_resume(self, resume_text, job_description):

        prompt = f"""
You are CareerPilot AI.

You are an ATS Resume Expert.

Compare the resume with the job description.

IMPORTANT

- NEVER invent skills.
- NEVER invent certifications.
- NEVER invent education.
- NEVER invent projects.
- NEVER invent companies.
- NEVER invent achievements.
- NEVER invent technologies.
- NEVER invent experience.
- Use ONLY information already present in the resume.
- Rewrite only grammar, formatting and ATS keywords.
- Keep every fact truthful.

Return ONLY valid JSON.

{{
    "ats_score":85,
    "career_readiness":90,
    "confidence":92,
    "keyword_match":88,

    "matched_skills":[
        "Python"
    ],

    "missing_skills":[
        "Docker"
    ],

    "resume_improvements":[
        "Improve project descriptions."
    ],

    "change_explanations":[
        "Added ATS keywords."
    ],

    "optimized_resume":"Professionally rewritten resume using ONLY information from the original resume.",

    "recruiter_recommendation":"Shortlisted"
}}

Resume

{resume_text}

Job Description

{job_description}
"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]

        content = self.clean_json(content)

        return json.loads(content)

    def generate_interview_questions(self, resume_text, job_description):

        prompt = f"""
You are CareerPilot AI.

Generate exactly 10 interview questions.

Include:

- HR
- Technical
- Resume Based
- Project Based
- Behavioural

Return ONLY JSON.

{{
    "questions":[
        "Tell me about yourself."
    ]
}}

Resume

{resume_text}

Job Description

{job_description}
"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]

        content = self.clean_json(content)

        data = json.loads(content)

        return data["questions"]