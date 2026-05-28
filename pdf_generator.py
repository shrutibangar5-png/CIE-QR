from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime


def create_pdf(data, qr_path):

    # Create unique PDF filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    pdf = canvas.Canvas(
        f"output/labels_{timestamp}.pdf",
        pagesize=A4
    )

    # Add QR Image
    qr = ImageReader(qr_path)

    pdf.drawImage(
        qr,
        180,
        500,
        width=250,
        height=250
    )

    # Company Name
    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawString(
        180,
        780,
        "CIE"
    )

    # Title
    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        180,
        760,
        f"QR Generated For {len(data)} Entries"
    )

    # Table Preview
    y = 450

    pdf.setFont("Helvetica", 8)

    for index, row in data.iterrows():

        text = (
            f"{row['Part Number']} | "
            f"{row['Batch']} | "
            f"{row['Serial Number']}"
        )

        pdf.drawString(50, y, text)

        y -= 10

    pdf.save()

    print("PDF Generated Successfully")