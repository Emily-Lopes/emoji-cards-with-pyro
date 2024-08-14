import Pyro5.client
database = Pyro5.client.Proxy("PYRONAME:db-server")
print(database.get_cartas_disponiveis())   