import json
import socket

settings = {
    'host': '127.0.0.1',
    'port': 9091
}

def create_udp_connection():

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((settings['host'], settings['port']))
        return sock
        
    except socket.error as e:
        print(f'Falha ao se conectar com {settings["host"]}:{settings["port"]}')
        print(e)
        return None
    
def receive_data(sock):
    try:
        print(f'Aguardando dados ...')
        data, addr = sock.recvfrom(1024)
        json_data = data.decode('utf-8').split('/n')[0]
        data = json.loads(json_data)
        print(f'Dados recebidos: {data}')
    except Exception as e:
        print('Falha no recebimento do json')
    

sock = None
sock = create_udp_connection()
while True:
    receive_data(sock)
