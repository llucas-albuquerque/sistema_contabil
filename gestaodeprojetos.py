#gestaodeprojetos 
class Projeto:
    def __init__(self, nome, data_inicio, data_fim, descricao):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao
        self.orcamento = 0
        self.custo_total = 0
        self.recursos = []

    def definir_orcamento(self, orcamento):
        self.orcamento = orcamento

    def adicionar_recurso(self, recurso):
        self.recursos.append(recurso)

    def calcular_custo_total(self):
        for recurso in self.recursos:
            self.custo_total += recurso.custo

    def relatorio(self):
        print(f"Projeto: {self.nome}")
        print(f"Data de Início: {self.data_inicio}")
        print(f"Data de Fim: {self.data_fim}")
        print(f"Descrição: {self.descricao}")
        print(f"Orçamento: {self.orcamento}")
        print(f"Custo Total: {self.custo_total}")
        print("Recursos:")
        for recurso in self.recursos:
            print(f"\t{recurso.nome} - Custo: {recurso.custo}")


class Recurso:
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo


class SistemaContabil:
    def __init__(self):
        self.projetos = []

    def criar_projeto(self, nome, data_inicio, data_fim, descricao):
        projeto = Projeto(nome, data_inicio, data_fim, descricao)
        self.projetos.append(projeto)
        return projeto

    def relatorio_projetos(self):
        for projeto in self.projetos:
            projeto.calcular_custo_total()
            projeto.relatorio()

# Este sistema contábil permite a criação de projetos com nome, data de início, data de término, descrição e definição de um orçamento. Também é possível adicionar recursos ao projeto e calcular o custo total do projeto. O relatório do projeto mostra informações como nome, datas, descrição, orçamento, custo total e recursos utilizados.
# Para usar o sistema, você pode criar uma instância da classe SistemaContabil e criar projetos através do método criar_projeto(). Por exemplo:

sistema_contabil = SistemaContabil()

projeto_1 = sistema_contabil.criar_projeto(
    "Projeto 1", "01/01/2023", "31/12/2023", "Descrição do Projeto 1"
)
projeto_1.definir_orcamento(10000)

recurso_1 = Recurso("Recurso 1", 5000)
projeto_1.adicionar_recurso(recurso_1)

sistema_contabil.relatorio_projetos()

# Este código cria um novo projeto chamado "Projeto 1" com data de início em 01/01/2023, data de término em 31/12/2023 e uma descrição. Em seguida, define um orçamento de 10000 e adiciona um recurso chamado "Recurso 1" com custo de 5000. Por fim, o relatório do projeto é gerado.

