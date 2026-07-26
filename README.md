# CareerPilot AI

CareerPilot AI is an AI-powered career assistant that helps job seekers improve their resumes honestly and prepare for interviews.

Unlike many existing resume optimization tools, CareerPilot AI never adds fake skills, fake certifications, fake projects, or fake experience. It only improves the resume using the information already provided by the user, making it ATS-friendly while keeping every detail truthful.

---

# Project Idea

While exploring existing AI resume optimization tools, I noticed a common problem.

Most tools improve ATS scores by adding:
- Fake skills
- Fake certifications
- Fake projects
- Fake achievements
- Technologies that are not actually present in the resume

Although this may increase the ATS score, it can create problems during interviews because candidates may be asked about things they never actually worked on.

I wanted to solve this problem by building an AI that improves resumes without changing the truth.

---

# My Innovation

CareerPilot AI follows a Truthful Resume Optimization approach.

Instead of generating a completely new resume, it improves the existing resume while keeping every fact genuine.

CareerPilot AI:

- Uses only the information already available in the resume.
- Improves grammar and professional wording.
- Makes the resume ATS-friendly.
- Finds missing recruiter keywords.
- Explains every recommendation made by AI.
- Generates personalized interview questions using both the resume and the job description.

CareerPilot AI never:

- Adds fake skills.
- Adds fake certifications.
- Adds fake projects.
- Adds fake work experience.
- Adds fake achievements.
- Changes education details.
- Changes personal information.

---

# Features

- User Registration & Login
- Resume Upload (PDF & DOCX)
- ATS Score Analysis
- Career Readiness Score
- Keyword Match Score
- Matched Skills Detection
- Missing Skills Detection
- Resume Improvement Suggestions
- Explainable AI Recommendations
- Truthful Resume Optimization
- Personalized AI Interview Questions
- Download Optimized Resume
- Download AI Report
- Analysis History

---

# Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Database
- SQLite

### AI
- OpenRouter API
- inclusionai/ling-3.0-flash:free

### Libraries
- pdfplumber
- python-docx
- reportlab
- requests

---

# Project Structure

```
CareerPilotAi/
│
├── app.py
├── config.py
├── database.py
├── pdf_report.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── ai_service.py
│   └── resume_parser.py
│
├── templates/
├── static/
├── uploads/
├── reports/
└── database/
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CareerPilotAi.git
```

## 2. Open the project

```bash
cd CareerPilotAi
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a `.env` file

Create a file named `.env` in the project folder.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
SECRET_KEY=your_secret_key
```

---

# Getting an OpenRouter API Key

1. Visit https://openrouter.ai
2. Create a free account or sign in.
3. Click your profile icon.
4. Open **Keys**.
5. Click **Create API Key**.
6. Copy the generated API key.
7. Paste it into the `.env` file.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# How to Use

1. Register or Login.
2. Upload your Resume (PDF or DOCX).
3. Paste the Job Description.
4. Click **Analyze Resume**.
5. View:
   - ATS Score
   - Career Readiness
   - Keyword Match
   - Matched Skills
   - Missing Skills
   - Resume Improvements
   - Explainable AI Suggestions
   - Optimized Resume
6. Download the AI Report.
7. Download the Optimized Resume.
8. Generate AI Interview Questions based on your resume.

---

# What Makes CareerPilot AI Different?

Most AI resume builders only generate an ATS score or rewrite the resume by inventing new skills and experience.

CareerPilot AI focuses on ethical AI.

Instead of creating false information, it:

- Compares the resume with the job description.
- Improves ATS compatibility.
- Enhances professional wording.
- Identifies missing keywords.
- Explains every recommendation.
- Keeps every fact exactly as written by the user.

The goal is to help candidates create resumes they can confidently defend during interviews.

---

# Future Enhancements

- Voice-based AI Interview
- Resume PDF Export
- LinkedIn Profile Analysis
- Job Recommendation System
- Career Roadmap Generator
- Multi-language Resume Support

---

# Developed By

