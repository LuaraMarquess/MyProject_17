#Demonstração de operadores lógicos em condicionais...

print("O que você vai fazer amanhã de manhã?")
print("dormir/estudar/planejar")
manha = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar/treinar/trabalhar")
tarde = input()

if not manha or not tarde:
    print("você precisa dizer o que vai fazer!")
else:
    if manha == "dormir" or tarde == "jogar":
       print("você está despediçando o seu dia!")
    elif manha =="estudar" or tarde=="treinar":
        print("Que bom! Você ira se apefeiçoar!")
    elif manha =="planejar" and tarde =="trabalhar":
        print("Para trabalhar melhor,devo planejar!")
    else:
        print("Não combinamos estas ações")
print("Tenha um bom dia!")  