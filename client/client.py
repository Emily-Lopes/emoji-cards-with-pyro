import Pyro5.api

def criar_conta(username, senha):
    server_app = Pyro5.api.Proxy("PYRONAME:emojicards.server")
    try:
        resultado = server_app.criar_conta(username, senha)
        print(resultado)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    criar_conta('ingred', '123')

if __name__ == "__main__":
    main()
