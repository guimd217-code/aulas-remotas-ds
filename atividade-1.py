
nome = input("Qual e o seu nome? ")

idade_texto = input("Qual e a sua idade? ")

idade_numero = int(idade_texto)

if idade_numero >= 18:

    print(f"Ola, {nome}, voce e maior de idade.")
else:
    print(f"Ola, {nome}, voce e menor de idade.")