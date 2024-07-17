
celsius = int(input("Digite a temperatura:  "))
print("Digite a conversão da temperatura desejada")
#temperatura = int(input("1.Celsius/ 2.Kelvin/ 3. Fahrenheit"))
print("1-Converter de C para F")
print("2- Converter de C para K")
print("3- Converter de K para C")
print("4- Converter de k para F")
print("5- Converter de F para C")
print("6-Converter de F para K" )
estado = int(input())

match estado:
        case 1:
            Fahrenheit = (9/5 * celsius) -32
            print(f"A conversão de C para F é: {Fahrenheit:.2f} ")
        case 2:
            kelvin = celsius + 273
            print(f"A conversão de C para F é: {kelvin:.2f}")
        case 3:
             kelvin = celsius - 273
             print(f"A conversão de K para C é: {kelvin:.2f}")
        case 4:
            fahrenheit = celsius * 9/5 +32
            print(f"A temperatura em k convertida em F é:  {fahrenheit:.2f} ")
        case 5:
            fahrenheit = (celsius - 32) /1.8
            print(f"A conversao de temperatura em F para C é:  {fahrenheit:.2f}")
        case 6:
             kelvin = (celsius - 32) * 5/9 +  273.15
             print("A temperatura em k convertida em F é:    ", kelvin)
        case _:
          print("OPERAÇÃO INVÁLIDA:")

