Python Socket File Transfer
Python Socket File Transfer is a simple command-line tool that uses Python's socket module to transfer files and directories over a network.

Installation
The scripts require Python 3.6 or later. You can check your Python version by running python --version.

You will also need to install the tqdm library if it's not already installed. You can install it with pip:

pip install tqdm
Usage
There are two scripts involved in the file transfer process: a server script (s.py) and a client script (c.py).

Server
To start the server, navigate to the directory containing s.py and run:

python s.py
The server will start listening for connections on port 5000. When a client connects, it will receive files sent by the client and save them in the current directory.

Client
To send a file, navigate to the directory containing c.py and run:

python c.py
The client script will connect to the server and prompt you for a file to upload. Enter the path to the file you want to upload. The file will then be sent to the server.


https://github.com/MFaiqKhan/socket-server-client