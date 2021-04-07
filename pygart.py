import pygame

def start():
 pygame.init()
 window = pygame.display.set_mode((800, 600))

 osx = 70
 osy = 50
 player = pygame.rect.Rect(osx, osy, 100, 100)  # tworzy prostokąt

 run = True
 while run:
    pygame.time.Clock().tick(60)  # maksymalnie 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
            run = False

    keys = pygame.key.get_pressed()

    speed = 5
    if keys[pygame.K_RIGHT]:  # czy strzałka w prawo jest naciskana
        osx += speed
    if keys[pygame.K_LEFT]:  # strzałka w lewo
        osx -= speed
    if keys[pygame.K_UP]:  # strzałka w górę
        osy -= speed
    if keys[pygame.K_DOWN]:  # strzałka w dół
        osy += speed

    player = pygame.rect.Rect(osx, osy, 100, 100)

    window.fill((24, 164, 240))  # rysowanie tła
    pygame.draw.rect(window, (20, 200, 20), player)  # rysowanie gracza
    pygame.display.update()


if __name__ == "__main__":
    start()
