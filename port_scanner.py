# Guilherme Melo de Jesus - Baseado no livro 'Python para Pentest' de Daniel Moreno

# Ferramenta que realiza a varredura de portas

import socket

host = "192.168.0.1"
portas = [21, 22, 23, 80, 443]

for porta in portas:

    # Cria um socket do tipo TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define um intervalo de 1 segundo
    sock.settimeout(1)

    # Captura resposta
    resposta = sock.connect_ex((host, porta))

    # Encerra conexão
    sock.close()

    # Verifica se a reposta é 0 (porta aberta)
    if (resposta == 0):
        print(porta)