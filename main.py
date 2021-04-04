import random

def main():
    print("=> GAME AND APPS <=")
    print(" ")
    menu()


def menu():
    print(" ")
    print("[1] PAPER/STONE/SCISSORS - GAME")
    print("[2] INFO ABOUT FILE/CATALOG / S")
    print("[3] RANDOM VALUE - GUESS WHAT")
    print(" ")

    wybor = int(input("POSITION FROM MENU ======> "))

    if wybor == 1:
        paper()
    elif wybor == 2:
        files()
    elif wybor == 3:
        randomes()

def paper():
    print(" ")
    print("WELCOME to the game versus BOT PC")
    wayUser = input("stone/paper/scissors ==> ")
    tools = ["stone","paper","scissors"]
    wayPC = print(random.choice(tools))

def files():
    print(" ")
    print("INFORMATION about FILE/CATALOG")

def randomes():
    print(" ")
    print("WELCOME to the game guess the number")


main()
