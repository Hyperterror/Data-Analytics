import pdfplumber
import os

pdf_path = r'd:\College\Programming\Data-Analytics\68d12fc7eebb3ba2ffec8f92.pdf'
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text(x_tolerance=2, y_tolerance=2)
        if text:
            text = text.encode('ascii', 'replace').decode('ascii')
            print(f"\n--- Page {i+1} ---")
            print(text)
