def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisao por zero!"
    else:
        return "Operacao invalida!"

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
op = input("Digite a operacao (+, -, *, /): ")

resultado = calculadora(n1, n2, op)
print("Resultado:", resultado)