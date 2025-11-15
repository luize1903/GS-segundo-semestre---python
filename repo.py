from pathlib import Path
import json, csv 

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def _load():
    if not DB_PATH.exists():
        return []
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:

        return []

def _save(leads):
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def read_leads():
    return _load()

def create_lead(lead_dict):
    leads = _load()
    leads.append(lead_dict)
    _save(leads)


def export_csv(path=None):
    """Exporta os leads para CSV. Retorna o caminho do arquivo."""
    path = Path(path) if path else (DATA_DIR / "leads.csv")
    leads = _load()
    try:
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["Tecnologia", "Automação", "Desenvolvimento", "Criatividade", "Categoria", "created"])
            w.writeheader()
            for row in leads:
               row.setdefault("Categoria", "")
               w.writerow(row)
        return path
    except PermissionError:

        return None








