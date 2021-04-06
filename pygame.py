import pygame

def snake():
    
    pygame.init()
    window = pygame.display.set_mode((800,600))

    osx = 50
    osy = 50
    player = pygame.rect.Rect(osx,osy,100,100)

    start = True
    while start:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        osx += 1
    if keys[pygame.K_LEFT]:
        osx -= 1
    if keys[pygame.K_UP]:
        osy += 1
    if keys[pygame.K_DOWN]:
        osy -= 1

    window.fill((255, 242, 0))
    pygame.draw.rect(window,(50,100,50),player)
    pygame.display.update()

snake()