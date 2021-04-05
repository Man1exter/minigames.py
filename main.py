import random
import os
from random import randint

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
        paperGame()
    elif wybor == 2:
        files()
    elif wybor == 3:
        randomes()

def paperGame():
    print(" ")
    print("WELCOME to the game versus BOT PC")
    print(" ")
    
    rounds = int(input("how manu round do you want to play? => "))
    win = 0
    draw = 0
    lose = 0
    x = 0

    while x < rounds:
     wayUser = input("stone/paper/scissors ==> ")
     tools = ["stone","paper","scissors"]
     wayPC = print(random.choice(tools))

     if wayUser == wayPC:
         print(f"Both players selected {wayUser}")
         draw += 1
     elif wayUser == "stone":
       if wayPC == "scissors":
         print("Rock smashes scissors! You win!")
         win += 1
         x += 1
       else:
         print("Paper covers stone! You lose.")
         lose += 1
         x += 1
     elif wayUser == "paper":
       if wayPC == "stone":
         print("Paper covers stone! You win!")
         win += 1
         x += 1
       else:
         print("Scissors cuts paper! You lose.")
         lose += 1
         x += 1
     elif wayUser == "scissors":
       if wayPC == "paper":
         print("Scissors cuts paper! You win!")
         win += 1
         x += 1
     else:
         print("Rock smashes scissors! You lose.")
         lose += 1
         x += 1

    print("Wins => ",win)
    print("Draws => ",draw)
    print("Losses => ",lose)



def files():
      
    print(" ")
    print("INFORMATION about FILE/2x/CATALOG/2x")
    print(" ")
    print("catalog localization => ",os.getcwd())
    print("all files in catalog => ",os.listdir())
    print(" ")
    print("new catalog ====> os.mkdir() ")
    print("new catalogs ====> os.makedirs() ")
    print(" ")
    print("del catalog ====> os.rmdir() ")
    print("del catalogs ====> os.removedirs() ")
    print(" ")


def randomes():
      
    print(" ")
    print("WELCOME to the game guess the number")
    print(" ")

    roll = randint(1,100)
    answer = -1
    it = 0
    print("numbers 1 - 100")
    while answer != roll:
      it += 1
      answer = int(input("guess number: "))
      if answer > roll:
           print("an even greater number")
      elif answer < roll:
           print("an even smaller number")
    print("Amazing only => ",it," rounds")

main()
