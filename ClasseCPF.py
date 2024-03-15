from validate_docbr import CPF
class ValidadorCPF:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
            
        else:
            raise ValueError("Quantidade de caracteres incorreta. Confira e tente novamente")
        
    def formata_CPF(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata_CPF()
