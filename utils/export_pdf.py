# Name: Youssef Shafeek
# Date: 05/30/2025
# File Description: This utility module defines a function to export a structured 
# customer feedback report into a formatted PDF 

from fpdf import FPDF

# This function creates a PDF file from given text.
# Set Margins and font information (style and font) 
def export_to_pdf(text: str, filename: str = "customer_feedback_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Split lines to avoid overflowing width
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    
    # Generate the PDF file
    pdf.output(filename)
    print(f"\n PDF exported to: {filename}")
