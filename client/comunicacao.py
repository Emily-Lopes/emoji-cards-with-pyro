import Pyro5.client

@Pyro5.server.expose
class Comunicacao:
    def __init__(self):
        self.server = Pyro5.client.Proxy("PYRONAME:db-server")
        
    
    #def criar_comunicacao_server(self):
    #    self.server = Pyro5.client.Proxy("PYRONAME:db-server")

    def start_client():
        daemon = Pyro5.server.Daemon(host="localhost")
        ns = Pyro5.core.locate_ns()
        uri = daemon.register(Comunicacao)
        ns.register("clint", uri)
        print("Ready. Object uri =", uri)
        daemon.requestLoop()

