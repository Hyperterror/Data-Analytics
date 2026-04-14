import json, os
nb_path = r'd:\College\Programming\Data-Analytics\DA-AG-014_SQL_Advanced_Functions.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cell7 = nb['cells'][7]
print("Cell 7 full source:")
print(''.join(cell7.get('source', [])))
