from datetime import date

from datetime import date

def model_lead(tecnologia, automacao, desenvolvimento, criatividade, categoria):
    return {
        "Tecnologia": tecnologia,
        "Automação": automacao,
        "Desenvolvimento": desenvolvimento,
        "Criatividade": criatividade,
        "Categoria": categoria,
        "created": date.today().isoformat(),
    }








