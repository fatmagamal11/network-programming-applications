import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7000))

def start():
    connected=True
    nick=input("if you need disconnect write 'DES'\nif not Choose your nickname: ")
    client.send(nick.encode("utf-8"))
    while connected:
        if nick=="DES":
            connected=False
        else:
            print("you can send or recieve -->>> ")
            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=send)
            write_thread.start() 














# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(f"You recieved ' {message} '")
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
        
# Sending Messages To Server
def send():
    while True:
        message = input()
        client.send(message.encode('ascii'))
        
