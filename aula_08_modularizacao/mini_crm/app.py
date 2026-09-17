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

def list_leads():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead ainda")
        return

    print(f"## | {"Nome":<20} | {"email":<20} | Empresa")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["email"]:<20} | {lead["company"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()

    if not query:
        print("Consulta vazia")

        return 

#Envia a query para o control realizar a busca no leads

    leads_found = control.read_leads_search(query)

    print(f"## | {"Nome":<20} | {"email":<20} | Empresa")
    for i, lead in leads_found:
        print(f"{i:02d} | {lead["name"]:<20} | {lead["email"]:<20} | {lead["company"]}")


def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possivel exportar os leads")
    else:
        print(f"Exportado para {path_csv}")

def main():

    while True:

        print("\nmini CRM de leads")
        print("\n 1 - adicionar lead")
        print("\n 2 - listar leads")
        print("\n 3 - Buscar (nome/email/empresa)")
        print("\n 4 - Exportar CSV")
        print("\n 0 - sair do programa")

        opt = input("Escolha uma opcao: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção errada")

if __name__ == "__main__":
    main()