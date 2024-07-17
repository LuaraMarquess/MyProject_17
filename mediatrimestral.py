#Programa nota trimestral

nota1 = float (input("Digite o valor da primeira nota: "))
nota2 = float (input("Digite o valor da segunda nota: "))
nota3 = float (input("Digite o valor da terceira nota: "))
nota4 = float (input("Digite o valor da quarta nota:  "))
media = (nota1 + nota2 + nota3 + nota4)/4

if media>=6 :
    print(f"Aluno Aprovado por média = {media}")
else:
    print(f"Aluno reprovado por média  =  {media}")


#print(type(media)) Retorna o tipo da média