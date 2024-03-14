class CPF:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido! Verifique se os 11 dígitos foram inseridos.")

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
        
    def formata_CPF(self):
        parte_um = self.cpf[0:3]
        parte_dois = self.cpf[3:6]
        parte_tres = self.cpf[6:9]
        parte_quatro = self.cpf[9:]
        return ("{}.{}.{}-{}".format(parte_um, parte_dois, parte_tres, parte_quatro))    

    def __str__(self):
        return self.formata_CPF()
    
