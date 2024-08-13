import Pyro5.api
from funcionalidades import *

db_server = Pyro5.api.Proxy("PYRONAME:emojicards.dbserver")

@Pyro5.api.expose
class GameServer:
    def criar_conta(self, username, senha):
        # lógica da função
        # ai ao inves de fazer aquilo de fazer requisição eu teria que só inciar um objeto dbserver
        confirmation = db_server.verificar_username(username)

        if confirmation == "certo":
            print("server: conta criada com sucesso!") 
        else:
            return "erro ao criar conta" 

    # adicionar outros métodos

def start_server():
    Pyro5.api.Daemon.serveSimple(
        {
            GameServer: "emojicards.server" 
        },
        ns=True
    )

if __name__ == "__main__":
    start_server()
