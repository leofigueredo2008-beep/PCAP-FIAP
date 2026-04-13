nota_1 = float(input("digite a primeira nota do aluno: "))
nota_2 = float(input("digite a segunda nota do aluno: "))
nota_3 = float(input("digite a terceira nota do aluno: "))
nota_4 = float(input("digite a quarta nota do aluno: "))

Media=(nota_1+nota_2+nota_3+nota_4)/4
print(f"A média do aluno(a) é {Media}")

if Media>=7:
    print("Aprovado")
elif Media>=5:
    print("Recuperação")
else:
    print("Reprovado")