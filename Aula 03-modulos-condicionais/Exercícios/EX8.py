Sal=float(input("Digite seu salário: "))

if Sal<=280.0:
    X=Sal*0.2
    Sal_Novo=Sal+X
    print(f"Seu salário era de: {Sal:.2f}")
    print(f"Seu salário vai ser aumentado em 20%")
    print(f"{X:.2f} reais vai ser adicionado no seu salário")
    print(f"Seu novo salário é de {Sal_Novo:.2f} reais")