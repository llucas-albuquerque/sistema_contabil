#gestãodeativos
class Ativo:
    def __init__(self, nome, data_compra, custo_original, vida_util, metodo_depreciacao, taxa_depreciacao):
        self.nome = nome
        self.data_compra = data_compra
        self.custo_original = custo_original
        self.vida_util = vida_util
        self.metodo_depreciacao = metodo_depreciacao
        self.taxa_depreciacao = taxa_depreciacao

    def calcular_depreciacao(self):
        if self.metodo_depreciacao == 'linear':
            return (self.custo_original - self.valor_residual) / self.vida_util * self.taxa_depreciacao
        elif self.metodo_depreciacao == 'acelerada':
            # Cálculo de depreciação acelerada
            pass

    def calcular_valor_contabil(self):
        # Cálculo do valor contábil
        pass

    def calcular_valor_mercado(self):
        # Cálculo do valor de mercado
        pass

# Classe de gestão de ativos
class GestaoAtivos:
    def __init__(self):
        self.ativos = []

    def adicionar_ativo(self, ativo):
        self.ativos.append(ativo)

    def editar_ativo(self, nome_ativo, novo_valor):
        for ativo in self.ativos:
            if ativo.nome == nome_ativo:
                ativo.novo_valor = novo_valor

    def excluir_ativo(self, nome_ativo):
        for ativo in self.ativos:
            if ativo.nome == nome_ativo:
                self.ativos.remove(ativo)

    def gerar_relatorio_valor_contabil(self):
        # Gera relatório de valor contábil
        pass

    def gerar_relatorio_valor_mercado(self):
        # Gera relatório de valor de mercado
        pass

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

# Esse código cria três classes principais: Ativo, GestaoAtivos e ContabilidadeGeral. A classe Ativo é responsável pelo cálculo da depreciação e dos valores contábil e de mercado. A classe GestaoAtivos permite adicionar, editar e excluir ativos, bem como gerar relatórios de valor contábil e valor de mercado. A classe ContabilidadeGeral é responsável por gerenciar contas a pagar, contas a receber, transações, e relatórios financeiros.





