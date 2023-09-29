# Guilherme Melo de Jesus - Baseado no livro 'Python para Pentest' de Daniel Moreno
# Ferramenta que automatiza enumeração de servidores DNS

import socket

dominio = "google.com"

with open("brute-force.txt") as arquivo:
    nomes = arquivo.readlines()

for nome in nomes:
    dns = nome.strip() + "." + dominio

    try:
        print(dns + ": " + socket.gethostbyname(dns))
    except socket.gaierror:
        pass