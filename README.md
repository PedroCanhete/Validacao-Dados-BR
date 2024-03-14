# Validacao-Dados-BR
 Validador de dados no modelo brasileiro: CPF, CNPJ, Data, Hora e Telefone 

 Neste validador iremos verificar se a informação inserida está no padrão brasileiro ou não.
 
 __*CPF*__ -> Deve conter 11 dígitos e no modelo máscara 999.999.999-99

 __*CNPJ*__ -> Deve conter 14 dígitos e no modelo máscara 99.999.999/9999-99

__*Telefone*__ -> Deve conter 10 a 11 dígitos (incluindo código de área) e no modelo máscara (99)9 9999-9999

__*Data*__ -> Deve salvar o momento de algum cadastro e retornar no formato PT-BR (dd/mm/aaaa). Funcionalidade extra informando há quanto tempo o usuário está cadastrado.

__*CEP*__ -> Deve conter 8 dígitos e no modelo máscara 99999-999. Além disso, irá acessar WebService ViaCEP e retornar o endereço.

