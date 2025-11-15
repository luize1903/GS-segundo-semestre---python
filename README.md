# GS-segundo-semestre---python
Um programa que gera recomendações personalizadas indicando carreiras, se o usuário tiver mais de três caracteristicas, ele pode seguir profissões voltadas a Inteligência artificial, se tiver dois a um desing gráfico e se não tiver nenhum outras áreas, exemplo humanas

Com base nas respostas, o sistema:
Classifica o usuário em uma categoria profissional (IA, Design Gráfico ou Outras Áreas);
Salva todas as respostas em um banco de dados local (JSON);
Permite listar todos os registros já cadastrados;
Possui sistema de busca;
Exporta os dados para um arquivo CSV

Propósito
O objetivo é criar uma ferramenta simples, intuitiva e útil que ajude estudantes e candidatos a identificar áreas profissionais.

Instruções de execução
1. Execute o programa principal:
python app.py

2.No menu, escolha uma das opções:

[1] Adicionar habilidades
[2] Listar habilidades
[4] Exportar CSV
[0] Sair

Descrição dos arquivos:
---app.py---

Gerencia o menu
Recebe entradas do usuário
Classifica a profissão
Envia os dados para salvar no repositório
Lista, pesquisa e exporta

---stages.py---

Contém a função:

def model_lead(tecnologia, automacao, desenvolvimento, criatividade, categoria):

Ela organiza os dados em formato de dicionário para serem salvos no JSON.

---repo.py---

Responsável por:
Criar o diretório data/
Salvar os dados como JSON
Ler os dados salvos
Exportar todos os registros para CSV
