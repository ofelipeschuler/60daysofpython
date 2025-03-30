frutas = ["banana", "maçã", "uva", "pera", "manga"]

for fruta in frutas:
  print(fruta)
 
 # utilizando input para criar a lista de frutas
 
frutasv2 = []
 
while True:
  fruta = input("Digite o nome da fruta  : ")
  if fruta == "sair":
    break
  frutasv2.append(fruta)
  
print (frutasv2)