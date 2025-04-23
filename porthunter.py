import socket

def scan_ports(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout de 1 seconde
        result = sock.connect_ex((target, port))  # Connecte à l'hôte et au port

        if result == 0:
            print(f"Port {port} est ouvert")
            open_ports.append(port)
        sock.close()

    return open_ports

if __name__ == "__main__":
    target = input("Entrez l'adresse IP ou le domaine à scanner : ")
    start_port = int(input("Entrez le port de départ : "))
    end_port = int(input("Entrez le port de fin : "))

    open_ports = scan_ports(target, start_port, end_port)
    print("\nPorts ouverts trouvés :", open_ports)
