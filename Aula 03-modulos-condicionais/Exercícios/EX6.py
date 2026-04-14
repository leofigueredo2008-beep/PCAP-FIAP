
NUM_1 = int(input("Digite seu primeiro número: "))
NUM_2 = int(input("Digite seu segundo número: "))
OPERACAO = input("Digite a operação a ser realizada (apenas o sinal): ")

if OPERACAO == "+":
    print(f"A soma dos números é {NUM_1+NUM_2}")
elif OPERACAO == "-":
    print(f"A subtração dos números é {NUM_1-NUM_2}")
elif OPERACAO == "*":
    print(f"A multiplicação dos números é {NUM_1*NUM_2}")
elif OPERACAO == "/":
    print(f"A divisão dos números é {NUM_1/NUM_2}")
else:
    print("Essa é uma calculadora simples, não invente moda")