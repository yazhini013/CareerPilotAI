import os
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    jsonify,
    send_file,
    url_for
)

from werkzeug.utils import secure_filename

from config import Config

from database import (
    create_user,
    verify_user,
    save_analysis,
    get_history
)

from services.resume_parser import ResumeParser
from services.ai_service import AIService

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["REPORT_FOLDER"], exist_ok=True)

ai_service = AIService()


# -------------------------------------------------
# HOME
# -------------------------------------------------

@app.route("/")
def home():

    if "email" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# -------------------------------------------------
# REGISTER
# -------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name","").strip()
        email = request.form.get("email","").strip().lower()
        password = request.form.get("password","")

        if len(password) < 6:

            return render_template(
                "register.html",
                error="Password must be at least 6 characters."
            )

        success = create_user(
            name,
            email,
            password
        )

        if not success:

            return render_template(
                "register.html",
                error="Email already exists."
            )

        session["name"] = name
        session["email"] = email

        return redirect(url_for("dashboard"))

    return render_template("register.html")


# -------------------------------------------------
# LOGIN
# -------------------------------------------------

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email","").strip().lower()
        password = request.form.get("password","")

        user = verify_user(
            email,
            password
        )

        if user is None:

            return render_template(
                "login.html",
                error="Invalid email or password."
            )

        session["email"] = user["email"]
        session["name"] = user["name"]

        return redirect(url_for("dashboard"))

    return render_template("login.html")


# -------------------------------------------------
# LOGOUT
# -------------------------------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))
# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

@app.route("/dashboard")
def dashboard():

    if "email" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        name=session["name"]
    )


# -------------------------------------------------
# UPLOAD PAGE
# -------------------------------------------------

@app.route("/upload")
def upload():

    if "email" not in session:
        return redirect(url_for("login"))

    return render_template("upload.html")


# -------------------------------------------------
# ANALYZE RESUME
# -------------------------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    if "email" not in session:
        return redirect(url_for("login"))

    if "resume" not in request.files:

        return render_template(
            "upload.html",
            error="Please upload a resume."
        )

    file = request.files["resume"]

    if file.filename == "":

        return render_template(
            "upload.html",
            error="Please select a resume."
        )

    job_description = request.form.get(
        "job_description",
        ""
    ).strip()

    if job_description == "":

        return render_template(
            "upload.html",
            error="Please enter the Job Description."
        )

    extension = file.filename.rsplit(".", 1)[1].lower()

    if extension not in app.config["ALLOWED_EXTENSIONS"]:

        return render_template(
            "upload.html",
            error="Only PDF and DOCX files are allowed."
        )

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    print("Resume saved.")

    try:

        resume_text = ResumeParser.extract_text(filepath)

        print("Resume parsed successfully.")

    except Exception as e:

        print(e)

        return render_template(
            "upload.html",
            error=f"Resume Parsing Error: {str(e)}"
        )

    if resume_text.strip() == "":

        return render_template(
            "upload.html",
            error="Unable to extract text from the resume."
        )

    print("Calling AI Service...")

    try:

        result = ai_service.analyze_resume(
            resume_text,
            job_description
        )

        print("AI Response Received")
        print(result)

    except Exception as e:

        print("AI ERROR:", e)

        return render_template(
            "upload.html",
            error=f"AI Error: {str(e)}"
        )

    session["resume_text"] = resume_text
    session["job_description"] = job_description
    session["latest_result"] = result

    save_analysis(
        session["email"],
        result["ats_score"],
        json.dumps(result["matched_skills"]),
        json.dumps(result["missing_skills"]),
        result["optimized_resume"]
    )
    print("STEP 1 - File Saved")

    return render_template(
        "results.html",
        result=result
    )
# -------------------------------------------------
# HISTORY
# -------------------------------------------------

@app.route("/history")
def history():

    if "email" not in session:
        return redirect(url_for("login"))

    history_data = get_history(
        session["email"]
    )

    return render_template(
        "history.html",
        history=history_data
    )


# -------------------------------------------------
# INTERVIEW PAGE
# -------------------------------------------------

@app.route("/interview")
def interview():

    if "email" not in session:
        return redirect(url_for("login"))

    return render_template("interview.html")


# -------------------------------------------------
# AI INTERVIEW API
# -------------------------------------------------

