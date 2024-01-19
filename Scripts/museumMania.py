import pygame, sys
import spritesheet

pygame.init()

screen = pygame.display.set_mode((960,726))
pygame.display.set_caption("Museum Mania")

BLACK = (255, 0, 255)

background = pygame.image.load("Background.png").convert()
background = pygame.transform.smoothscale(background,(960, 726))
background_rect = background.get_rect()

background_rect.center = (480, 363)

sprite_sheet_image = pygame.image.load('Sprites/Shouty.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

frame_0 = sprite_sheet.get_image(0, 32, 64, 1, (255, 0, 255))
frame_0_rect = frame_0.get_rect()

frame_0_rect.center = (320, 475)

frame_1 = sprite_sheet.get_image(1, 32, 64, 1, (255, 0, 255))
frame_1_rect = frame_1.get_rect()

frame_1_rect.center = (320, 475)

shout = pygame.mixer.Sound('Placeholder/Shout.mp3')

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    screen.blit(background, background_rect)
#TO DO: If absolute value of position of stodian is less than 10 kick out shouty
    if event.type == pygame.MOUSEBUTTONDOWN:
        screen.blit(frame_1, frame_1_rect)
        pygame.mixer.Sound.play(shout)
    else:
        screen.blit(frame_0, frame_0_rect)

    pygame.display.update()
