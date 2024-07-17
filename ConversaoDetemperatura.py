#Conversão de temperatura

print()
print("Programa para converter temperatura")
print()

temp_c = float(input("Digite a temperatura a temperatura  ")) 
#temp_f = float(input("Digite a temperatura em Fahrenheit"))

#Conversao de temperatura Celsius para F
temp_f = temp_c * 9/5 + 32
print("A temperatura em C convertida em F  ",temp_f)

#Conversao de temperatura Celsius para K
temp_k = temp_c + 273.15
print("A temperatura em C convertida em K  ",temp_k)
print()

#----------------------------------------------------------------

#Conversao de temperatura K para Celsius
temp_k = temp_c - 273.15
print("A temperatura em k convertida em C  ",temp_k)

#Convesao de temperatura K par F
conversao_f = temp_k * 9/5 +32
print("A temperatura em k convertida em F  ",conversao_f)

#-----------------------------------------------------------------


#Conversao de temperatura F para Celsius
temp_f = (temp_c - 32) /1.8
print("A temperatura em F convertida em C  ",temp_f)

#Convesao de temperatura F par K
temp_k = (temp_c - 32) * 5/9 +  273.15
print("A temperatura em k convertida em F  ", temp_k)

