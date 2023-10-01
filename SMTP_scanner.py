# Guilherme Melo de Jesus - Baseado no livro 'Python para Pentest' de Daniel Moreno

# Ferramenta para enumeração de usuários SMTP

import socket

usuarios = ["admin", "teste", "root"]

for usuario in usuarios:

    # Cria um socket para se conectar com o servidor SMTP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta no servidor
    sock.connect(("IP DO SERVIDOR", 25))

    # Recebe o Banner do servidor
    sock.recv(1024)

    # Envia o nome de usuário para teste
    sock.send("VRFY " + usuario + "\n")

    # Recebe resposta do servidor em forma de 1024 bytes
    resposta = sock.recv(1024)

    # Encerra conexão
    sock.close()

    if "252" in resposta:
        print(usuario + " -> Válido")
    elif "550" in resposta:
        print(usuario + " -> Usuário não encontrado!")
    elif "503" in resposta:
        print("Servidor requer autenticação!")
        break
    elif "500" in resposta:
        print("Comando não suportado!")
        break
    else:
        print("Resposta do servido: " + resposta)

