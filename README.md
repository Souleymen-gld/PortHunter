# PortScanner - Scanner de Ports en Python

PortScanner est un simple scanner de ports TCP écrit en Python. Il permet de scanner une plage de ports d'une adresse IP ou d'un domaine afin de détecter les ports ouverts.

## Fonctionnalités
- **Scan de ports** : Scanne une plage de ports (par exemple, de 1 à 65535).
- **Affichage des ports ouverts** : Affiche les ports ouverts trouvés durant le scan.
- **Compatible avec IPv4** : Utilise l'adresse IP de l'hôte ou un nom de domaine pour effectuer le scan.
- **Timeout configurable** : La durée maximale pour la connexion à chaque port peut être ajustée.

## Installation

### Prérequis
- Python 3.x

### Étapes d'installation

1. Clonez le dépôt ou téléchargez le fichier `port_scanner.py` sur votre machine.
   
   ```bash
   git clone <URL_du_repository>
Vous n'avez besoin d'aucune bibliothèque supplémentaire pour faire fonctionner ce script.

Ouvrez un terminal et naviguez vers le dossier contenant le fichier port_scanner.py.

cd /chemin/vers/le/dossier
Utilisation
Exécutez le script avec Python :

python port_scanner.py
Le programme vous demandera d'entrer l'adresse IP ou le domaine à scanner, ainsi que la plage de ports que vous souhaitez analyser.

Exemple :

Entrez l'adresse IP ou le domaine à scanner : 192.168.1.1
Entrez le port de départ : 20
Entrez le port de fin : 1024
Le programme affichera les ports ouverts trouvés.

Exemple de sortie :

Modifier
Port 22 est ouvert
Port 80 est ouvert
Port 443 est ouvert

Ports ouverts trouvés : [22, 80, 443]
Exemple d'exécution

Voici un exemple d'exécution du programme :

Entrez l'adresse IP ou le domaine à scanner : example.com
Entrez le port de départ : 1
Entrez le port de fin : 100
Port 22 est ouvert
Port 80 est ouvert
Port 443 est ouvert

Ports ouverts trouvés : [22, 80, 443]
Avertissements
Ce programme est destiné à être utilisé dans un but éthique et responsable.

Veuillez obtenir l'autorisation explicite avant de scanner des réseaux ou des hôtes qui ne vous appartiennent pas.

Contributions
Les contributions sont les bienvenues ! Si vous avez des suggestions ou des corrections, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.
