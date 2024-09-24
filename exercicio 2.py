def fibonacci_sequence(n):
    fib_sequence =[0, 1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def is_fibonnacci_number(num):
    fib_sequence = fibonacci_sequence(num)
    if num in fib_sequence:
        return f"O número {num} não pertence à sequência de Fibonacci."
    else:
        return f"O número {num} pertence à sequência de Fibonacci."
    
numero = int(input("Informe um número: "))
resultado = is_fibonnacci_number(numero)
print(resultado)