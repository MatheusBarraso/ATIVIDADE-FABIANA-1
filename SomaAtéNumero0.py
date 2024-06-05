soma = 0
valor = float(input("Digite um número (digite 0 para encerrar): "))

while valor != 0:
    soma += valor
    valor = float(input("Digite outro número (digite 0 para encerrar): "))

print(f"Soma dos números digitados: {soma}")