#contabilidadefiscal
class ContabilidadeFiscal:
    def __init__(self, nome_empresa, cnpj, regime_tributario):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.regime_tributario = regime_tributario
        self.impostos = []
        
    def calcular_imposto(self, valor_faturamento):
        if self.regime_tributario == "Simples Nacional":
            aliquota = self._aliquota_simples_nacional(valor_faturamento)
        elif self.regime_tributario == "Lucro Presumido":
            aliquota = self._aliquota_lucro_presumido(valor_faturamento)
        elif self.regime_tributario == "Lucro Real":
            aliquota = self._aliquota_lucro_real(valor_faturamento)
        else:
            raise ValueError("Regime tributário inválido")
        
        valor_imposto = valor_faturamento * aliquota
        self.impostos.append(valor_imposto)
        
        return valor_imposto
    
    def _aliquota_simples_nacional(self, valor_faturamento):
        if valor_faturamento <= 180000:
            return 0.04
        elif valor_faturamento <= 360000:
            return 0.06
        elif valor_faturamento <= 720000:
            return 0.11
        elif valor_faturamento <= 1800000:
            return 0.16
        elif valor_faturamento <= 3600000:
            return 0.21
        elif valor_faturamento <= 4800000:
            return 0.33
        else:
            return 0.33
    
    def _aliquota_lucro_presumido(self, valor_faturamento):
        if valor_faturamento <= 4800000:
            return 0.04
        else:
            return 0.0625
        
    def _aliquota_lucro_real(self, valor_faturamento):
        # implementação da lógica de cálculo da alíquota para Lucro Real
        pass
    
    def emitir_guia_imposto(self, valor_imposto):
        # implementação da lógica para emissão da guia de imposto
        pass
    
    def apurar_imposto(self):
        # implementação da lógica para apuração do imposto
        pass
    
    def gerar_SPED_fiscal(self):
        # implementação da lógica para geração do SPED Fiscal
        pass
    
    def gerar_ECF(self):
        # implementação da lógica para geração do ECF
        pass
 
 # Nessa implementação, criamos uma classe ContabilidadeFiscal que recebe o nome da empresa, o CNPJ e o regime tributário como parâmetros no construtor. Em seguida, implementamos um método calcular_imposto que recebe o valor de faturamento e calcula o valor de imposto de acordo com o regime tributário. O resultado é adicionado à lista de impostos da empresa.
 # Também temos métodos para emitir guias de imposto, apurar o imposto, gerar o SPED fiscal e gerar o ECF. Esses métodos ainda não foram implementados, mas devem ser completados de acordo com as necessidades específicas do sistema contábil.