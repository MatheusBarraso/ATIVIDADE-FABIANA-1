somaPares = 0
quantidadePares = 0
valor = int(input("Digite um número par (0 para sair): "))

while valor != 0:
    if valor % 2 == 0:
        somaPares += valor
        quantidadePares += 1
    valor = int(input("Digite outro número par (0 para sair): "))

if quantidadePares > 0:
    mediaPares = somaPares / quantidadePares
    print(f"Média dos números pares: {mediaPares}")
else:
    print("Nenhum número par foi digitado.")