import json,rsa,questionary
from rsa.key import PrivateKey
from colorama import Fore

PrivateKey = PrivateKey(
    8469747975125914834477221733541622396372559197549752093478561809153078640718631889466996182416274676828820428473347471920889575131558260912997506625069509,
    65537,
    3358588436723870099613867562007410818879870430839418304245248703728736554282025776753187032693453126527787037620830372999298393620468446422454763696465969,
    6041814767429708774424408935997568800665609534932834082160594529331848484908504763,
    1401854956028234928408149462017513211912827740827488259317472792365506943)
def getPassword():
    try:
        with open('./.data/password.json',
                  'r') as outfile:
            content = json.load(outfile)
            options = list(content.keys())
            options.append("* Go Back *")
            opt = questionary.select(
                "Select Service Name:",
                choices = options).ask()
            _desc = opt
            for desc in content:
                if desc == _desc:
                    _Pass = content[f"{desc}"]["password"]
                    username = content[f"{desc}"]["username"]
                    fetchPass = _Pass[2:len(_Pass) - 1]
                    print("\n\n---------------------------------------------------------")
                    print(Fore.LIGHTBLUE_EX + "\n\U0001F464 Username: ",
                          Fore.LIGHTYELLOW_EX + username)
                    _stng = fetchPass.encode('iso-8859-15')
                    fetchPass = _stng.decode('unicode_escape').encode('latin1')
                    decPass = rsa.decrypt(fetchPass, PrivateKey).decode()
                    print(Fore.LIGHTBLUE_EX + "\n\U0001F511 Password: ",
                          Fore.CYAN + decPass,"\n")
                    print(Fore.RESET+
                        "---------------------------------------------------------\n\n"
                    )
    except:
        print(Fore.RED + "\nNo Password saved")
