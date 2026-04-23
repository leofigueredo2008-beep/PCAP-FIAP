nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("A nota deve estar entre 0 e 10")
    nota1 = float(input("Digite novamente a primeira nota: "))


nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("A nota deve estar entre 0 e 10")
    nota2 = float(input("Digite novamente a segunda nota: "))


media = (nota1 + nota2) / 2
print(f"A media é {media}")