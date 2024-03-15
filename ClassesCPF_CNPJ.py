from validate_docbr import CPF, CNPJ
class ValidadorCPF_CNPJ:
    def __init__(self, documento):
        if len(str(documento)) == 11:
            documento = str(documento)
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
            
        elif len(str(documento)) == 14:
            documento = str(documento)
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido")
            
        else:
            raise ValueError("Documento inválido")
            

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de caracteres incorreta. Confira e tente novamente")
        

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de caracteres incorreta. Confira e tente novamente")



        
    def formata_CPF(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def formata_CNPJ(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formata_CPF()
    
    def __str__(self):
        return self.formata_CNPJ()

