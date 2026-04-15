Sal=float(input("Digite seu salário: "))

if Sal<=280.0:
    X=Sal*0.2
    Sal_Novo=Sal+X
    print(f"Seu salário era de: {Sal:.2f}")
    print(f"Seu salário vai ser aumentado em 20%")
    print(f"{X:.2f} reais vai ser adicionado no seu salário")
    print(f"Seu novo salário é de {Sal_Novo:.2f} reais")

elif Sal>280.0 and Sal<700.0:
    X_2=Sal*0.15
    Sal_Novo_2=Sal+X_2
    print(f"Seu salário era de: {Sal:.2f}")
    print(f"Seu salário vai ser aumentado em 15%")
    print(f"{X_2:.2f} reais vai ser adicionado no seu salário")
    print(f"Seu novo salário é de {Sal_Novo_2:.2f} reais")

elif Sal>=700.0 and Sal<1500.00:
    X_3=Sal*0.10
    Sal_Novo_3=Sal+X_3
    print(f"Seu salário era de: {Sal:.2f}")
    print(f"Seu salário vai ser aumentado em 10%")
    print(f"{X_3:.2f} reais vai ser adicionado no seu salário")
    print(f"Seu novo salário é de {Sal_Novo_3:.2f} reais")

else:
    X_4=Sal*0.05
    Sal_Novo_4=Sal+X_4
    print(f"Seu salário era de: {Sal:.2f}")
    print(f"Seu salário vai ser aumentado em 5%")
    print(f"{X_4:.2f} reais vai ser adicionado no seu salário")
    print(f"Seu novo salário é de {Sal_Novo_4:.2f} reais")


