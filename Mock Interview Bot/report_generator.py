from fpdf import FPDF
import base64

def generate_pdf(text, filename="Interview_Feedback.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    raw = pdf.output(dest="S").encode("latin1")
    return base64.b64encode(raw).decode("utf-8")
