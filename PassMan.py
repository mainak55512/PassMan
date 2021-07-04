import questionary, sys
import passStore, passFetch, delPass, Cred
from colorama import Fore, Style
from os import system,name

print("\n\n")
print("==========================================================")
print("******                          *       *                 ")
print("*    *  ******  ******  ******  * *   * *  ******  *     *")
print("*    *  *    *  *       *       *   *   *  *    *  * *   *")
print("******  ******  ******  ******  *       *  ******  *  *  *")
print("*       *    *       *       *  *       *  *    *  *   * *")
print("*       *    *  ******  ******  *       *  *    *  *     *")
print("==========================================================")
print("\n\n")

if Cred.auth():
    while True:
        print()
        opt = questionary.select("What to do? ",
                                 choices=[
                                     "Fetch Password", "Store Password",
                                     "Delete Password", "Quit"
                                 ]).ask()

        if opt == "Fetch Password":
            print()
            passFetch.getPassword()

        elif opt == "Store Password":
            print()
            passStore.storePassword()

        elif opt == "Delete Password":
            delPass.delPassword()

        elif opt == "Quit":
            if name=='nt':
                _ = system('cls')
            else:
                _ = system('clear')
            sys.exit()
else:
    print(Fore.RED + Style.BRIGHT + "\n!!...Password does not Match...!!")
