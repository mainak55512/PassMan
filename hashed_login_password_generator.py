from hashlib import sha256

enc = sha256()

passwd = input("Enter new login Password: ") # Enter your password here
enc.update(str.encode(f'%fp1%gih#%{passwd}%97@68&%'))
hashed_passwd = enc.hexdigest()
print("The Hashed Password is: ",hashed_passwd) # copy the generated password from the terminal and paste that to the cred.json's password field