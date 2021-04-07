import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((1024, 760)) # 1024 × 760 4:3

class Player:
    def __init__(self):
        self.osx = 0  
        self.osy = 0  
        self.image = pygame.image.load("./jppp/rulon223223.png")  
        self.width = 50 
        self.height = 50
        self.speed = 4  
        self.hitbox = pygame.Rect(self.osx, self.osy, self.width, self.height)

    def tick(self, keys): 
        if keys[pygame.K_UP]:
            self.osy -= self.speed
        if keys[pygame.K_LEFT]:
            self.osx -= self.speed
        if keys[pygame.K_DOWN]:
            self.osy += self.speed
        if keys[pygame.K_RIGHT]:
            self.osx += self.speed

        self.hitbox = pygame.Rect(self.osx, self.osy, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.osx, self.osy))

class Cash:
    def __init__(self):
        self.osx = randint(0, 1280)
        self.osy = randint(0, 720)
        self.image = pygame.image.load("./jppp/harnas-butelka-promo.png")
        self.width = 25  
        self.height = 25
        self.hitbox = pygame.Rect(self.osx, self.osy, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.osx, self.osy, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.osx, self.osy))

def start():
    run = True
    player = Player()
    clock = 0
    score = 0
    beers = []
    background = pygame.image.load("./jppp/ruloniktilt1.png")
    while run:
        clock += pygame.time.Clock().tick(60) / 1000  
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
        keys = pygame.key.get_pressed()
        if clock >= 2:
            clock = 0
            beers.append(Cash())

        player.tick(keys)
        for banknote in beers:
            banknote.tick()

        for banknote in beers:
            if player.hitbox.colliderect(banknote.hitbox):
                beers.remove(banknote)
                score += 1

        window.blit(background, (0, 0))  
        player.draw()
        for banknote in beers:
            banknote.draw()
        pygame.display.update()

    print("Wypiles ",score," sztuk NIEZIEMSKIEGO NEKATRU")

if __name__ == "__main__":
    start()
