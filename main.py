import pygame
import os
import sys
from random import randrange

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width)
        self.rect.y = randrange(height)

    def update(self):
        self.rect = self.rect.move(randrange(3) - 1, randrange(3) - 1)


def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption('Спрайты')
    all_sprites = pygame.sprite.Group()
    image = load_image("bomb.png")
    for _ in range(50):
        Bomb(all_sprites)
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приёма и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     screen.blit(image, (event.pos[0] - image.get_width()//2,
            #                         event.pos[1] - image.get_height()//2))
        # отрисовка и изменение свойств объектов
        screen.fill("white")
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
