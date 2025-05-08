def busca_linear(lista, numero_procurado):
    """
    Procurar um número dentro de uma lista, utilizando busca linear
    :param lista: lista de números
    :param numero_procurado: número a ser procurado na lista
    """
    for i, numero in enumerate(lista): #função ativa do python enumerate
    #enumerate passa por cada item dentro de uma lista enquanto contabiliza
        if numero == numero_procurado:
            return i
    return -1 #se não encontrar o número, retorna -1
  
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_procurado = 12

buscando_o_numero = busca_linear(lista, numero_procurado)
print(buscando_o_numero)

if buscando_o_numero != -1:
    print(f"Encontrei o número {numero_procurado} na posição {buscando_o_numero}")
else:
    print(f"Não encontrei o número {numero_procurado} na lista")