# Folha de Pagamento
TAXA_INSS = 0.11
TAXA_IR = 0.275

# Define a classe Funcionario
class Funcionario:
    def __init__(self, nome, salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto

    def calcular_salario_liquido(self):
        # Calcula o valor do INSS
        inss = self.salario_bruto * TAXA_INSS

        # Calcula o valor do imposto de renda
        if self.salario_bruto <= 1903.98:
            ir = 0
        elif self.salario_bruto <= 2826.65:
            ir = (self.salario_bruto - 1903.98) * 0.075 - 142.80
        elif self.salario_bruto <= 3751.05:
            ir = (self.salario_bruto - 2826.65) * 0.15 - 354.80
        elif self.salario_bruto <= 4664.68:
            ir = (self.salario_bruto - 3751.05) * 0.225 - 636.13
        else:
            ir = (self.salario_bruto - 4664.68) * 0.275 - 869.36

        # Calcula o salário líquido
        salario_liquido = self.salario_bruto - inss - ir

        return salario_liquido

# Cria alguns funcionários
funcionario1 = Funcionario("João", 5000)
funcionario2 = Funcionario("Maria", 3000)

# Imprime os salários líquidos dos funcionários
print("Salário líquido do", funcionario1.nome, ": R$", funcionario1.calcular_salario_liquido())
print("Salário líquido da", funcionario2.nome, ": R$", funcionario2.calcular_salario_liquido())


# Observações
# Neste exemplo, criamos uma classe Funcionario com os atributos nome e salario_bruto. Também definimos as taxas de INSS e Imposto de Renda, e implementamos o método calcular_salario_liquido, que realiza os cálculos para obter o valor do INSS, imposto de renda e salário líquido do funcionário.
# No final, criamos dois funcionários e imprimimos os seus respectivos salários líquidos usando o método calcular_salario_liquido. Obviamente, este é apenas um exemplo básico e há muitas outras coisas que poderiam ser adicionadas a um sistema de folha de pagamento completo, como cálculo de férias, décimo terceiro, horas extras, entre outras coisas. 