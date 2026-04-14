import sys
try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

print(f"PyPDF2: {HAS_PYPDF2}")
print(f"pdfplumber: {HAS_PDFPLUMBER}")

import subprocess
result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
# Search for pdf-related
for line in result.stdout.splitlines():
    if 'pdf' in line.lower():
        print(line)
