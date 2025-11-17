from pathlib import Path
import json, csv 

# Diretório onde os arquivos serão armazenados
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def _load():
    if not DB_PATH.exists():
        return []
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8")) # Lê o conteúdo JSON
    except json.JSONDecodeError:

        return []

def _save(leads): #Salva a lista de leads no arquivo JSON
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def read_leads(): #Retorna toda a lista de leads armazenados
    return _load()

def create_lead(lead_dict): #Adiciona um novo lead ao banco de dados
    leads = _load()
    leads.append(lead_dict)
    _save(leads)


def export_csv(path=None):
    """Exporta os leads para CSV. Retorna o caminho do arquivo."""
    path = Path(path) if path else (DATA_DIR / "leads.csv")
    leads = _load()
    try: ## Define os campos que aparecerão no CSV
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["Tecnologia", "Automação", "Desenvolvimento", "Criatividade", "Categoria", "created"])
            w.writeheader()
            for row in leads: # Garante que a chave 'Categoria' exista em todos os registros
               row.setdefault("Categoria", "")
               w.writerow(row)
        return path
    except PermissionError:

        return None








