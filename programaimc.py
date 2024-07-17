#Programa IMC

altura = float(input("Digite a sua altura:  "))
peso = int(input("Digite o seu peso:  "))

imc = peso / (altura ** 2)

#print(f"O seu IMC é {imc}. ")
print(f"O seu IMC é {imc:.2f}")
if imc >25:
    print("Acima do peso ideal")

elif imc < 18:
    print("Abaixo do peso ideal")

else:
    print(" O seu peso está ok")