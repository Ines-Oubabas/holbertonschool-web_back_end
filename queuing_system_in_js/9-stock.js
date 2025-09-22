// 9-stock.js
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

/** ========= Données produits ========= */
const listProducts = [
  { id: 1, name: 'Suitcase 250',  price: 50,  stock: 4 },
  { id: 2, name: 'Suitcase 450',  price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650',  price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((p) => p.id === Number(id));
}

/** ========= Redis (stock réservé) ========= */
const client = redis.createClient(); // 127.0.0.1:6379 par défaut (redis v2.x)
client.on('error', (err) => console.error('Redis error:', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const stockKey = (itemId) => `item.${itemId}`;

async function reserveStockById(itemId, stock) {
  await setAsync(stockKey(itemId), String(stock));
}

async function getCurrentReservedStockById(itemId) {
  const val = await getAsync(stockKey(itemId));
  return Number(val) || 0;
}

/** ========= Routes ========= */

// Liste de tous les produits
app.get('/list_products', (_req, res) => {
  res.json(
    listProducts.map((p) => ({
      itemId: p.id,
      itemName: p.name,
      price: p.price,
      initialAvailableQuantity: p.stock,
    }))
  );
});

// Détail d’un produit + quantité courante
app.get('/list_products/:itemId', async (req, res) => {
  const product = getItemById(req.params.itemId);
  if (!product) return res.json({ status: 'Product not found' });

  const reserved = await getCurrentReservedStockById(product.id);
  const currentQuantity = Math.max(product.stock - reserved, 0);

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// Réserver 1 unité d’un produit
app.get('/reserve_product/:itemId', async (req, res) => {
  const product = getItemById(req.params.itemId);
  if (!product) return res.json({ status: 'Product not found' });

  const reserved = await getCurrentReservedStockById(product.id);
  const remaining = product.stock - reserved;

  if (remaining <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: product.id });
  }

  await reserveStockById(product.id, reserved + 1);
  res.json({ status: 'Reservation confirmed', itemId: product.id });
});

/** ========= Start server ========= */
app.listen(port, '0.0.0.0', () => {
  console.log(`API listening on http://localhost:${port}`);
});
