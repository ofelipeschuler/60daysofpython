import random
import string
# string fornece um conjunto de caracteres prontos como números, letras e símbolos.
# random fornece funções para gerar números aleatórios.
def gerador_de_senhas(tamanho):
  comprimento = tamanho
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''
  
  while len(senha) < comprimento:
    senha += random.choice(caracteres)
  
  print(f"Sua senha gerada é: {senha}")

gerador_de_senhas(30) 
  