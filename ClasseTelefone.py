import re

class Telefone:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto! Verifique a quantidade de dígitos inseridos.")


    def valida_telefone(self, telefone):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        retorno = re.findall(padrao, telefone)
        if retorno:
            return True
        else:
            return False