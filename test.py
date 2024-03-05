from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfFileReader, PdfFileWriter
import io

def create_pdf(template_path, output_path, data):
    # Load the PDF template
    template_pdf = PdfFileReader(open(template_path, "rb"))

    # Create a new PDF writer
    output = PdfFileWriter()

    # Get the existing template page
    template_page = template_pdf.getPage(0)

    # Create a new PDF with reportlab
    packet = io.BytesIO()
    new_pdf = canvas.Canvas(packet, pagesize=letter)

    # Add text using reportlab
    for key, value in data.items():
        new_pdf.drawString(200, 700 - len(data) * 20, f"{key}: {value}")

    new_pdf.showPage()
    new_pdf.save()

    packet.seek(0)

    # Merge the template with the new content
    new_page = PdfFileReader(packet).getPage(0)
    template_page.merge_page(new_page)

    # Add the merged page to the output PDF
    output.addPage(template_page)

    # Save the filled-in PDF to the output path
    with open(output_path, "wb") as output_file:
        output.write(output_file)

# Example usage
template_path = "/Users/marek/Desktop/aa.pdf"
output_path = "/Users/marek/Desktop/output.pdf"
json_data = {"Name": "John Doe", "Age": 25}

print("done")

create_pdf(template_path, output_path, json_data)
