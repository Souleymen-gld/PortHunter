import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    """Scanne un port spécifique sur la cible."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout de 1 seconde
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} est ouvert")
                return port
    except Exception as e:
        print(f"Erreur lors du scan du port {port}: {e}")
    return None

def scan_ports(target, start_port, end_port):
    """Scanne une plage de ports sur la cible."""
    open_ports = []
    print(f"Scan en cours sur {target} pour les ports {start_port} à {end_port}...\n")

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target, p), range(start_port, end_port + 1))

    for port in results:
        if port is not None:
            open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    try:
        target = input("Entrez l'adresse IP ou le domaine à scanner : ")
        start_port = int(input("Entrez le port de départ (1-65535) : "))
        end_port = int(input("Entrez le port de fin (1-65535) : "))

        # Validation des entrées
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Erreur : La plage de ports est invalide.")
            exit(1)

        open_ports = scan_ports(target, start_port, end_port)
        print("\nPorts ouverts trouvés :", open_ports if open_ports else "Aucun")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides pour les ports.")
    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
