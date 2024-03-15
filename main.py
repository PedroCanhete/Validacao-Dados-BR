from ClassesCPF_CNPJ import Documento


###### Testes de utilização das classes
cpf_teste = "01234567890" #CPF correto
documento = Documento.cria_documento(cpf_teste)
print(documento)

cnpj_teste = "17977236000185" #CNPJ correto
documento_cnpj = Documento.cria_documento(cnpj_teste)
print(documento_cnpj)


cpf_teste2 = "00100200345" #CPF inválido
documento2 = Documento.cria_documento(cpf_teste2)

cnpj_teste2 = "001530410001781" #CNPJ com caracteres a mais
documento_cnpj2 = Documento.cria_documento(cnpj_teste2)
print(documento_cnpj2)