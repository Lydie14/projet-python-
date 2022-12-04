import pygame
import cv2
import sys
from cvzone.HandTrackingModule import HandDetector

#initialiser pygame
pygame.init()

score1=0
score2=0
def endInterface(screen, score1, score2):
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('microsoftsansserif', 50)
        msg = 'win!' if score1 > score2 else 'lost'
        texts = [font.render(msg, True,'red'),
            font.render('Press ESCAPE to quit.', True,'red'),
            font.render('Press ENTER to continue or play again.', True,'red')]
        positions = [[220, 200], [200, 270], [200, 300]]
        if score1 or score2==5:
            sys.exit()
# Détection de la main
def main():
    cap = cv2.VideoCapture(0)  
    detector = HandDetector(maxHands=1)
    clock = pygame.time.Clock()# mettre à jour l'horloge du jeu
    
#Declaration de la taille de la fenetre pong
    s_w = 800
    s_h = 600
    col1 = (255, 0, 255)
    col2 = (0, 255, 0)

    s_size =(s_w,s_h)
    fps = 30
    screen = pygame.display.set_mode(s_size)
    clock = pygame.time.Clock()

    # Definir la taille de la balle
    ball = pygame.Rect(s_w/2 - 15,s_h/2 - 15,30,30)
    speedy = 5
    speedx = 5


    #Déclarer les paddles  sous forme rectangulaire
    paddle1 = pygame.Rect(10, s_h/2, 10, 80)
    paddle2 = pygame.Rect(s_w-10,s_h/2,10,80)
    
   


 
    while True:
        success, img = cap.read()# ouverture de la caméra 

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)
        if hands:
            lmList = hands[0]['lmList']  
            pointIndex = lmList[8][1]  #les coordonnées de x , y au bout de l'index 
            
            paddle1.y = pointIndex # orienter la palette selon l'index du doigt 
        cv2.imshow('image', img)
        
    # pour faire une collision avec la balle
        ball.y = ball.y + speedy
        ball.x = ball.x + speedx
        
    
        # imposer un limiteur pour la balle
        if ball.x<0 or ball.x>775:
            speedx = -speedx
        if ball.y<0 or ball.y>565:
            speedy = -speedy

        # imposer un limiteur pour les padlles
        if paddle1.y<0:
            paddle1.y=0
        if paddle2.y<0:
            paddle2.y=0
        if paddle1.y > 750:
            paddle1.y = 750
        if paddle2.y > 750:
            paddle2.y = 750

        #Collision  entre la balle et la paddlel 
        if ball.colliderect(paddle1)or ball.colliderect(paddle2):
            speedx= -1*speedx

        #Auto move de la padelle2
        paddle2.y = ball.y
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()




        screen.fill('black')
        pygame.draw.ellipse(screen,col1,ball) #déclarer la balle dans le jeu
        pygame.draw.rect(screen, col1, paddle1)#déclarer la palette 1 dans le jeu
        pygame.draw.rect(screen, col1, paddle2)#déclarer la palette 2 dans le jeu

        pygame.display.update()#fonction qui met à jour uniquement la "nouvelle" zone dessinée.
        clock.tick(fps)



if __name__ == '__main__':
    main()
    
    
