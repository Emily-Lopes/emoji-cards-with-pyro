import Pyro5.api

@Pyro5.api.expose
class DatabaseServer(object):
    def verificar_username(self, username):
        print(f"bd-server: recebi {username} para verificar")
        return f"certo"


def start_db_server():
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(DatabaseServer)
    print(f'dbserver:\n {uri}')
    ns.register("dbserver", uri)
    print("DB-Server ready.")
    daemon.requestLoop() 