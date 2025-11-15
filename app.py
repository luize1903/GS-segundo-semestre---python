from stages import model_lead
import repo


def perguntar_sn(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in ["sim", "s"]:
            return "sim"
        elif resposta in ["não", "nao", "n"]:
            return "não"
        else:
            print(" Responda apenas com 'sim' ou 'não'.")

def add_leads():
    tecnologia = perguntar_sn("Interesse em tecnologia: ").strip()
    automacao = perguntar_sn("Prática em automação: ").strip()
    desenvolvimento = perguntar_sn("Facilidade no desenvolvemento: ").strip()
    criatividade = perguntar_sn("Alta criatividade: ").strip()
    respostas = [tecnologia, automacao, desenvolvimento, criatividade]
    pontuacao = respostas.count("sim")

    if pontuacao >= 3:
        categoria = "Profissões voltadas a Inteligência artificial"
    elif pontuacao >= 1:
        categoria = "Design Gráfico"
    else:
        categoria = "Outras áreas, exemplo humanas"

    print(f"\n Classificação: {categoria}")

    repo.create_lead(model_lead(tecnologia, automacao, desenvolvimento, criatividade, categoria))

    print("✔ Lead adicionado!")


def list_leads():
    leads = repo.read_leads()
    if not leads:
        print("Nenhum lead ainda.")
        return
    print("\n# | Interesse em tecnologia   | Prática com automação   | Facilidade no desenvolvimento   |Alta Criatividade   |Categoria  ")
    print("--+----------------------+-------------------+-------------------------------------------------------------------")
    for i, l in enumerate(leads):
        print(f"{i:02d}| {l['Tecnologia']:<20} | {l['Automação']:<17} | {l['Desenvolvimento']:<21} |{l['Criatividade']:<21}|{l['Categoria']:<21}")


def search_flow():
    q = input("Buscar por: ").strip().lower()
    if not q:
        print("Consulta vazia.")
        return
    leads = repo.read_leads()
    results = []
    for i, l in enumerate(leads):
        blob = f"{l['Tecnologia']} {l['Automação']} {l['Desenvolvimento']}{l['Criatividade']}{l['Categoria']}".lower()
        if q in blob:
            results.append((i, l))
    if not results:
        print("Nada encontrado.")
        return
    print("\n# | Interesse em tecnologia   | Prática com automação   | Facilidade no desenvolvimento   |Alta Criatividade   |Categoria  ")
    print("--+----------------------+-------------------+-----------------------")
    for i, l in results:
        print(f"{i:02d}| {l['Tecnologia']:<20} | {l['Automação']:<17} | {l['Desenvolvimento']:<21} |{l['Criatividade']:<21}|{l['Categoria']:<21}")


# criar vazio e dps exportar da função

def export_leads():
    path = repo.export_csv()
    if path is None:
        print("Não consegui escrever o CSV. Feche o arquivo se estiver aberto e tente novamente.")
    else:
        print(f"✔ Exportado para: {path}")


# criar search_flow primeiro, dps export_leads

def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            add_leads()
        elif op == "2":
            list_leads()
        elif op == "4":
            export_leads()      
        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")




def print_menu():
    print("\nIdentificador de profisões futuras")
    print("[1] Adicionar habilidades")
    print("[2] Listar habilidades")
    print("[4] Exportar CSV")
    print("[0] Sair")


if __name__ == "__main__":
    main()





