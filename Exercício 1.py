#Faça um programa em Python que calcule e mostre o valor do volume do tronco deuma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura dotronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) ecalcular a seguinte expressão:volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("Olá ser humano, para calcular o volume do tronco de uma pirâmide, siga as instruções a seguir!")
H = float(input("Insira a altura do tronco da pirâmide (Em metros): "))
Bmenor = float(input("Insira o valor da base menor (Em metros): "))
Bmaior = float(input("Agora insira o valor da base maior (Em metros): "))
volume = (H/3)*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
print("O volume do tronco dessa pirâmide é: ", volume, "metros" ) 