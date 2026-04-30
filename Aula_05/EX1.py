Var_nomes = ["Ana", "José", "João", "Enzo"]

for v in range(len(Var_nomes)):
    for i in range (v+1,len(Var_nomes)):
        print(Var_nomes[v], Var_nomes[i])

print("")

for v in range(len(Var_nomes)):
    for i in range (v, len(Var_nomes)):
        if v != i:
            print(Var_nomes[v], Var_nomes[i])