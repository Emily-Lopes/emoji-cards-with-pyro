import Pyro5.server
import Pyro5.core

class ListenServer(object):
    def __init__(self):
        self.cliente = None
    
    def set_mensagem_servidor(self, mensagem):
        self.cliente.mensagem_servidor = mensagem
        
    def start_listen_server(self, cliente):
        self.cliente = cliente
        daemon = Pyro5.server.Daemon(host="localhost")
        ns = Pyro5.core.locate_ns()
        uri = daemon.register(ListenServer)
        ns.register(self.cliente.username, uri)
        print(f"Ready {self.cliente.username}. Object uri = {uri}")
        daemon.requestLoop()



