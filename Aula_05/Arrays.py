lista_frutas = ["banana", "Maçã", "Pera"]

print(lista_frutas)

lista_frutas.append("morango")
print(lista_frutas)

qtd = len(lista_frutas)
print(qtd)



for i in range(qtd):
    print(lista_frutas[i])


for fruta in lista_frutas:
    print(fruta)