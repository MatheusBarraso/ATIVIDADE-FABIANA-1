nomes = [input("Digite o nome da pessoa 1: "),
         input("Digite o nome da pessoa 2: "),
         input("Digite o nome da pessoa 3: ")]

print("Nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)