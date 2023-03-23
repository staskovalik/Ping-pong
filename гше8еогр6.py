from pygame import *
from random import randint

clock = time.Clock()
run = True
font.init()
text = font.Font(None, 70).render(message, True, (255, 255, 255))
while run:
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
                 
    #рендер
    window.blit(text, (250, 250))
    display.update()
    clock.tick(60)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))

