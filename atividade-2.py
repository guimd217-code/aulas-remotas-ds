
numero_str = input("Digite um numero para ver a tabuada: ")
numero = int(numero_str)

print(f"--- Tabuada do {numero} ---")

for i in range(1, 11):
 
    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado}")