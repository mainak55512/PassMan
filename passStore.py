import rsa,json
from rsa.key import PublicKey
from colorama import Fore

PublicKey = PublicKey(
    8469747975125914834477221733541622396372559197549752093478561809153078640718631889466996182416274676828820428473347471920889575131558260912997506625069509, 65537)

def storePassword():
    data = {}
    desc = input(Fore.LIGHTGREEN_EX +
                 "\U0001F4C3 Service Name (Can't be empty): ")
    username = input(Fore.LIGHTYELLOW_EX + "\U0001F464 Enter New Username: ")
    Passwd = input("\U0001F511 Password: ")
    encPass = rsa.encrypt(Passwd.encode(), PublicKey)
    data[f'{desc}'] = {
        "username": username,
        "password": str(encPass)
    }
    try:
        with open('./.data/password.json',
                  'r') as outfile:
            content=json.load(outfile)
        with open('./.data/password.json',
                  'w') as outfile:
            content.update(data)
            json.dump(content, outfile, indent=4)
    except:
        with open('./.data/password.json',
                  'w') as outfile:
            json.dump(data, outfile, indent=4)
