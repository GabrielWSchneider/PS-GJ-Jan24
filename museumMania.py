import pygame, sys

def get_image(sheet, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image

pygame.init()

screen = pygame.display.set_mode((960,726))

pygame.display.set_caption("Museum Mania")

background = pygame.image.load("Background.png").convert()
background = pygame.transform.smoothscale(background,(960, 726))
background_rect = background.get_rect()

background_rect.center = (480, 363)

sprite_sheet_image = pygame.image.load('Sprites/Shouty.png').convert_alpha()
frame_0 = get_image(sprite_sheet_image, 32, 64, 1, BLACK)
frame_0_rect = frame_0.get_rect()

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    screen.blit(background, background_rect)
    screen.blit(frame_0, frame_0_rect)
    pygame.display.update()
