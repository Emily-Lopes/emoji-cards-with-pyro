import Pyro5.api
# from funcionalidades import *

db_server = Pyro5.api.Proxy("PYRONAME:dbserver")
print(db_server) 

@Pyro5.api.expose
class ServerApp:
    def criar_conta(self, username, senha):
        confirmation = db_server.verificar_username(username)

        if confirmation == "certo":
            print("server: conta criada com sucesso!") 
        else:
            return "erro ao criar conta" 

    # adicionar outros métodos

def start_server():
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(ServerApp)
    print(f'server:\n {uri}')
    ns.register("server", uri)
    print("Server ready.")
    daemon.requestLoop() 
    
if __name__ == "__main__":
    start_server()