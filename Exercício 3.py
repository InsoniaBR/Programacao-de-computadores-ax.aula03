#3- Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.
ano = 365
mes = 30
idadeAnos = int(input("Digite sua idade em anos: "))
IdadeMeses = int(input("Digite os meses além dos anos: "))
Idadedias = (idadeAnos*ano)+(IdadeMeses*mes)
print("Sua idade em dias é: ", Idadedias, "dias")