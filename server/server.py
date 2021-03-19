from time import sleep
import socket


# unused ports: 26490-26999
port = 26969
address = socket.gethostbyname(socket.gethostname())
print(address)
coordinates = [(215,55),(235,52)]
connections = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Binding \"{address}\" to \"{port}\"")
s.bind((address,port))
s.listen(30)

def send(client, msg, encoding="utf8"):
	if msg == "":
		pass
	else:
		compressed = []
		for coordinate in coordinates:
			compressed.append(f"{coordinate[0]},{coordinate[1]}")
		compressed = "|".join(compressed)
		print(compressed)
		client.send(compressed.encode(encoding))

def recv(client, buffer=1024, encoding="utf8"):
	msg = client.recv(buffer).decode(encoding)
	return msg


# client, address = s.accept()
connections.append(s.accept())
print(f"{address}: CONNECTED")

while True:
	coordinates = [(215,55),(235,52)]
	for connection in connections:
		client, address = connection
		print(f"Sent: {coordinates}")
		send(client, coordinates)
	for connection in connections:
		print("TEST")
		client, address = connection
		coordinates.append(recv(client))
		print(coordinates)
	
