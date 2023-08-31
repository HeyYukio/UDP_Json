
import socket 
import json
import time

settings = {
    'host': '127.0.0.1',
    'port': 9091
}

data = {
    'category': 'Test',
    'name': "Henrique Yukio Murata",
    'counter': 1
}

def create_connection():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((settings['host'], settings['port']))
        print(f'Conectado a {settings["host"]}:{settings["port"]}')
        return sock
    except socket.error as e:
        print(f'Falha ao se conectar com {settings["host"]}:{settings["port"]}')
        print(e)
        return None

def sendData(sock):   
    json_data = json.dumps(data)
    encoded_json = (json_data+'\n').encode('utf-8')
    sock.sendto(encoded_json, (settings['host'], settings['port']))
    print('Envio do json por UDP bem sucedido')
    data['counter'] = data['counter'] + 1
    time.sleep(5)
    
while True:
    sock = None
    sock = create_connection()
    try:
        sendData(sock)
    except Exception as e:
        print(['Falha ano envio do json por UDP'])
        print(e)
        sock.close()
        break


