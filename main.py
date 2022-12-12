import pygame
import os
import sys
from random import randrange


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


def main():
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Спрайты')
    all_sprites = pygame.sprite.Group()
    image = load_image("bomb.png")
    for _ in range(50):
        bomb = pygame.sprite.Sprite(all_sprites)
        bomb.image = image
        bomb.rect = bomb.image.get_rect()
        bomb.rect.x = randrange(width)
        bomb.rect.y = randrange(height)
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
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
