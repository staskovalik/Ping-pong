from pygame import*

def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    font.init()
    text = font.Font(None, 70).render(message, True, (255, 255, 255))
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                quit()

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

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed

window = display.set_mode((700, 500))
clock = time.Clock()
while True:
    #обробка подій
    for e in event.get():
        if e.type == QUIT:
            quit()
    # оновлення обєктів

    # відмалювати
    window.fill((100, 100, 100))
    display.update()
    clock.tick(60)

    
