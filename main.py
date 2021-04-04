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
    print(" ")
    
    wayUser = input("stone/paper/scissors ==> ")
    tools = ["stone","paper","scissors"]
    wayPC = print(random.choice(tools))

    if wayPC == "stone" & wayUser == "paper" | wayPC == "paper" & wayUser == "scissors" | wayPC == "scissors" & wayUser == "stone":
        print(" ====> WYGRALES")
    elif wayPC == "stone" & wayUser == "stone" | wayPC == "paper" & wayUser == "paper" | wayPC == "scissors" & wayUser == "scissors":
        print(" ====> REMIS")
    elif wayPC == "paper" & wayUser == "stone" | wayPC == "scissors" & wayUser == "paper" | wayPC == "stone" & wayUser == "scissors":
        print(" ====> PRZEGRALES")

def files():
    print(" ")
    print("INFORMATION about FILE/CATALOG")

def randomes():
    print(" ")
    print("WELCOME to the game guess the number")


main()
