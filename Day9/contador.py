# Contador que para quando atingit um limite definido pelo usuário.
def contador_personalizado():
  try:
    limite = int(input("Digite o valor máximo do contador: "))
    # function range cria uma lista de números de 0 até o valor definido pelo usuário.
    limite = limite +1
    for i in range(limite):
      print(i)
      if i == limite:
        print("Contador finalizado.")
        break
  except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
    
contador_personalizado()