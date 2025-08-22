#!/usr/bin/env python3
from exercise import Cache, replay

cache = Cache()

# Task 0-1 : store et get
key = cache.store(b"hello")
print("Stored key:", key)
print("Retrieved:", cache.get(key, fn=lambda d: d.decode("utf-8")))

# Task 2 : compteur d'appels
print("Count after first store:", cache.get(cache.store.__qualname__))

# Task 3 : historique
k1 = cache.store("foo")
k2 = cache.store("bar")
k3 = cache.store(42)

# Task 4 : replay
replay(cache.store)
