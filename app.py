#pip install pygame
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("the game worm")

worm = [(100,50)]
direction = (10,0)
food = (300,200)


def draw():
    screen.fill((0,0,0))
    for segment in worm:
        pygame.draw.rect(screen, (0,255,0), (*segment, 10, 10))
    

    pygame.draw.rect(screen, (255,0,0), (*food, 10, 10))
    pygame.display.update()


running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0,-10)
            if event.key == pygame.K_DOWN:
                direction = (0,10)
            if event.key == pygame.K_LEFT:
                direction = (-10,0)
            if event.key == pygame.K_RIGHT:
                direction = (10,0)

    new_head = (worm[0][0] + direction[0], worm[0][1] + direction[1])
    worm.insert(0, new_head)
    
    if new_head == food:
        food = (random.randint(0,59)*10, random.randint(0,39)*10)
    else:
        worm.pop()

    if new_head in worm [1:]:
        print("You ate yourself! Game over.")
        running = False

    if new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 400:
        print("You hit the wall! Game over.")
        running = False

    draw()
    clock.tick(15)


pygame.quit()