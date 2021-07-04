import json, questionary
from colorama import Fore


def delPassword():
    try:
        with open('./.data/password.json',
                  'r') as outfile:
            content = json.load(outfile)
            options = list(content.keys())
            options.append("* Go Back *")
            opt = questionary.select("Select Service Name:",
                                     choices=options).ask()
            for desc in content:
                if desc == opt:
                    content.pop(f"{desc}")
                    break

        with open('./.data/password.json',
                  'w') as outfile:
            json.dump(content, outfile, indent=4)
    except:
        print(Fore.RED + "\n!!! Something went wrong !!!")
