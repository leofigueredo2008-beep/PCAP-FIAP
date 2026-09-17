from pathlib import Path 
import json, csv

data_dir = Path(__file__).resolve().parent / "data"

DB_PATH = data_dir / "leads.json"

#crud
#create - read - update - delete

#read
def read_leads():
    if not DB_PATH.exists():
        return []
    
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    
#create
def create_lead(lead_dict):
    leads = read_leads() #lista de dicionarios de leads
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")



# EXPORT LEADS COMO CSV

def export_csv():
    path_csv = data_dir / "leads.csv"

    leads = read_leads() #LISTA - ARRAY

    try: 
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames = leads[0].keys())
            writer.writeheader()
            for row in leads :
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None

#READ LEAD FROM QUERY
def read_leads_search(query):
    leads = read_leads()
    result = []


    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]} {lead["company"]}".lower()

        if query.lower() in txt_lead:
            result.append((i,lead)) 

    return result
