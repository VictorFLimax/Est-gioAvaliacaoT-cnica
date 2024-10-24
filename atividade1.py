

def fibonacci(n):
    num1 = 0
    num2 = 1
    while num1 < n:
        temp = num1 + num2
        num1 = num2
        num2 = temp

    if num1 == n:
        return True
    else:
        return False

numero = int(input("Numero: "))

if fibonacci(numero):
    print(f"O número {numero} faz parte da sequência de Fibonacci.")
else:
    print(f"O número {numero} não faz parte da sequência de Fibonacci.")