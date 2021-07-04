from hashlib import sha256

enc = sha256()

passwd = "test" # Enter your password here
enc.update(str.encode(f'%fp1%gih#%{passwd}%97@68&%'))
hashed_passwd = enc.hexdigest()
print(hashed_passwd) # copy the generated password from the terminal and paste that to the cred.json's password field