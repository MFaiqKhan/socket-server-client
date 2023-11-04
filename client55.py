import os
import socket
from tqdm import tqdm
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    """ TCP socket and connecting to the server """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client.connect(ADDR)
            break
        except Exception as e:
            print("Server is offline, retrying...")
            time.sleep(5)
    print("Connected to the server.")

    while True:
        """ Get filename as input from the user """
        filename = input('File to upload (or type "exit" to quit): ')
        if filename.lower() == 'exit':
            break
        if not os.path.isfile(filename):
            print("File does not exist. Please try again.")
            continue

        FILESIZE = os.path.getsize(filename)

        """ Sending the filename and filesize to the server. """
        data = f"{filename}_{FILESIZE}"
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"SERVER: {msg}")

        """ Data transfer. """
        bar = tqdm(range(FILESIZE), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=SIZE)

        with open(filename, "rb") as f:
            while True:
                data = f.read(SIZE)

                if not data:
                    break

                client.send(data)
                msg = client.recv(SIZE).decode(FORMAT)

                bar.update(len(data))
        print("File sent successfully.")

    """ Closing the connection """
    client.close()

if __name__ == "__main__":
    main()
