# Contabilidade Geral
class ContabilidadeGeral:
    def __init__(self):
        self.contas_a_pagar = {}
        self.contas_a_receber = {}
        self.balanco_patrimonial = {}
        self.demonstracao_resultados = {}
        
    def adicionar_conta_a_pagar(self, descricao, valor):
        self.contas_a_pagar[descricao] = valor
        
    def adicionar_conta_a_receber(self, descricao, valor):
        self.contas_a_receber[descricao] = valor
        
    def gerar_balanco_patrimonial(self):
        ativos = sum(self.balanco_patrimonial.get('ativos', {}).values())
        passivos = sum(self.balanco_patrimonial.get('passivos', {}).values())
        patrimonio_liquido = ativos - passivos
        self.balanco_patrimonial = {
            'ativos': {'total': ativos},
            'passivos': {'total': passivos},
            'patrimonio_liquido': patrimonio_liquido
        }
        
    def gerar_demonstracao_resultados(self):
        receitas = sum(self.demonstracao_resultados.get('receitas', {}).values())
        despesas = sum(self.demonstracao_resultados.get('despesas', {}).values())
        lucro_ou_prejuizo = receitas - despesas
        self.demonstracao_resultados = {
            'receitas': {'total': receitas},
            'despesas': {'total': despesas},
            'lucro_ou_prejuizo': lucro_ou_prejuizo
        }
        
    def gerar_relatorios_contabeis(self):
        self.gerar_balanco_patrimonial()
        self.gerar_demonstracao_resultados()
        # outros relatórios contábeis
        
    def imprimir_relatorios_contabeis(self):
        self.gerar_relatorios_contabeis()
        print('Relatório de Balanço Patrimonial:')
        print(self.balanco_patrimonial)
        print('Relatório de Demonstração de Resultados:')
        print(self.demonstracao_resultados)
        # imprimir outros relatórios contábeis

# Segunda forma de criar essa opção de Contabilidade Geral

class Conta:
    def __init__(self, nome, valor, data_vencimento, data_pagamento=None):
        self.nome = nome
        self.valor = valor
        self.data_vencimento = data_vencimento
        self.data_pagamento = data_pagamento
        self.status = 'Em aberto' if data_pagamento is None else 'Pago'

    def pagar(self, data_pagamento):
        self.data_pagamento = data_pagamento
        self.status = 'Pago'


class ContaPagar(Conta):
    def __init__(self, nome, valor, data_vencimento, data_pagamento=None):
        super().__init__(nome, valor, data_vencimento, data_pagamento)
        self.tipo = 'Pagar'


class ContaReceber(Conta):
    def __init__(self, nome, valor, data_vencimento, data_pagamento=None):
        super().__init__(nome, valor, data_vencimento, data_pagamento)
        self.tipo = 'Receber'


class BalancoPatrimonial:
    def __init__(self):
        self.ativos = []
        self.passivos = []

    def adicionar_ativo(self, nome, valor, data_aquisicao):
        self.ativos.append({'nome': nome, 'valor': valor, 'data_aquisicao': data_aquisicao})

    def adicionar_passivo(self, nome, valor, data_aquisicao):
        self.passivos.append({'nome': nome, 'valor': valor, 'data_aquisicao': data_aquisicao})

    def calcular_saldo(self):
        total_ativos = sum([ativo['valor'] for ativo in self.ativos])
        total_passivos = sum([passivo['valor'] for passivo in self.passivos])
        return total_ativos - total_passivos


class DemonstracaoResultados:
    def __init__(self):
        self.receitas = []
        self.despesas = []

    def adicionar_receita(self, nome, valor, data):
        self.receitas.append({'nome': nome, 'valor': valor, 'data': data})

    def adicionar_despesa(self, nome, valor, data):
        self.despesas.append({'nome': nome, 'valor': valor, 'data': data})

    def calcular_lucro(self):
        total_receitas = sum([receita['valor'] for receita in self.receitas])
        total_despesas = sum([despesa['valor'] for despesa in self.despesas])
        return total_receitas - total_despesas


