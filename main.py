import pygame,cv2
import sys
from cvzone.HandTrackingModule import HandDetector
pygame.init()

#Declaration de la taille de la fenetre pong
def main():
    cap = cv2.VideoCapture(0) 
    detector = HandDetector(maxHands=1)
    clock = pygame.time.Clock()

    s_w = 800
    s_h = 600
    col1 = (255,255,255)
    col2 = (255,0,0)

    s_size =(s_w,s_h)
    fps = 30
    screen = pygame.display.set_mode(s_size)
    clock = pygame.time.Clock()

    # Definir la taille de la balle
    ball = pygame.Rect(s_w/2 - 15,s_h/2 - 15,30,30)
    speedy = 5
    speedx = 5


    #DECLARER LES PADLLES
    paddle1 = pygame.Rect(10, s_h/2, 10,80)
    paddle2 = pygame.Rect(s_w-25,s_h/2,10,80)


    run = True
    while True:
        success, img = cap.read()

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)
        if hands:
            lmList = hands[0]['lmList']  # hands
            pointIndex = lmList[8][1]  # coordonnées x et y du bout de l'index
            paddle1.y = pointIndex
        cv2.imshow('image', img)
    # pour faire boucollisionger la balle
        ball.y = ball.y + speedy
        ball.x = ball.x + speedx
    # DECLARER LA VITESSE DE LA PALETTE 1
        paddle1.y = paddle1.y +speedy
        # imposer un limiteur pour la balle
        if ball.x<0 or ball.x>775:
            speedx = -speedx
        if ball.y<0 or ball.y>565:
            speedy = -speedy

        # imposer un limiteur pour les padelles
        if paddle1.y<0:
            paddle1.y=0
        if paddle2.y<0:
            paddle2.y=0
        if paddle1.y > 750:
            paddle1.y = 750
        if paddle2.y > 750:
            paddle2.y = 750

        #COLIISION
        if ball.colliderect(paddle1)or ball.colliderect(paddle2):
            speedx= -1*speedx

        #automove
        paddle2.y = ball.y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()




        screen.fill('black')
        pygame.draw.ellipse(screen,col1,ball)
        pygame.draw.rect(screen, col1, paddle1)
        pygame.draw.rect(screen, col1, paddle2)

        pygame.display.update()
        clock.tick(fps)



if __name__ == '__main__':
    main()
    