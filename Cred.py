import json,getpass
from hashlib import sha256
enc=sha256()

def auth():
    with open('./.data/cred.json') as credentials:
        cred = json.load(credentials)
        passwd = getpass.getpass("\N{key} Enter Password: ")
        enc.update(str.encode(f'%fp1%gih#%{passwd}%97@68&%'))
        hashed_passwd = enc.hexdigest()
        if hashed_passwd != cred['passwd']:
            return 0
        else:
            return 1
