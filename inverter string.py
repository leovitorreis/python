def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
