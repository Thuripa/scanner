import nmap

# Cria o scanner
scanNmap = nmap.PortScanner()

# Inicia o scan nas portas 22 e 80 -F (scan rápido) -O (OS detection)
scanNmap.scan("192.168.0.1", "22, 80", "-F -O", True)

# Exibe a linha de comando
print(scanNmap.command_line())

# Exibe o resultado do scan
for host in scanNmap.all_hosts():

    print("Nmap scan report for ", host)
    print("Host: ", scanNmap[host]["status"]["state"])

    for protocolo in scanNmap[host].all_protocols():

        print("PORT / STATE / SERVICE ")

        for porta in scanNmap[host][protocolo]:

            alvo = scanNmap[host][protocolo][porta]
            print(str(porta) + " / " + protocolo + " \t" + "/" +
                  alvo["state"] + "\t" + alvo["name"])

            enderecoMAC = scanNmap[host]["addresses"]["mac"]
            print("MAC Address: " + enderecoMAC + " (" +
                  scanNmap[host]["vendor"][enderecoMAC] + ") " + "\n")