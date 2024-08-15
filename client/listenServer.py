import Pyro5.server
import Pyro5.core

class ListenServer(object):
    def __init__(self, cliente):
        self.cliente = cliente
    
    @Pyro5.server.expose
    def set_mensagem_servidor(self, mensagem):
        self.cliente.mensagem_servidor = mensagem
        
    def start_listen_server(self):
        daemon = Pyro5.server.Daemon(host="localhost")
        ns = Pyro5.core.locate_ns()
                # Verifica se o objeto já está registrado e o desregistra
        if hasattr(self, self.cliente.username):
            daemon.unregister(self)
        
        uri = daemon.register(ListenServer)
        ns.register(self.cliente.username, uri)
        print(f"Ready {self.cliente.username}. Object uri = {uri}")
        daemon.requestLoop()



