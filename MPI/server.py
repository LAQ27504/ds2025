from mpi4py import MPI

info = MPI.Info.Create()
service_name = "my_service_name"
port = MPI.Open_port()

try:
    print("Running server")
    MPI.Publish_name(service_name=service_name, port_name=port, info=info)
    print(f"Service '{service_name}' published at port '{port}'.")

    #Wait for a connection from the client
    server = MPI.COMM_WORLD.Accept(port)
    print("Client connected.")

    # # Example communication (e.g., receive and send data)
    # message = server.recv()
    # print(f"Received from client: {message}")
    # server.send("Hello from server!")

    # # Disconnect from the client
    # server.Disconnect()
    # print("Client disconnected.")
finally:
    MPI.Unpublish_name(service_name=service_name, port_name=port, info=info)
    MPI.Close_port(port)
    print("Service unpublished and port closed.")

# def download(fileName):
#     if (os.path.exists(fileName)):
#         with open(fileName, 'rb') as f:
#             content = f.read()
#         return content    
#     else:
#         return False

# def upload(fileName : str, content : bytes):
#     with open(fileName, "wb") as f:
#         f.write(content.data)
#     return "Successfully"

# def list():
#     fileList = os.listdir()
#     return fileList

# def main():
#     host = "192.168.127.103"
#     port = 8080
#     server = xmlrpc.server.SimpleXMLRPCServer((host, port), allow_none=True)
#     print("Start the server")
#     server.register_function(upload, "upload")
#     server.register_function(list, "list")
#     server.register_function(download, "download")
#     server.serve_forever()

#     return 

# if __name__ == "__main__":
#     main()