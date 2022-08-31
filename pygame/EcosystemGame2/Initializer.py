import pickle
import pygame
import sys
import math
from Window.WindowClass import Window

pygame.init()

print("Enter a positive number to load past save or 0 to create new simulation: ")
input = int(input())

if input>0:
    with open("EcoOutputData","rb") as file:
        window = pickle.load(file)
else:
    window = Window()

clock = pygame.time.Clock()

display = pygame.display.set_mode((1200,700))
display.fill((255,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            window.gui.update(pygame.mouse.get_pos(),display,window)

    keys = pygame.key.get_pressed()

    movement = [0,0]

    if keys[pygame.K_a]:
        movement[0] +=5
    if keys[pygame.K_d]:
        movement[0] -=5
    if keys[pygame.K_w]:
        movement[1] +=5
    if keys[pygame.K_s]:
        movement[1] -=5


    window.updateDisplay(movement,display)
    clock.tick(60)
