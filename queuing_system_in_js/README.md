# Queuing system in JS

## Prérequis
- Ubuntu 18.04
- Node.js 12.x
- Redis 5.0.7+ (testé avec 6.0.10)
- `npm install` (utilise Babel + Mocha + ESLint + Kue)

## Tâche 0 — Installer Redis
```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make -j$(nproc)
src/redis-server &
src/redis-cli ping    # PONG
src/redis-cli set Holberton School
src/redis-cli get Holberton  # "School"
# Copier dump.rdb depuis redis-6.0.10 (ou 5.0.7) vers la racine du projet:
cp dump.rdb /path/to/queuing_system_in_js/

Scripts utiles

npm run dev <file.js> : lance un fichier avec babel-node + nodemon

npm test <pattern> : lance mocha avec Babel

Exemples rapides

Client Redis de base
npm run dev 0-redis_client.js

Opérations simples
npm run dev 1-redis_op.js

Opérations async/await
npm run dev 2-redis_op_async.js

Hash avancé
npm run dev 4-redis_advanced_op.js

Pub/Sub (2 terminaux)
npm run dev 5-subscriber.js
npm run dev 5-publisher.js

Kue (2 terminaux)
Créateur: npm run dev 6-job_creator.js
Processeur: npm run dev 6-job_processor.js

Kue avec progression/erreurs (2 terminaux)
Créateur: npm run dev 7-job_creator.js
Processeur: npm run dev 7-job_processor.js

Tests unitaires
npm test 8-job.test.js

Stock + Redis + Express
npm run dev 9-stock.js

GET /list_products

GET /list_products/:itemId

GET /reserve_product/:itemId