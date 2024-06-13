######################################################
# Nia Bourgeois and Rocio Comparini
# Nov 10
# Space Invaders game
# References:
#   https://github.com/attreyabhatt/Space-Invaders-Pygame
######################################################



import math
import random


import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 800))

# Background
background = pygame.image.load('spaceinvaders/background.png')

# Sound
mixer.music.load("spaceinvaders/background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceinvaders/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceinvaders/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Create the Apple
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('spaceinvaders/APPLE.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Create the Banana
bananaImg = []
bananaX = []
bananaY = []
bananaX_change = []
bananaY_change = []
num_of_banana = 1

for i in range(num_of_banana):
    bananaImg.append(pygame.image.load('spaceinvaders/banana.png'))
    bananaX.append(random.randint(0, 736))
    bananaY.append(random.randint(50, 150))
    bananaX_change.append(4)
    bananaY_change.append(40)

# Create the Strawberry
strawberryImg = []
strawberryX = []
strawberryY = []
strawberryX_change = []
strawberryY_change = []
num_of_strawberry = 1

for i in range(num_of_strawberry):
    strawberryImg.append(pygame.image.load('spaceinvaders/strawberry.png'))
    strawberryX.append(random.randint(0, 736))
    strawberryY.append(random.randint(50, 150))
    strawberryX_change.append(4)
    strawberryY_change.append(40)

# Create the pencil
pencilImg = []
pencilX = []
pencilY = []
pencilX_change = []
pencilY_change = []
num_of_pencil = 1

for i in range(num_of_pencil):
    pencilImg.append(pygame.image.load('spaceinvaders/pencil.png'))
    pencilX.append(random.randint(0, 736))
    pencilY.append(random.randint(50, 150))
    pencilX_change.append(4)
    pencilY_change.append(40)

# Create the  pig
pigImg = []
pigX = []
pigY = []
pigX_change = []
pigY_change = []
num_of_pig = 1

for i in range(num_of_pig):
    pigImg.append(pygame.image.load('spaceinvaders/pig.png'))
    pigX.append(random.randint(0, 736))
    pigY.append(random.randint(50, 150))
    pigX_change.append(4)
    pigY_change.append(40)

# Create the Bullet


# Fire - The bullet is currently moving

bulletImg = pygame.image.load('spaceinvaders/bullet.png')
bulletX = 0
bulletY = 300
bulletX_change = 0
bulletY_change = 10

# Ready - You can't see the bullet on the screen
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def banana(x, y, i):
    screen.blit(bananaImg[i], (x, y))


def strawberry(x, y, i):
    screen.blit(strawberryImg[i], (x, y))


def pencil(x, y, i):
    screen.blit(pencilImg[i], (x, y))


def pig(x, y, i):
    screen.blit(pigImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10 ))
    print("fireee")


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def isCollision1(bananaX, bananaY, bulletX, bulletY):
    distance1 = math.sqrt(math.pow(bananaX - bulletX, 2) + (math.pow(bananaY - bulletY, 2)))
    if distance1 < 27:
        return True
    else:
        return False


def isCollision2(strawberryX, strawberryY, bulletX, bulletY):
    distance2 = math.sqrt(math.pow(strawberryX - bulletX, 2) + (math.pow(strawberryY - bulletY, 2)))
    if distance2 < 27:
        return True
    else:
        return False


def isCollision3(pencilX, pencilY, bulletX, bulletY):
    distance3 = math.sqrt(math.pow(pencilX - bulletX, 2) + (math.pow(pencilY - bulletY, 2)))
    if distance3 < 27:
        return True
    else:
        return False


def isCollision4(pigX, pigY, bulletX, bulletY):
    distance4 = math.sqrt(math.pow(pigX - bulletX, 2) + (math.pow(pigY - bulletY, 2)))
    if distance4 < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":

                    bulletSound = mixer.Sound("spaceinvaders/laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("spaceinvaders/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        # Banana Movement
    for i in range(num_of_banana):

        # Game Over
        if bananaY[i] > 440:
            for j in range(num_of_banana):
                bananaY[j] = 2000
            game_over_text()
            break

        bananaX[i] += bananaX_change[i]
        if bananaX[i] <= 0:
            bananaX_change[i] = 4
            bananaY[i] += bananaY_change[i]
        elif bananaX[i] >= 736:
            bananaX_change[i] = -4
            bananaY[i] += bananaY_change[i]

            # Collision
        collision1 = isCollision1(bananaX[i], bananaY[i], bulletX, bulletY)
        if collision1:
            explosionSound = mixer.Sound("spaceinvaders/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            bananaX[i] = random.randint(0, 736)
            bananaY[i] = random.randint(50, 150)

        banana(bananaX[i], bananaY[i], i)

        # strawberry Movement
    for i in range(num_of_strawberry):

        # Game Over
        if strawberryY[i] > 440:
            for j in range(num_of_strawberry):
                strawberryY[j] = 2000
            game_over_text()
            break

        strawberryX[i] = strawberryX_change[i] + strawberryX[i]
        if strawberryX[i] <= 0:
            strawberryX_change[i] = 4
            strawberryY[i] += strawberryY_change[i]
        elif strawberryX[i] >= 736:
            strawberryX_change[i] = -4
            strawberryY[i] += strawberryY_change[i]

            # Collision
        collision2 = isCollision2(strawberryX[i], strawberryY[i], bulletX, bulletY)
        if collision2:
            explosionSound = mixer.Sound("spaceinvaders/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            strawberryX[i] = random.randint(0, 736)
            strawberryY[i] = random.randint(50, 150)

        strawberry(strawberryX[i], strawberryY[i], i)

        # pencil Movement
    for i in range(num_of_pencil):

        # Game Over
        if pencilY[i] > 440:
            for j in range(num_of_pencil):
                pencilY[j] = 2000
            game_over_text()
            break

        pencilX[i] = pencilX_change[i] + pencilX[i]
        if pencilX[i] <= 0:
            pencilX_change[i] = 4
            pencilY[i] += pencilY_change[i]
        elif pencilX[i] >= 736:
            pencilX_change[i] = -4
            pencilY[i] += pencilY_change[i]

            # Collision
        collision3 = isCollision3(pencilX[i], pencilY[i], bulletX, bulletY)
        if collision3:
            explosionSound = mixer.Sound("spaceinvaders/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += -1
            pencilX[i] = random.randint(0, 736)
            pencilY[i] = random.randint(50, 150)

        pencil(pencilX[i], pencilY[i], i)

        # pencil Movement
    for i in range(num_of_pig):

        # Game Over
        if pencilY[i] > 440:
            for j in range(num_of_pig):
                pencilY[j] = 2000
            game_over_text()
            break

        pigX[i] = pigX_change[i] + pigX[i]
        if pigX[i] <= 0:
            pigX_change[i] = 4
            pigY[i] += pigY_change[i]
        elif pigX[i] >= 736:
            pigX_change[i] = -4
            pigY[i] += pigY_change[i]

            # Collision
        collision4 = isCollision4(pigX[i], pigY[i], bulletX, bulletY)
        if collision4:
            explosionSound = mixer.Sound("spaceinvaders/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += -1
            pigX[i] = random.randint(0, 736)
            pigY[i] = random.randint(50, 150)

        pig(pigX[i], pigY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 380
        bullet_state = "ready"

    if bullet_state is "fire":
        bulletY -= bulletY_change
        fire_bullet(bulletX, bulletY)

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()

pygame.quit()
