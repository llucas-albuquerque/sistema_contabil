#gestaodeestoque
class Estoque:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            raise ValueError("Quantidade solicitada é maior que a quantidade em estoque.")
        self.quantidade -= quantidade

# Classe de gestão de estoque
class GestaoEstoque:
    def __init__(self):
        self.estoque = []

    def adicionar_item_estoque(self, item):
        self.estoque.append(item)

    def remover_item_estoque(self, nome_item):
        for item in self.estoque:
            if item.nome == nome_item:
                self.estoque.remove(item)

    def registrar_entrada_estoque(self, nome_item, quantidade, preco_unitario):
        for item in self.estoque:
            if item.nome == nome_item:
                item.adicionar_estoque(quantidade)
                item.preco_unitario = preco_unitario
                break
        else:
            item = Estoque(nome_item, quantidade, preco_unitario)
            self.adicionar_item_estoque(item)

    def registrar_saida_estoque(self, nome_item, quantidade):
        for item in self.estoque:
            if item.nome == nome_item:
                item.remover_estoque(quantidade)
                break
        else:
            raise ValueError("Item não encontrado no estoque.")

    def gerar_relatorio_inventario(self):
        for item in self.estoque:
            print(f"{item.nome}: {item.quantidade} x {item.preco_unitario} = {item.quantidade * item.preco_unitario}")

# Classe de contabilidade geral
class ContabilidadeGeral:
    def __init__(self):
        self.contas_a_pagar = []
        self.contas_a_receber = []
        self.transacoes = []

    def adicionar_conta_a_pagar(self, conta):
        self.contas_a_pagar.append(conta)

    def adicionar_conta_a_receber(self, conta):
        self.contas_a_receber.append(conta)

    def registrar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def gerar_relatorio_financeiro(self, periodo):
        # Gera relatório financeiro com base no período especificado
        pass

#Esse código cria três classes principais: Estoque, GestaoEstoque e ContabilidadeGeral. A classe Estoque é responsável por manter o nome, a quantidade e o preço unitário de cada item no estoque, bem como adicionar e remover itens do estoque. A classe GestaoEstoque permite adicionar e remover itens do estoque, registrar entradas e saídas de mercadorias e gerar um relatório de inventário. A classe ContabilidadeGeral é responsável por gerenciar contas a pagar, contas a receber e transações, além de relatórios financeiros.