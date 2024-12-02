import xmlrpc.server
import os

def download(fileName):
    if (os.path.exists(fileName)):
        with open(fileName, 'rb') as f:
            content = f.read()
        return content    
    else:
        return False

def upload(fileName : str, content : bytes):
    with open(fileName, "wb") as f:
        f.write(content.data)
    return True

def list():
    fileList = os.listdir()
    return fileList

def main():
    host = "127.0.1.1"
    port = 8080
    server = xmlrpc.server.SimpleXMLRPCServer((host, port), allow_none=True)
    print("Start the server")
    server.register_function(upload, "upload")
    server.register_function(list, "list")
    server.register_function(upload, "upload")
    server.serve_forever()

    return 

if __name__ == "__main__":
    main()