@app.route("/api/interview", methods=["POST"])
def api_interview():

    if "email" not in session:

        return jsonify({
            "error": "Please login first."
        }), 401

    resume_text = session.get("resume_text", "")
    job_description = session.get("job_description", "")

    if resume_text == "" or job_description == "":

        return jsonify({
            "questions": [
                "Please analyze your resume before generating interview questions."
            ]
        })

    print("Generating Interview Questions...")

    try:

        questions = ai_service.generate_interview_questions(
            resume_text,
            job_description
        )

        print("Interview AI Response:")
        print(questions)

        if isinstance(questions, dict):

            questions = questions.get(
                "questions",
                []
            )

        if not isinstance(questions, list):

            questions = []

        if len(questions) == 0:

            questions = [

                "Tell me about yourself.",

                "Explain your final year project.",

                "Why are you interested in this role?",

                "Describe one technical challenge you solved.",

                "Explain your strongest programming language.",

                "How do you debug an application?",

                "Describe your teamwork experience.",

                "How do you manage deadlines?",

                "Where do you see yourself in five years?",

                "Why should we hire you?"

            ]

        return jsonify({

            "questions": questions

        })

    except Exception as e:

        print("Interview Error:")
        print(e)

        return jsonify({

            "questions":[

                "Tell me about yourself.",

                "Explain your final year project.",

                "What are your strengths?",

                "Describe a difficult bug you fixed.",

                "How do you work in a team?",

                "Explain one database project.",

                "What is Flask?",

                "How do you optimize SQL queries?",

                "Why this company?",

                "Any questions for us?"

            ]

        })
    
# -------------------------------------------------
# DOWNLOAD OPTIMIZED RESUME
# -------------------------------------------------
@app.route("/download_resume")
def download_resume():

    if "email" not in session:
        return redirect(url_for("login"))

    if "latest_result" not in session:
        return redirect(url_for("upload"))

    report_path = os.path.join(
        app.config["REPORT_FOLDER"],
        "CareerPilot_Optimized_Resume.pdf"
    )

    doc = SimpleDocTemplate(report_path)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>CareerPilot AI - ATS Optimized Resume</b>", styles["Heading1"]))
    story.append(Paragraph("<br/>", styles["BodyText"]))

    resume = session["latest_result"]["optimized_resume"]

    for line in resume.split("\n"):

        if line.strip() == "":
            story.append(Paragraph("<br/>", styles["BodyText"]))
        else:
            story.append(Paragraph(line.replace("&", "&amp;"), styles["BodyText"]))

    doc.build(story)

    return send_file(
        report_path,
        as_attachment=True,
        download_name="CareerPilot_Optimized_Resume.pdf"
    )
# -------------------------------------------------
# DOWNLOAD AI REPORT
# -------------------------------------------------

@app.route("/download_report")
def download_report():

    if "email" not in session:
        return redirect(url_for("login"))

    if "latest_result" not in session:
        return redirect(url_for("upload"))

    result = session["latest_result"]

    report_path = os.path.join(
        app.config["REPORT_FOLDER"],
        "CareerPilot_AI_Report.txt"
    )

    with open(report_path, "w", encoding="utf-8") as f:

        f.write("=" * 80 + "\n")
        f.write("CAREERPILOT AI REPORT\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"ATS Score : {result.get('ats_score',0)}/100\n\n")

        f.write("MATCHED SKILLS\n")
        f.write("-" * 40 + "\n")

        for skill in result.get("matched_skills",[]):
            f.write(f"✓ {skill}\n")

        f.write("\n")

        f.write("MISSING SKILLS\n")
        f.write("-" * 40 + "\n")

        for skill in result.get("missing_skills",[]):
            f.write(f"• {skill}\n")

        f.write("\n")

        f.write("RESUME IMPROVEMENTS\n")
        f.write("-" * 40 + "\n")

        for item in result.get("resume_improvements",[]):
            f.write(f"• {item}\n")

        f.write("\n")

        f.write("CAREERPILOT AI CHANGE EXPLANATIONS\n")
        f.write("-" * 40 + "\n")

        for item in result.get("change_explanations",[]):
            f.write(f"• {item}\n")

        f.write("\n")

        f.write("ATS OPTIMIZED RESUME\n")
        f.write("=" * 80 + "\n\n")

        f.write(result.get("optimized_resume",""))

    return send_file(
        report_path,
        as_attachment=True,
        download_name="CareerPilot_AI_Report.txt"
    )


# -------------------------------------------------
# HEALTH CHECK
# -------------------------------------------------

@app.route("/health")
def health():

    return jsonify({

        "status": "running",

        "application": "CareerPilot AI",

        "version": "1.0"

    })


# -------------------------------------------------
# ERROR HANDLERS
# -------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):

    return render_template(
        "base.html"
    ), 404


@app.errorhandler(500)
def internal_error(e):

    return render_template(
        "base.html"
    ), 500


# -------------------------------------------------
# RUN APPLICATION
# -------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("CareerPilot AI Started Successfully")
    print("Open http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )