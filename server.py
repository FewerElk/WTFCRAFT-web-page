import socket

HOST = '127.0.0.1' # Adresse IP locale de votre machine
PORT = 80 # Port à utiliser pour le serveur
with open("page.html", "r") as file:
    PAGE = file.read()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Serving on http://{HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    
    response = bytes("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{0}".format(PAGE), "utf-8")
    client_socket.sendall(response)
    client_socket.close()
