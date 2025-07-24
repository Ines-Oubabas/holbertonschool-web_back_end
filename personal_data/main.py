#!/usr/bin/env python3
"""Test script for password hashing and validation"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
hashed = hash_password(password)
print(hashed)
print(is_valid(hashed, password))
