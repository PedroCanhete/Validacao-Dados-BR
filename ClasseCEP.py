import requests

class CEP:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido! Confira a quantidade de dígitos e tente novamente.")

    def cep_eh_valido(self, cep):
        if len(str(cep)) == 8:
            return True
        else:
            return False
        
    def formata_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def __str__(self):
        return self.formata_cep()
    
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return ("Cidade: {}, Bairro: {}, Rua: {}, CEP: {}, Estado: {}".format(
            dados['localidade'], 
            dados['bairro'], 
            dados['logradouro'], 
            dados['cep'], 
            dados['uf'])
        )