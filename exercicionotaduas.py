nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media < 4:
    print(f"Aluno reprovado")
elif media > 6:
    print(f"Aluno aprovado direto")
elif media >4 and media <6:
    print("Aluno em recuperação")
elif media>5:
    print(f"Reprovado na recuperação")
else:
    print(f"Aprovado na recuperação")