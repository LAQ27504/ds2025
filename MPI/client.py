from mpi4py import MPI

# Specify the service name used by the server
service_name = "my_service_name"

try:
    # Look up the service's port using its published name
    port = MPI.Lookup_name(service_name=service_name)
    print(f"Found service '{service_name}' at port '{port}'.")

    # Connect to the service
    client = MPI.COMM_WORLD.Connect(port)
    print("Connected to the server.")

    # Example communication (e.g., send and receive data)
    client.send("Hello from client!")
    response = client.recv()
    print(f"Received from server: {response}")

    # Disconnect from the server
    client.Disconnect()
    print("Disconnected from the server.")
except Exception as e:
    print(f"Error: {e}")


# def upload(argument):
#     server = argument[0]
#     filename = argument[1]

#     if not os.path.exists(filename):
#         return "File does not exist"

#     with open(filename, "rb") as file:
#         content = file.read()

#     response = server.upload(filename, content)

#     return response


# def download(argument):
#     server = argument[0]
#     filename = argument[1]
#     content = server.download(filename)

#     if not content:
#         return "File not found"
#     else:
#         with open(filename, "wb") as f:
#             f.write(content.data)
#         return f"File {filename} downloaded successfully."


# def list(argument):
#     server = argument[0]
#     files = server.list()
#     return files


# if __name__ == "__main__":
#     host = ""
#     port = 8080

#     server = xmlrpc.client.ServerProxy(f"http://{host}:{port}/", allow_none=True)
#     options = {
#         "UPLOAD": upload,
#         "DOWNLOAD": download,
#         "LIST": list,
#     }
#     while True:
#         try:
#             userInput = (
#                 input("Enter operation (UPLOAD <file_name>, DOWNLOAD <file_name>, LIST) or QUIT to exit: ").strip()
#             )
#             userInput = userInput.split(" ")
#             while userInput.count(" "): 
#                 userInput.remove(" ")
#             operation = userInput[0].upper()
#             argument = userInput[-1 : ]

#             argument = [server] + argument

#             print(argument)
#             if operation == "QUIT":
#                 break

#             if operation not in options:
#                 print("Invalid operation")
#                 continue
#             else:
#                 response = options[operation](argument)
#                 print("Response from server:", response)

#         except Exception as e:
#             print(f"Error: {e}")
#             continue