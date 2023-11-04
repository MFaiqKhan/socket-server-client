import os
import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    """ TCP socket and connecting to the server """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[+] Listening...")

    while True:
        """ Accepting the connection from the client. """
        conn, addr = server.accept()
        print(f"[+] Client connected from {addr[0]}:{addr[1]}")

        while True:
            """ Receiving the filename and filesize from the client. """
            data = conn.recv(SIZE).decode(FORMAT)
            if not data:
                break
            filename, filesize = data.split("_")
            filename = os.path.basename(filename)
            FILESIZE = int(filesize)

            print("[+] Filename and filesize received from the client.")
            conn.send("Filename and filesize received".encode(FORMAT))

            """ Data transfer """
            bar = tqdm(range(FILESIZE), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=SIZE)

            with open(f"recv_{filename}", "wb") as f:
                while True:
                    data = conn.recv(SIZE)

                    if not data:
                        break

                    f.write(data)
                    conn.send("Data received.".encode(FORMAT))

                    bar.update(len(data))
            print("File received successfully.")

        """ Closing connection. """
        conn.close()

if __name__ == "__main__":
    main()
