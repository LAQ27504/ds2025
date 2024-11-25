import socket

def main():
    host = '127.0.0.1'
    port = 5000
    clients = 5
    
    s_ket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s_ket.bind((host, port))
    s_ket.listen(clients)

    print("Init Clients")

    client_socket, client_andress = s_ket.accept()

    data = client_socket.recv(1024).decode()

    file_name = "output.txt"

    fo = open(file_name, 'w')

    fo.write(data)

    print('Received data and overwrite the data successfully')

    client_socket.close()


if __name__ == "__main__":
    main()