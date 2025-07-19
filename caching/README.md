# Caching Algorithms Project

This project implements various caching strategies in Python, based on the `BaseCaching` class.

## 📚 Objectives

- Understand what a caching system is
- Learn and implement different cache replacement policies:
  - FIFO (First-In First-Out)
  - LIFO (Last-In First-Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)

## 📁 Files

| File              | Description                                  |
|-------------------|----------------------------------------------|
| `0-basic_cache.py` | Basic dictionary-based cache (no eviction)  |
| `1-fifo_cache.py`  | FIFO cache replacement policy               |
| `2-lifo_cache.py`  | LIFO cache replacement policy               |
| `3-lru_cache.py`   | LRU cache replacement policy                |
| `4-mru_cache.py`   | MRU cache replacement policy                |
| `base_caching.py`  | Parent class containing shared attributes   |

## 🧪 How to Test

Each cache file has its own test file:

```bash
chmod +x *.py
./0-main.py  # test BasicCache
./1-main.py  # test FIFOCache
./2-main.py  # test LIFOCache
./3-main.py  # test LRUCache
./4-main.py  # test MRUCache
Ensure base_caching.py is present in the same directory as the scripts.

🛠 Requirements
Python 3.9

Ubuntu 20.04 LTS

Files must follow pycodestyle (PEP8)

Run linter check with:

bash
Copier
Modifier
pycodestyle *.py
🧼 File Format
First line must be: #!/usr/bin/env python3

End each file with a newline

All files must be executable:

bash
Copier
Modifier
chmod +x *.py
📝 Documentation
Each file, class, and method contains detailed docstrings explaining their purpose.

🧠 Learning Points
What is a caching system and its use cases

Differences between FIFO, LIFO, LRU, MRU, LFU

How to implement efficient memory replacement mechanisms
