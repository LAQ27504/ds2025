from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def upload(argument):
    contents = argument[0]
    filename = argument[1]

    if not os.path.exists(f"MPI/Client/{filename}"):
        return "File does not exist"

    with open(f"MPI/Client/{filename}", "rb") as file:
        content = file.read()

    contents["argument"] = [content, filename]

    comm.send(contents, dest=0)

    response = comm.recv(source=0)
    
    return response


def download(argument):
    contents = argument[0]
    filename = argument[1]

    contents['argument'] = filename

    comm.send(contents, dest=0)

    content = comm.recv(source=0)

    if not content:
        return "File not found"
    else:
        with open(f"MPI/Client/{filename}", "wb") as f:
            f.write(content)
        return f"File {filename} downloaded successfully."


def list(argument):
    contents = argument[0]
    comm.send(contents, dest=0)

    return comm.recv(source=0)



if __name__ == "__main__":
    if rank != 0: 
        print("hello")
        options = {
            "UPLOAD": upload,
            "DOWNLOAD": download,
            "LIST": list,
        }
        while True:
            try:
                userInput = (
                    input(f"[Client {rank}]: Enter operation (UPLOAD <file_name>, DOWNLOAD <file_name>, LIST) or QUIT to exit: ").strip()
                )
                userInput = userInput.split(" ")
                while userInput.count(" "): 
                    userInput.remove(" ")
                operation = userInput[0].upper()
                argument = userInput[-1 : ]

                contents = {
                    "operation" : operation,
                    "argument" : '',
                    "rank" : rank,
                }

                argument = [contents] + argument

                if operation == "QUIT":
                    comm.send(argument,dest=0)
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