#gestaodecobrança
import datetime


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.divida = 0
        self.pagamentos = []

    def adicionar_pagamento(self, valor, data):
        self.pagamentos.append((valor, data))
        self.divida -= valor

    def enviar_email_cobranca(self):
        if self.divida > 0:
            mensagem = f"Prezado(a) {self.nome},\n\nVocê tem uma dívida pendente conosco no valor de R${self.divida:.2f}. Por favor, faça o pagamento o mais breve possível.\n\nAtenciosamente,\nEquipe de cobrança"
            # Aqui seria o código para enviar o e-mail

    def enviar_sms_cobranca(self):
        if self.divida > 0:
            mensagem = f"Prezado(a) {self.nome}, você tem uma dívida pendente conosco no valor de R${self.divida:.2f}. Por favor, faça o pagamento o mais breve possível."
            # Aqui seria o código para enviar o SMS


class SistemaContabil:
    def __init__(self):
        self.clientes = []

    def criar_cliente(self, nome, email, telefone):
        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        return cliente

    def verificar_pagamentos(self):
        for cliente in self.clientes:
            if cliente.divida > 0:
                for valor, data in cliente.pagamentos:
                    if data < datetime.date.today():
                        cliente.divida += valor

                        # Enviar cobrança por e-mail
                        cliente.enviar_email_cobranca()

                        # Enviar cobrança por SMS
                        cliente.enviar_sms_cobranca()

# Este sistema contábil permite a criação de clientes com nome, e-mail e telefone. É possível adicionar pagamentos dos clientes, que são armazenados em uma lista de pagamentos e subtraídos do valor da dívida. O sistema também verifica se há pagamentos pendentes e, se houver, envia uma cobrança por e-mail e/ou SMS.

# Para usar o sistema, você pode criar uma instância da classe SistemaContabil e criar clientes através do método criar_cliente(). Por exemplo:
sistema_contabil = SistemaContabil()

cliente_1 = sistema_contabil.criar_cliente(
    "João Silva", "joao.silva@email.com", "9999-9999"
)
cliente_1.divida = 10000
cliente_1.adicionar_pagamento(5000, datetime.date(2023, 3, 20))
cliente_1.adicionar_pagamento(4000, datetime.date(2023, 3, 21))

sistema_contabil.verificar_pagamentos()

# Este código cria um novo cliente chamado "João Silva" com um e-mail e telefone. Em seguida, define uma dívida pendente de 10000 e adiciona dois pagamentos: um de 5000 com a data de 20/03/2023 e outro de 4000 com a data de 21/03/2023. Por fim, o sistema verifica se há pagamentos pendentes e envia uma cobrança por e-mail e/ou SMS para o cliente, caso existam pagamentos em atraso. No exemplo acima, como todos os pagamentos foram feitos antes da data de hoje (21/03/2023), o sistema não enviará nenhuma cobrança.
# É importante lembrar que este é apenas um exemplo básico e que existem muitas outras funcionalidades que um sistema contábil com opção de gestão de cobrança pode ter, dependendo das necessidades específicas do seu escritório. Além disso, é necessário implementar outros recursos, como persistência de dados e autenticação de usuários, para garantir a segurança e a confiabilidade do sistema.
