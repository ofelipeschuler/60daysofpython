def pode_dirigir(idade):
  if idade >= 18:
    return True
  else:
    return False
  
try:
  input_user = int(input("Digite a sua idade: "))
  print(pode_dirigir(input_user)) # True
except ValueError:
  print("Entrada inválida. Por favor, insira um número inteiro.")