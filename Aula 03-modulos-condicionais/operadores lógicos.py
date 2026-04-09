verifica_email=True
verifica_senha=False

login = verifica_email and verifica_senha
print(login)

if login:
    print("entrar no programa")

logica_ou = False or False or False
print(logica_ou)

negacao = not False
print(negacao)

if not login:
    print("Bora, lembra a senha")


