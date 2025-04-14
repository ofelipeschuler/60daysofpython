# Lista ordenada a partir do método sorted.

#1 Lista Numérica
lista_num = [55, 51, 64, 90, 24, 34, 64, 62, 44, 12, 1, 7]

# sorted() é uma função embutida que ordena os elementos de uma lista.
# Ela retorna uma nova lista com os elementos ordenados, sem modificar a lista original.
numeros_ordenados = sorted(lista_num)
numeros_ordenados_2 = sorted(lista_num, reverse=True)

print(numeros_ordenados)

print(numeros_ordenados_2)