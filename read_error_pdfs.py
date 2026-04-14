import pdfplumber
import sys

pdfs_with_errors = [
    r'd:\College\Programming\Data-Analytics\68d12fc7eebb3ba2ffec8f92.pdf',
    r'd:\College\Programming\Data-Analytics\68da573adcf3946995d751cf.pdf',
    r'd:\College\Programming\Data-Analytics\67fdf7a89a28c2606cb64c23.pdf',
]

for pdf_path in pdfs_with_errors:
    import os
    fname = os.path.basename(pdf_path)
    print(f"\n{'='*60}")
    print(f"FILE: {fname}")
    print('='*60)
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Pages: {len(pdf.pages)}")
            for i, page in enumerate(pdf.pages[:3]):
                try:
                    text = page.extract_text(x_tolerance=2, y_tolerance=2)
                    if text:
                        # Replace problem chars
                        text = text.encode('ascii', 'replace').decode('ascii')
                        print(f"\n--- Page {i+1} ---")
                        print(text[:1500])
                except Exception as e:
                    print(f"Page {i+1} error: {e}")
    except Exception as e:
        print(f"File error: {e}")
