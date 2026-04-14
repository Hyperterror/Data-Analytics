import json, os
nb_path = r'd:\College\Programming\Data-Analytics\DA-AG-014_SQL_Advanced_Functions.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    print(f"\nCell {i}: {src[:120]}")
