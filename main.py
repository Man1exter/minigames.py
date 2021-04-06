#import pygame
import random
import os
from random import randint

def main():
    print(" ")
    print("=> GAME AND APPS <=")
    print(" ")
    menu()


def menu():
    print(" ")
    print("[1] PAPER/STONE/SCISSORS - GAME")
    print("[2] INFO ABOUT FILE/CATALOG / S")
    print("[3] RANDOM VALUE - GUESS WHAT")
    print("[4] SNAKE GAME IN WINDOW")
    print(" ")

    ex = int(input("POSITION FROM MENU ======> "))

    if ex == 1:
        paperGame()
    elif ex == 2:
        files()
    elif ex == 3:
        randomes()
    elif ex == 4:
          snake()

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
    print("all date and upgrades in file ==> ",os.stat("main.py"))
    print(" ")
    print(" ")
    print("rename file ==> ",os.rename("from","to"))
    print("3 more info about localization ==> ",os.walk("directory"))
    print("open file ==> ",os.startfile("path........"))
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


def snake():
      
      print(" ")
      print(" <=> SNAKE GAME <=> ")
      print(" ")
      
      #pygame.init()
      #window = pygame.display.set_mode((800,600))

      #osx = 50
      #osy = 50
      #player = pygame.rect.Rect(osx,osy,100,100)

      #start = True
      #while start:
            #pygame.time.Clock().tick(60)
            #for event in pygame.event.get():
                  #if event.type == pygame.QUIT:
                        #start = False

      #keys = pygame.key.get_pressed()

      #if keys[pygame.K_RIGHT]:
            #osx += 1
      #if keys[pygame.K_LEFT]:
            #osx -= 1
      #if keys[pygame.K_UP]:
            #osy += 1
      #if keys[pygame.K_DOWN]:
            #osy -= 1

      #window.fill((255, 242, 0))
      #pygame.draw.rect(window,(50,100,50),player)
      #pygame.display.update()
main()
