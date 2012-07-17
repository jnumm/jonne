#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012, Tuomas Numminen
# Copyright (C) 2012, Juhani Numminen
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pygame
import random
import time

pygame.font.init()


# The functions of the game.

def draw_menu(window, image_list, mouse_pos):
               # r    g    b
    window.fill((250, 250, 250))

    active_image = -1
    image_index = 0

    position = [261,50]
    for image_pair in image_list:
        window.blit(image_pair[0], position)
        if mouse_pos[0] > 261 and mouse_pos[0] < 320:
            if mouse_pos[1] > 50 and mouse_pos[1]<102:
                window.blit(image_pair[1], position)
                active_image = image_index

    image_index =+ 1

    pygame.display.flip()
    return active_image

def draw_game(draw_window, character, position, background, background_position, health, background2, background_position2):

    draw_window.fill((0, 0, 0))

    draw_window.blit(background, (background_position,0))
    draw_window.blit(background, (background_position - background.get_width(),0))

    font = pygame.font.Font(None, 24)
    text = font.render("Health: " + str(health), True, (255,0,0))
    display.blit(text, (0,0))


    draw_window.blit(background2, (background_position2,200))
    draw_window.blit(background2, (background_position2 - background2.get_width(),200))
    # Let's move the boxes.
    for box_x in box:
        draw_window.blit(box1, (box_x,350))

    # Update Fps to the titlebar.
    pygame.display.set_caption("FPS: " + str(random.randint(60, 80)))


    draw_window.blit(character, position)

    pygame.display.flip()

def control(position):
    #position[0] = 2;
    #position[1] = 5;
    true = True

    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:

        position[0]=position[0]+5
    if keys[pygame.K_LEFT]:
        position[0]=position[0]-5

    if position[1]==155  and keys[pygame.K_SPACE]:
        position[2]=1

    if position[2]==1:
        # If we are jumping, go up.
        position[1]=position[1]-5
    else:
        # If we are not jumping, go down.
        if position[1] < 155:
            position[1]=position[1]+5

    # If we are too high, stop jumping.
    if position[2]==1 and position[1]<45:
        position[2]=0

    if keys[pygame.K_p]:
        print "P pantu!"
        while true:
            print "pausel'"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                print "exittaa"
                break
            break
        print "ny pitäs jatkuu..."

def update_fps():
    # Update the FPS to the title bar.
    pygame.display.set_caption("Fps: " + str(random.randint(60, 80)))

                        # (x, y)                                         (x,y)
def point_inside_character(character_position, character_width, character_height, point):
    if character_position[0] > point[0]:
        return False
    elif character_position[0] + character_width < point[0]:
        return False
    elif character_position[1] > point[1]:
        return False
    elif character_position[1] + character_height < point[1]:
        return False
    else:
        return True

         # (x, y)         kuva    (x, y)          kuva
def hit(character1_position, character1, character2_position, character2):
    if point_inside_character(character1_position, character1.get_width(), character1.get_height(), character2_position):
        return True
    if point_inside_character(character1_position, character1.get_width(), character1.get_height(), (character2_position[0], character2_position[1] + character2.get_height())):
        return True
    if point_inside_character(character1_position, character1.get_width(), character1.get_height(), (character2_position[0] + character2.get_width(), character2_position[1])):
        return True
    if point_inside_character(character1_position, character1.get_width(), character1.get_height(), (character2_position[0] + character2.get_width(), character2_position[1] + character2.get_height())):
        return True

    return False

##  Load images
display = pygame.display.set_mode((640, 400))
                #  x    y  hyppaa
character_data = [100, 100, 0]
#x = 100
#y = 100

speed = 10

credits = "Tuomas Numminen & Juhani Numminen"

x_movement = speed
y_movement = speed

start_image = pygame.image.load("../gfx/start.png")
start_image2 = pygame.image.load("../gfx/start2.png")

box1 = pygame.image.load("../gfx/poison.png")

box = [3,300,600]

try:
    file = open("../hiscore.txt","r")
    best_point = int(file.readline())
    best_name = file.readline()
    file.close()
except (IOError, ValueError):
    fileError = open("../hiscore.txt","w")
    fileError.write("0")
    fileError.close()

    best_point = 0
    best_name = ""

menu = []
menu.append((start_image, start_image2))

background2 = pygame.image.load("../gfx/ground.png")
background = pygame.image.load("../gfx/clouds.png")
background_position = 0
background_position2 = 0

character = pygame.image.load("../gfx/guy.png")

mouse = [0,0]

clock = pygame.time.Clock()

name = raw_input ("Your nickname: ")

## Game start: menu
show_menu = True
while show_menu:
    key_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse=event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            key_pressed = True

    update_fps()

    active_image = draw_menu(display, menu, mouse)

    if key_pressed and active_image > -1:
        show_menu = False
        break

touches = 0

health = 10
start_time = time.clock()

# Game while
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    control(character_data)
    #print character_data

    # Gamelogic
    background_position = background_position - 1
    background_position2 = background_position2 - 5
    background_position = background_position % 640
    background_position2 = background_position2 % 640

    for index in range(len(box)):
        box[index] = box[index] - 7
        if box[index]<-200:
            box[index] = 900

    # touch
    does_hit = 0
    for index in range(len(box)):
        if hit(character_data, character, (box[index], 350), box1):
            does_hit = 1

    if does_hit == 1 and touches == 0:
        touches = 1
        health=health-1

    if does_hit == 0:
        touches = 0
               #              x                 y
    position = (character_data[0], character_data[1])
    draw_game(display, character, position, background, background_position, health, background2, background_position2)

    clock.tick(40)
    if health == 0:
        break

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            break



elapsed_time = int(round(time.clock() - start_time))
font = pygame.font.Font(None, 24)

if elapsed_time > best_point:
    file2 = open("../hiscore.txt", "w")
    file2.write(str(elapsed_time) + "\n" )
    file2.write (name)
    file2.close()

    text = font.render("Time: " + str(elapsed_time) + " s      This game is made by " + credits, True, (255,0,0))
    text2 = font.render("##### NEW RECORD #####",True,(50,255,0))
    text3 = font.render("Previous record: "  + str(best_point) + "s", True, (255,0,0))
    text4 = font.render("Made by: " + best_name, True, (255,0,0))
else:
    text = font.render("Time: " + str(elapsed_time) + " s      This game is made by " + credits, True, (255,0,0))
    text2 = font.render("##### NO NEW RECORD #####" + "s", True, (255,0,0))
    text3 = font.render("Current record: " + str(best_point) + "s", True, (255,0,0))
    text4 = font.render("Made by: " + best_name, True, (255,0,0))
#END While
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    update_fps()

    display.fill((0, 0, 0))

    display.blit(text, (0,0))
    display.blit(text2, (0,50))
    display.blit(text3, (0,100))
    display.blit(text4, (0,125))

    pygame.display.flip()

