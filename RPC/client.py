import xmlrpc.client
import os
from typing import Dict, Callable


def upload(argument):
    server = argument[0]
    filename = argument[1]

    if not os.path.exists(filename):
        return "File does not exist"

    with open(filename, "rb") as file:
        content = file.read()

    response = server.upload(filename, content)

    return response


def download(argument):
    server = argument[0]
    filename = argument[1]
    content = server.download(filename)

    if not content:
        return "File not found"
    else:
        with open(filename, "wb") as f:
            f.write(content.data)
        return f"File {filename} downloaded successfully."


def list(argument):
    server = argument[0]
    files = server.list()
    return files


if __name__ == "__main__":
    host = "192.168.127.103"
    port = 8080

    server = xmlrpc.client.ServerProxy(f"http://{host}:{port}/", allow_none=True)
    options = {
        "UPLOAD": upload,
        "DOWNLOAD": download,
        "LIST": list,
    }
    while True:
        try:
            userInput = (
                input("Enter operation (UPLOAD <file_name>, DOWNLOAD <file_name>, LIST) or QUIT to exit: ").strip()
            )
            userInput = userInput.split(" ")
            while userInput.count(" "): 
                userInput.remove(" ")
            operation = userInput[0].upper()
            argument = userInput[-1 : ]

            argument = [server] + argument

            if operation == "QUIT":
                break

            if operation not in options:
                print("Invalid operation")
                continue
            else:
                response = options[operation](argument)
                print("Response from server:", response)

        except Exception as e:
            print(f"Error: {e}")
            continue