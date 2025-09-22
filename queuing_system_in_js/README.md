# 📦 Queuing System in JS

Projet Holberton – **Node.js + Redis + Kue + Express**

Ce projet met en place un système de **file d’attente (queue)** avec Redis et Kue, ainsi qu’une API REST simple utilisant Express et Redis pour gérer des stocks de produits.  
Il couvre plusieurs notions : opérations Redis basiques, Pub/Sub, gestion de jobs avec Kue, suivi de progression/erreurs, tests unitaires et API REST.

---

## 🚀 Installation & Setup

### Prérequis
- Ubuntu 18.04+ (ou WSL2)
- Node.js 12.x
- Redis >= 5.0.7

### Cloner le repo
```bash
git clone https://github.com/<ton-github>/holbertonschool-web_back_end.git
cd holbertonschool-web_back_end/queuing_system_in_js
Installer les dépendances
bash
Copier le code
npm install
Vérifier Redis
bash
Copier le code
redis-cli ping
# → PONG
📂 Structure du projet
0-redis_client.js : connexion Redis basique

1-redis_op.js : opérations GET/SET avec callbacks

2-redis_op_async.js : mêmes opérations en async/await

4-redis_advanced_op.js : stockage et lecture de hash Redis

5-subscriber.js / 5-publisher.js : Pub/Sub Redis

6-job_creator.js / 6-job_processor.js : création et traitement de jobs Kue

7-job_creator.js / 7-job_processor.js : jobs avec progression et blacklist

8-job.js / 8-job-main.js : fonction générique de création de jobs + tests (8-job.test.js)

9-stock.js : API REST Express pour gérer des stocks de produits avec Redis

🧪 Utilisation & Démonstrations
0–4. Redis basique
bash
Copier le code
npm run dev 2-redis_op_async.js
Affiche School, Reply: OK, 100.

5. Pub/Sub
Terminal A (subscriber)

bash
Copier le code
npm run dev 5-subscriber.js
Terminal B (publisher)

bash
Copier le code
npm run dev 5-publisher.js
6–7. Queue avec Kue
Processor

bash
Copier le code
npm run dev 6-job_processor.js
Creator

bash
Copier le code
npm run dev 6-job_creator.js
Task 7 (progress & blacklist)

bash
Copier le code
npm run dev 7-job_processor.js
npm run dev 7-job_creator.js
8. Fonction générique & tests
bash
Copier le code
npm run dev 8-job-main.js
npm test 8-job.test.js
# → 2 passing
9. API Express + Redis
Lancer le serveur :

bash
Copier le code
npm run dev 9-stock.js
Dans un autre terminal :

bash
Copier le code
curl 127.0.0.1:1245/list_products
curl 127.0.0.1:1245/list_products/1
curl 127.0.0.1:1245/reserve_product/1
✅ Résultats attendus
Redis : connexion, GET/SET, hash → OK

Pub/Sub : messages publiés/reçus, arrêt avec KILL_SERVER → OK

Kue : jobs créés/traités, progression, blacklist → OK

Tests : 8-job.test.js → OK (2 passing)

API REST : JSON correct pour la liste, le détail, et la réservation de produits → OK

