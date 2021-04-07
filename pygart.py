import pygame

def start():
 pygame.init()
 window = pygame.display.set_mode((1024, 760)) # 1024×760 4:3

 osx = 70
 osy = 50
 player = pygame.rect.Rect(osx, osy, 100, 100) 

 class Player:
     def __init__(self):
         self.osx = 0
         self.osy = 0
         self.width = 0
         self.height = 0
         self.avatar = pygame.image.load("/jppp/rulon223223.png")

     def tick(self):
        speed = 5
        if keys[pygame.K_RIGHT]: 
          osx += self.speed
        if keys[pygame.K_LEFT]:  
          osx -= self.speed
        if keys[pygame.K_UP]:  
          osy -= self.speed
        if keys[pygame.K_DOWN]:  
          osy += self.speed

     def draw(self):
         window.blit(self.avatar,(self.osx,self.osy))

 run = True
 while run:
    pygame.time.Clock().tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False

    keys = pygame.key.get_pressed()

    player = pygame.rect.Rect(osx, osy, 100, 100)

    window.fill((24, 164, 240))  # rysowanie tła
    pygame.draw.rect(window, (20, 200, 20), player) 
    pygame.display.update()

if __name__ == "__main__":
    start()
