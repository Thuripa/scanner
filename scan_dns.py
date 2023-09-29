# Guilherme Melo de Jesus - Baseado no livro 'Python para Pentest' de Daniel Moreno
# Ferramenta que automatiza enumeração de servidores DNS

# Importa biblioteca socket
import socket
import threading


def thread():
    for nome in nomes:
        dns = nome.strip() + "." + site

        try:
            print(dns + ": " + socket.gethostbyname(dns))
        except socket.gaierror:
            pass


# Domínio a ser testado
site = "univali.br"

# Abre o arquivo wordlist
with open("brute-force.txt") as arquivo:
    nomes = arquivo.readlines()

threading.Thread(target=thread).start()