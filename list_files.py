import os, glob, datetime

path = r'd:\College\Programming\Data-Analytics'

print("=== PDFs ===")
pdfs = glob.glob(os.path.join(path, '*.pdf'))
pdfs.sort(key=lambda x: os.path.getmtime(x), reverse=True)
for p in pdfs:
    mtime = os.path.getmtime(p)
    dt = datetime.datetime.fromtimestamp(mtime)
    print(dt.strftime('%Y-%m-%d %H:%M') + ' | ' + os.path.basename(p) + ' | ' + str(os.path.getsize(p)) + ' bytes')

print("\n=== Notebooks ===")
nbs = glob.glob(os.path.join(path, '*.ipynb'))
nbs.sort(key=lambda x: os.path.getmtime(x), reverse=True)
for p in nbs:
    mtime = os.path.getmtime(p)
    dt = datetime.datetime.fromtimestamp(mtime)
    print(dt.strftime('%Y-%m-%d %H:%M') + ' | ' + os.path.basename(p))
