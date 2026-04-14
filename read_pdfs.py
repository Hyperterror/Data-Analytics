import pdfplumber
import os
import glob

path = r'd:\College\Programming\Data-Analytics'
pdfs = glob.glob(os.path.join(path, '*.pdf'))
pdfs.sort(key=lambda x: os.path.getsize(x))

for pdf_path in pdfs:
    fname = os.path.basename(pdf_path)
    size = os.path.getsize(pdf_path)
    print(f"\n{'='*60}")
    print(f"FILE: {fname} ({size} bytes)")
    print('='*60)
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"Pages: {total_pages}")
            # Extract first 2 pages to preview
            for i, page in enumerate(pdf.pages[:2]):
                text = page.extract_text()
                if text:
                    print(f"\n--- Page {i+1} ---")
                    print(text[:800])
    except Exception as e:
        print(f"Error: {e}")
