base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"Resultado: {resultado}")