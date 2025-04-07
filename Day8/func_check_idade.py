def pode_dirigir(idade):
  if idade >= 18:
    return True
  else:
    return False
  
print(pode_dirigir(21)) # True
print(pode_dirigir(17)) # False