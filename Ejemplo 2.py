# Paradigma funcional:

numeros = [1, 2, 3, 4, 5, 6]


pares = list(filter(lambda x: x % 2 == 0, numeros))


resultado = list(map(lambda x: x * 2, pares))

print("Números originales:", numeros)
print("Números pares:", pares)
print("Resultado final:", resultado)