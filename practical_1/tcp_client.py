import socket

def main():
    host = '127.0.0.1'
    port = 5000
    
    s_ket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s_ket.connect((host, port))

    filename = input("Input filename")
    fi = open(filename, 'r')
    data = fi.read()

    s_ket.send(str(data).encode())

    data = fi.read()
    fi.close()

if __name__ == "__main__":
    main()