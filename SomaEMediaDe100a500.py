soma = 0
quantidade = 0

for numero in range(101, 500, 2):
    soma += numero
    quantidade += 1

media = soma / quantidade
print(f"Soma dos ímpares: {soma}")
print(f"Média dos ímpares: {media}")
