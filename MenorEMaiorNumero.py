valor = int(input("Digite um valor inteiro (0 para sair): "))

if valor != 0:
    maior = menor = valor 
else:
    maior = menor = 0

while valor != 0:
    valor = int(input("Digite outro valor inteiro (0 para sair): "))
    if valor != 0:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")