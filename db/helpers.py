import tinydb
import hashlib

def load_db():
    return tinydb.TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
