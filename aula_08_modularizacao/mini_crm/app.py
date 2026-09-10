from model import model_lead
import control


def add_lead():
    name = input("nome: ")
    email = input("email: ")
    company = input("empresa: ")
    step = input("etapa: ")

    # validar as entradas do usuario
    # depois de validar 

    print(model_lead(name, email, company, step))

    #de pois de modelado ... vamos enviar esse dict(leads) para o leads.json
    control.create_lead(model_lead(name, email, company, step))

    print("Lead adicionado (func)")


def main():

    while True:

        print("\nmini CRM de leads")
        print("\n 1 - adicionar lead")
        print("\n 2 - listar leads")
        print("\n 0 - sair do programa")

        opt = input("Escolha uma opcao: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Listar leads")
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção errada")

if __name__ == "__main__":
    main()