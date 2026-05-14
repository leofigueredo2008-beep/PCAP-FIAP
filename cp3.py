temperatura = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
SALAS = 0
lista_criticos = []



for sala in range(len(temperatura)):
    SOMA = 0
    SALAS += 1
    critico = 0
    for temp in range(len(temperatura[sala])):
        SOMA += temperatura[sala][temp]
        if temperatura[sala][temp]>= 33:
            critico += 1
    lista_criticos.append(critico)
    print("Sala", SALAS)
    print(temperatura[sala])
    print("Media: ", SOMA/len(temperatura[sala]))
    print("Registros criticos:",critico)

print(f"A sala com maior numeros de criticos e a {lista_criticos.index(max(lista_criticos))+1}")



