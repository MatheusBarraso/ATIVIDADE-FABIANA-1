i = 0
x = 1
numerosNegativos = 0
numerosPositivos = 0

for i in range(1, 21):
    numero = int(input("Digite  o {}° número: ".format(x)))
    i += 1
    x += 1

    if numero < 0:
        numerosNegativos += 1
    else:
        numerosPositivos += 1 

somaPositivos = numerosPositivos * numerosPositivos 

print(" ")
print("A quantidade de números negativos é de: {}".format(numerosNegativos))
print("A soma dos números positivos é de: {}".format(somaPositivos))