import Pyro5.api

@Pyro5.api.expose
class DatabaseServer:
    def verificar_username(self, username):
        # retorno abaixo é só de teste
        print(f"bd-server: recebi {username} para verificar")
        return f"certo"

    # adicionar outras funcionalidades

def start_db_server():
    Pyro5.api.Daemon.serveSimple(
        {
            DatabaseServer: "emojicards.dbserver" 
        },
        ns=True
    )

if __name__ == "__main__":
    start_db_server()
