import pygame, sys, spritesheet

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Museum Mania")

background = pygame.image.load("..\Placeholder Scenes\Museum-Bg-1.png").convert()
background = pygame.transform.smoothscale(background, (1600, 900))

sprite_sheet_image = pygame.image.load('../Sprites/Shouty.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

shouty_animation_list = []
shouty_animation_steps = 2
last_update = pygame.time.get_ticks()
shouty_animation_cooldown = 125
frame = 0

for x in range(shouty_animation_steps):
    shouty_animation_list.append(sprite_sheet.get_image(x, 32, 64, 1, (255,0,255)))
 
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= shouty_animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(shouty_animation_list):
            frame = 0

    screen.blit(background, (0, 0))
    screen.blit(shouty_animation_list[frame], (0, 0))
    pygame.display.update()
