import json
import os

BASE = r'd:\College\Programming\Data-Analytics'

checks = {
    'DA-AG-014_SQL_Advanced_Functions.ipynb': {
        'expected_q': 'Q7',
        'check_text': 'TotalOrders'
    },
    'DA-AG-014_Tableau_Data_Visualization.ipynb': {
        'expected_q': 'Q1',
        'check_text': 'Business Intelligence'
    },
    'Python_OOPs_Assignment.ipynb': {
        'expected_q': 'Theory',
        'check_text': 'Method Resolution Order'
    },
    'Files_Exception_Handling_Assignment.ipynb': {
        'expected_q': 'Theory',
        'check_text': 'reference counting'
    },
    'Data_Toolkit_Assignment.ipynb': {
        'expected_q': 'Theory',
        'check_text': 'pairplot'
    },
}

all_ok = True
for fname, check in checks.items():
    path = os.path.join(BASE, fname)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        all_text = ' '.join(''.join(c.get('source', [])) for c in nb['cells'])
        found = check['check_text'] in all_text
        cell_count = len(nb['cells'])
        print(f"[{'OK' if found else 'FAIL'}] {fname} ({cell_count} cells) — '{check['check_text']}': {found}")
        if not found:
            all_ok = False
    except Exception as e:
        print(f"[ERROR] {fname}: {e}")
        all_ok = False

print()
print("All checks passed!" if all_ok else "Some checks FAILED — review above.")
