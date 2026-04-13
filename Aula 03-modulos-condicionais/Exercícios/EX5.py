A = int(input("Digite um valor: "))
B = int(input("Digite um valor: "))

if A%2  == 0 and B%2 == 0:
    print("Os valores são multiplos entre si")
elif A%3 == 0 and B%3 == 0:
    print("Os valores são multiplos entre si")
elif  A%5 == 0 and B%5 == 0:
    print("Os valores são multiplos entre si")
elif  A%7 == 0 and B%7 == 0:
    print("Os valores são multiplos entre si")
else:
    print("Os valores não são multiplos")