Yazhini

# CareerPilot AI

CareerPilot AI is an AI-powered career assistant that helps job seekers improve their resumes honestly and prepare for interviews.

Unlike many existing resume optimization tools, CareerPilot AI never adds fake skills, fake certifications, fake projects, or fake experience. It only improves the resume using the information already provided by the user, making it ATS-friendly while keeping every detail truthful.

---

# Project Idea

While exploring existing AI resume optimization tools, I noticed a common problem.

Most tools improve ATS scores by adding:
- Fake skills
- Fake certifications
- Fake projects
- Fake achievements
- Technologies that are not actually present in the resume

Although this may increase the ATS score, it can create problems during interviews because candidates may be asked about things they never actually worked on.

I wanted to solve this problem by building an AI that improves resumes without changing the truth.

---

# My Innovation

CareerPilot AI follows a Truthful Resume Optimization approach.

Instead of generating a completely new resume, it improves the existing resume while keeping every fact genuine.

CareerPilot AI:

- Uses only the information already available in the resume.
- Improves grammar and professional wording.
- Makes the resume ATS-friendly.
- Finds missing recruiter keywords.
- Explains every recommendation made by AI.
- Generates personalized interview questions using both the resume and the job description.

CareerPilot AI never:

- Adds fake skills.
- Adds fake certifications.
- Adds fake projects.
- Adds fake work experience.
- Adds fake achievements.
- Changes education details.
- Changes personal information.

---

# Features

- User Registration & Login
- Resume Upload (PDF & DOCX)
- ATS Score Analysis
- Career Readiness Score
- Keyword Match Score
- Matched Skills Detection
- Missing Skills Detection
- Resume Improvement Suggestions
- Explainable AI Recommendations
- Truthful Resume Optimization
- Personalized AI Interview Questions
- Download Optimized Resume
- Download AI Report
- Analysis History

---

# Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Database
- SQLite

### AI
- OpenRouter API
- inclusionai/ling-3.0-flash:free

### Libraries
- pdfplumber
- python-docx
- reportlab
- requests

---

# Project Structure

```
CareerPilotAi/
│
├── app.py
├── config.py
├── database.py
├── pdf_report.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── ai_service.py
│   └── resume_parser.py
│
├── templates/
├── static/
├── uploads/
├── reports/
└── database/
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/yazhini013/CareerPilotAi.git
```

## 2. Open the project

```bash
cd CareerPilotAi
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a `.env` file

Create a file named `.env` in the project folder.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
SECRET_KEY=your_secret_key
```

---

# Getting an OpenRouter API Key

1. Visit https://openrouter.ai
2. Create a free account or sign in.
3. Click your profile icon.
4. Open **Keys**.
5. Click **Create API Key**.
6. Copy the generated API key.
7. Paste it into the `.env` file.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# How to Use

1. Register or Login.
2. Upload your Resume (PDF or DOCX).
3. Paste the Job Description.
4. Click **Analyze Resume**.
5. View:
   - ATS Score
   - Career Readiness
   - Keyword Match
   - Matched Skills
   - Missing Skills
   - Resume Improvements
   - Explainable AI Suggestions
   - Optimized Resume
6. Download the AI Report.
7. Download the Optimized Resume.
8. Generate AI Interview Questions based on your resume.

---

# What Makes CareerPilot AI Different?

Most AI resume builders only generate an ATS score or rewrite the resume by inventing new skills and experience.

CareerPilot AI focuses on ethical AI.

Instead of creating false information, it:

- Compares the resume with the job description.
- Improves ATS compatibility.
- Enhances professional wording.
- Identifies missing keywords.
- Explains every recommendation.
- Keeps every fact exactly as written by the user.

The goal is to help candidates create resumes they can confidently defend during interviews.

---

# Future Enhancements

- Voice-based AI Interview
- Resume PDF Export
- LinkedIn Profile Analysis
- Job Recommendation System
- Career Roadmap Generator
- Multi-language Resume Support

---

# Developed By

Yazhini
