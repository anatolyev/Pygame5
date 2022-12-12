import pygame
import os
import sys


pygame.init()
SIZE = WIDTH, HEIGHT = 400, 400
SCREEN = pygame.display.set_mode(SIZE)


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
    clock = pygame.time.Clock()
    pygame.display.set_caption('Заголовок окна')
    all_sprites = pygame.sprite.Group()
    # место для новых спрайтов
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приёма и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        # отрисовка и изменение свойств объектов
        SCREEN.fill("white")
        all_sprites.draw(SCREEN)
        all_sprites.update()
        clock.tick(30)  # 30 кадров в секунду
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
