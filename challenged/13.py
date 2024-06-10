from xmlrpc import client

server = "http://www.pythonchallenge.com/pc/phonebook.php"
client = client.ServerProxy(server)

print(client.phone('Bert'))