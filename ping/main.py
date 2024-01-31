import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("you-spin-me-round.knping.pl", 20000))

def find_task(data):
    res = data.split(' ')
    print(res)


try:
    # Receive data from the server
    data = s.recv(1024)  # 1024 is the buffer size, you can adjust it based on your needs
    data = data.decode('utf-8')
    # Process the received data
    print("Received data:", data) # Assuming the data is in UTF-8 encoding
    task = find_task(data)
finally:
    # Close the socket connection
    s.close()