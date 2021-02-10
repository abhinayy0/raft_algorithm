# echo_server

import socket 

from key_value_operations import KeyValueStore
def run_server():

	kvs = KeyValueStore()
	catch_up(kvs)
	server_address = ('localhost', 10000)

	print(f"starting server on {server_address[0]} port {server_address[1]}")


	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(server_address)
	sock.listen(1)


	while True:
	    print('Waiting for a connection')
	    connection, client_address = sock.accept()

	    try:
	        print(f"connection from {client_address}")

	        while True:
	            operation = connection.recv(1024)
	            if operation:
	            	string_operations = operation.decode("utf-8")
	            	print(f"received {string_operations}")
	            	with open("commands.txt", "a") as file:
	            		file.write(string_operations + '\n')
	            	response = kvs.execute(string_operations)
	            	connection.sendall(response.encode('utf-8'))
	            else:
	            	print(f"no more data from {client_address}")
	            	break
	    finally:
	        connection.close()

def catch_up(key_value_store):
	log = ""
	with open('commands.txt', "r") as file:
		log = file.read()
	
	for command in log.split('\n'):
		key_value_store.execute(command)


run_server()


