import pdfplumber

from docx import Document


class ResumeParser:

    @staticmethod
    def extract_text(path):

        if path.endswith(".pdf"):

            return ResumeParser.extract_pdf(path)

        return ResumeParser.extract_docx(path)

    @staticmethod
    def extract_pdf(path):

        text=""

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                t=page.extract_text()

                if t:

                    text+=t+"\n"

        return text

    @staticmethod
    def extract_docx(path):

        doc=Document(path)

        text=""

        for p in doc.paragraphs:

            text+=p.text+"\n"

        return text