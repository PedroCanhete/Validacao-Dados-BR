from Clas
from validate_docbr import CNPJ

cpf = ValidadorCPF("48362871890")
print(cpf)


cnpj = CNPJ()
bf = '50341659000160'
print(cnpj.validate(bf))