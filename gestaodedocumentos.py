#gestaodedocumentos
class GestaoDocumentos:
    def __init__(self):
        self.documentos = {}

    def adicionar_documento(self, tipo, numero, data, valor, descricao):
        self.documentos[numero] = {
            "tipo": tipo,
            "data": data,
            "valor": valor,
            "descricao": descricao
        }

    def remover_documento(self, numero):
        del self.documentos[numero]

    def buscar_documento(self, numero):
        return self.documentos.get(numero)

    def gerar_relatorio_documentos(self):
        print("Relatório de documentos:\n")
        for numero, dados in self.documentos.items():
            print(f"Documento: {numero}")
            print(f"Tipo: {dados['tipo']}")
            print(f"Data: {dados['data']}")
            print(f"Valor: R$ {dados['valor']:.2f}")
            print(f"Descrição: {dados['descricao']}")
            print("\n")

# Nessa classe, temos um dicionário chamado documentos que irá armazenar todas as informações dos documentos contábeis. A função adicionar_documento adiciona um novo documento ao dicionário com as informações fornecidas (tipo, número, data, valor e descrição). A função remover_documento remove um documento do dicionário com base no número fornecido. A função buscar_documento retorna as informações de um documento específico com base no número fornecido. A função gerar_relatorio_documentos gera um relatório com todos os documentos armazenados no dicionário.
# Você pode integrar essa classe ao seu sistema contábil e usá-la para gerenciar todos os documentos contábeis necessários, como notas fiscais, recibos, contratos, entre outros. Certifique-se de adaptar o código às necessidades específicas do seu projeto.