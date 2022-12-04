import pygame,sys
from button import *

pygame.init()

s_w = 800
s_h = 600
col1 = (255,255,255)
col2 = (255,0,0)

s_size =(s_w,s_h)
fps = 30
screen = pygame.display.set_mode(s_size)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

commencer_img = font.render('COMMENCER',True,col1)
commencer_button = Button(400, 125, commencer_img, 1)
help_img = font.render('HELP',True,col1)
help_button = Button(420, 225, help_img, 1)
historique_img = font.render('HISTORIQUE',True,col1)
historique_button = Button(430, 325, historique_img, 1)
exit_img = font.render('EXIT',True,col1)
exit_button = Button(440, 425, exit_img, 1)
while True:
    screen.fill((41, 36, 33))
    if commencer_button.draw(screen):
        print()
    if help_button.draw(screen):
        print('a fin de maitriser le jeux, il suffit de faire bouger la palette avec la detection de la main, le but c est de ne pas laisser la balle depasser les limite de la pallete' )
    if historique_button.draw(screen):
        print()
    if exit_button.draw(screen):
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(fps)
