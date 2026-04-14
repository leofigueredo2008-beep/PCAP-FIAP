Ano_nasc = int(input("Qual seu ano de nascimento: "))

Idade = 2026-Ano_nasc

if Idade<=15:
    print("Seu voto é proibido, espere mais para votar")
elif Idade>=16 and Idade<=17:
    print("Seu voto é opcional")
elif Idade>=18 and Idade<=69:
    print("Seu voto é obrigatório")
else:
    print("Seu voto é opcional")