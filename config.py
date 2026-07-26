import os

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "careerpilot_secret"
    )

    UPLOAD_FOLDER = "uploads"

    REPORT_FOLDER = "reports"

    ALLOWED_EXTENSIONS = {
        "pdf",
        "docx"
    }