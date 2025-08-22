# 0x0B. Redis basic

## Description
Projet visant à manipuler Redis avec Python.  
On y apprend à :
- Écrire et lire des données simples dans Redis
- Convertir les types (bytes → str/int)
- Compter le nombre d’appels d’une méthode avec Redis
- Sauvegarder l’historique des entrées et sorties
- Rejouer l’historique avec `replay`

## Technologies
- Python 3.9
- Redis (installé sur Ubuntu 20.04)
- redis-py

## Installation

```bash
# Installer Redis
sudo apt-get -y install redis-server

# Lancer Redis dans le container
service redis-server start

# Installer la dépendance Python
pip3 install redis

Usage
./main.py

2. requirements.txt

Pour lister la dépendance :

redis

3. Rappel sur la structure de ton dossier
holbertonschool-web_back_end/
└── 0x0B_redis_basic/
    ├── exercise.py   # tout le code du projet
    ├── main.py       # fichiers de test
    ├── README.md
    └── requirements.txt