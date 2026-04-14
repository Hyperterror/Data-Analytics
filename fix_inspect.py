import json
import os

nb_path = r'd:\College\Programming\Data-Analytics\DA-AG-014_SQL_Advanced_Functions.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find index of Q6 and Q8 cells
q6_idx = None
q8_idx = None
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if 'Q6.' in src and 'ECommerceDB' in src:
        q6_idx = i
    if 'Q8.' in src and 'ProductName' in src and 'CategoryName' in src:
        q8_idx = i

print(f"Q6 at index: {q6_idx}")
print(f"Q8 at index: {q8_idx}")
print(f"Total cells: {len(nb['cells'])}")
if q6_idx is not None and q8_idx is not None:
    print(f"Gap between Q6 and Q8: {q8_idx - q6_idx - 1} cell(s)")
