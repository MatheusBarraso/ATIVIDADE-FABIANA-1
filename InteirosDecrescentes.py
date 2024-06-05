valores = [int(input("Digite o primeiro valor: ")),
           int(input("Digite o segundo valor: ")),
           int(input("Digite o terceiro valor: "))]

valores.sort(reverse=True)
print("Valores em ordem decrescente:")
for valor in valores:
    print(valor)