class RelatorioContabil:
    def __init__(self):
        self.contas_pagar = []
        self.contas_receber = []

    def adicionar_conta_pagar(self, nome, valor, data_vencimento, data_pagamento=None):
        conta_pagar = ContaPagar(nome, valor, data_vencimento, data_pagamento)
        self.contas_pagar.append(conta_pagar)

    def adicionar_conta_receber(self, nome, valor, data_vencimento, data_pagamento=None):
        conta_receber = ContaReceber(nome, valor, data_vencimento, data_pagamento)
        self.contas_receber.append(conta_receber)

        def gerar_relatorio_contas_pagar(self):
        print('Contas a Pagar:')
        for conta in self.contas_pagar:
            print(f'{conta.nome} - R$ {conta.valor} - Vencimento: {conta.data_vencimento} - Status: {conta.status}')

    def gerar_relatorio_contas_receber(self):
        print('Contas a Receber:')
        for conta in self.contas_receber:
            print(f'{conta.nome} - R$ {conta.valor} - Vencimento: {conta.data_vencimento} - Status: {conta.status}')

    def gerar_relatorio_balanco_patrimonial(self):
        balanco = BalancoPatrimonial()
        for conta in self.contas_receber:
            balanco.adicionar_ativo(conta.nome, conta.valor, conta.data_vencimento)
        for conta in self.contas_pagar:
            balanco.adicionar_passivo(conta.nome, conta.valor, conta.data_vencimento)
        saldo = balanco.calcular_saldo()
        print(f'Balanço Patrimonial:\nAtivos: R$ {sum([ativo["valor"] for ativo in balanco.ativos])}\nPassivos: R$ {sum([passivo["valor"] for passivo in balanco.passivos])}\nSaldo: R$ {saldo}')

    def gerar_relatorio_demonstracao_resultados(self):
        dr = DemonstracaoResultados()
        for conta in self.contas_receber:
            dr.adicionar_receita(conta.nome, conta.valor, conta.data_vencimento)
        for conta in self.contas_pagar:
            dr.adicionar_despesa(conta.nome, conta.valor, conta.data_vencimento)
        lucro = dr.calcular_lucro()
        print(f'Demonstração de Resultados:\nReceitas: R$ {sum([receita["valor"] for receita in dr.receitas])}\nDespesas: R$ {sum([despesa["valor"] for despesa in dr.despesas])}\nLucro: R$ {lucro}')

# Exemplo de uso:
rc = RelatorioContabil()
rc.adicionar_conta_pagar('Fornecedor 1', 1500, '2023-03-31')
rc.adicionar_conta_pagar('Fornecedor 2', 2000, '2023-04-15')
rc.adicionar_conta_receber('Cliente 1', 3000, '2023-03-25')
rc.adicionar_conta_receber('Cliente 2', 4000, '2023-04-10')
rc.gerar_relatorio_contas_pagar()
rc.gerar_relatorio_contas_receber()
rc.gerar_relatorio_balanco_patrimonial()
rc.gerar_relatorio_demonstracao_resultados()

# Nesse exemplo, temos a classe Conta, que é a classe base para as classes ContaPagar e ContaReceber, que representam contas a pagar e contas a receber, respectivamente. A classe BalancoPatrimonial representa o balanço patrimonial, e a classe DemonstracaoResultados representa a demonstração de resultados. A classe RelatorioContabil é responsável por gerar os relatórios contábeis.

# No exemplo de uso, criamos algumas contas a pagar e contas a receber:

rc = RelatorioContabil()
rc.adicionar_conta_pagar('Fornecedor 1', 1500, '2023-03-31')
rc.adicionar_conta_pagar('Fornecedor 2', 2000, '2023-04-15')
rc.adicionar_conta_receber('Cliente 1', 3000, '2023-03-25')
rc.adicionar_conta_receber('Cliente 2', 4000, '2023-04-10')
rc.gerar_relatorio_contas_pagar()
rc.gerar_relatorio_contas_receber()
rc.gerar_relatorio_balanco_patrimonial()
rc.gerar_relatorio_demonstracao_resultados()

# Nesse exemplo, criamos uma instância da classe RelatorioContabil, adicionamos algumas contas a pagar e receber usando os métodos adicionar_conta_pagar e adicionar_conta_receber, e geramos os relatórios contábeis usando os métodos gerar_relatorio_contas_pagar, gerar_relatorio_contas_receber, gerar_relatorio_balanco_patrimonial e gerar_relatorio_demonstracao_resultados.

# Os relatórios são gerados no console e mostram as contas a pagar e a receber, o balanço patrimonial e a demonstração de resultados. É importante notar que este é apenas um exemplo simples e que um sistema contábil real seria muito mais complexo e teria muitas outras funcionalidades.
