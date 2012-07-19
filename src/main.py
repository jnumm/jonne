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

# The following line is not needed if pgu is installed.
import sys; sys.path.insert(0, "..")

from pgu import gui

class Game:
    """Jonne game class
    """

    size = width, height = 640, 400

    def __init__(self):
        """Initialization of the game
        """
        pygame.init()

        self.display = None
        self.mouse_pos = [0, 0]

        self.character_data = [100, 100, 0]
        self.health = 10
        self.box_data = [3, 300, 600]

        self.credits = "Tuomas Numminen & Juhani Numminen"

        self.start_image = pygame.image.load("../gfx/start.png")
        self.start_image2 = pygame.image.load("../gfx/start2.png")

        self.box_image = pygame.image.load("../gfx/poison.png")

        self.background = pygame.image.load("../gfx/clouds.png")
        self.background2 = pygame.image.load("../gfx/ground.png")
        self.background_position = 0
        self.background_position2 = 0

        self.character = pygame.image.load("../gfx/guy.png")

        self.menu = [[self.start_image, self.start_image2]]

        self.clock = pygame.time.Clock()

        self.font_normal = pygame.font.Font(None, 24)

    def ask_name(self):
        # Fill the screen with white.
        self.display.fill((255, 255, 255))

        app = gui.App()

        table = gui.Table()

        table.tr()
        table.td(gui.Label("Your name "))
        name_input = gui.Input()
        table.td(name_input)

        table.tr()
        ok_button = gui.Button("OK")
        ok_button.connect(gui.CLICK, app.quit)
        table.td(ok_button)

        app.init(widget=table, screen=self.display)
        app.connect(gui.QUIT, quit, None)
        app.run()

        return name_input.value

    def draw_menu(self):
        """Draw a menu
        """

        self.display.fill((250, 250, 250))

        active_image = -1
        image_index = 0

        position = [261, 50]
        for image_pair in self.menu:
            self.display.blit(image_pair[0], position)
            if self.mouse_pos[0] > 261 and self.mouse_pos[0] < 320:
                if self.mouse_pos[1] > 50 and self.mouse_pos[1] < 102:
                    self.display.blit(image_pair[1], position)
                    active_image = image_index

        image_index += 1

        pygame.display.flip()
        return active_image

    def draw_game(self):

        self.display.fill((0, 0, 0))

        self.display.blit(self.background, (self.background_position, 0))
        self.display.blit(self.background, (self.background_position - self.background.get_width(), 0))

        text = self.font_normal.render("Health: " + str(self.health), True, (255, 0, 0))
        self.display.blit(text, (0, 0))


        self.display.blit(self.background2, (self.background_position2, 200))
        self.display.blit(self.background2, (self.background_position2 - self.background2.get_width(), 200))
        # Let's move the boxes.
        for box_x in self.box_data:
            self.display.blit(self.box_image, (box_x, 350))

        # Update Fps to the titlebar.
        pygame.display.set_caption("FPS: " + str(random.randint(60, 80)))


        self.display.blit(self.character, (self.character_data[0], self.character_data[1]))

        pygame.display.flip()

    def control(self):
        """Game control handling function

        This is called from a loop.
        """

        true = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.character_data[0] += 5

        if keys[pygame.K_LEFT]:
            self.character_data[0] -= 5

        if self.character_data[1] == 155 and keys[pygame.K_SPACE]:
            self.character_data[2] = 1

        if self.character_data[2] == 1:
            # If we are jumping, go up.
            self.character_data[1] -= 5
        else:
            # If we are not jumping, go down.
            if self.character_data[1] < 155:
                self.character_data[1] += 5

        # If we are too high, stop jumping.
        if self.character_data[2] == 1 and self.character_data[1] < 45:
            self.character_data[2] = 0

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

    def update_fps(self):
        # Update the FPS to the title bar.
        pygame.display.set_caption("Fps: " + str(random.randint(60, 80)))

                            # (x, y)                                         (x,y)
    def point_inside_character(self, character_position, character_width, character_height, point):
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
    def hit(self, character1_position, character1, character2_position, character2):
        if self.point_inside_character(character1_position, character1.get_width(), character1.get_height(), character2_position):
            return True
        if self.point_inside_character(character1_position, character1.get_width(),
                character1.get_height(), (character2_position[0], character2_position[1] + character2.get_height())):
            return True
        if self.point_inside_character(character1_position, character1.get_width(),
                character1.get_height(), (character2_position[0] + character2.get_width(), character2_position[1])):
            return True
        if self.point_inside_character(character1_position, character1.get_width(),
                character1.get_height(), (character2_position[0] + character2.get_width(), character2_position[1] + character2.get_height())):
            return True

        return False

    def run(self):
        self.display = pygame.display.set_mode(self.size,
                pygame.HWSURFACE | pygame.DOUBLEBUF)

        try:
            f = open("../hiscore.txt","r")
            self.best_point = int(f.readline())
            self.best_name = f.readline()
            f.close()
        except (IOError, ValueError):
            f = open("../hiscore.txt","w")
            f.write("0")
            f.close()

            self.best_point = 0
            self.best_name = ""

        name = self.ask_name()

        ## Game start: menu
        show_menu = True
        while show_menu:
            key_pressed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    key_pressed = True

            self.update_fps()

            active_image = self.draw_menu()

            if key_pressed and active_image > -1:
                show_menu = False
                break

        touches = 0

        start_time = time.clock()

        # Game while
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.control()

            # Gamelogic
            self.background_position -= 1
            self.background_position2 -= 5
            self.background_position %= 640
            self.background_position2 %= 640

            for index in range(len(self.box_data)):
                self.box_data[index] = self.box_data[index] - 7
                if self.box_data[index] < -200:
                    self.box_data[index] = 900

            # touch
            does_hit = 0
            for index in range(len(self.box_data)):
                if self.hit(self.character_data, self.character, (self.box_data[index], 350), self.box_image):
                    does_hit = 1

            if does_hit == 1 and touches == 0:
                touches = 1
                self.health -= 1

            if does_hit == 0:
                touches = 0

            self.draw_game()

            self.clock.tick(40)

            if self.health == 0:
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break

        self.elapsed_time = int(round(time.clock() - start_time))

        if self.elapsed_time > self.best_point:
            file2 = open("../hiscore.txt", "w")
            file2.write(str(self.elapsed_time) + "\n" )
            file2.write(self.name)
            file2.close()

            text = self.font_normal.render("Time: " + str(self.elapsed_time), True, (255, 0, 0))
            text2 = self.font_normal.render("##### NEW RECORD #####",True,(50, 255, 0))
            text3 = self.font_normal.render("Previous record: "  + str(self.best_point) + "s", True, (255, 0, 0))
            text4 = self.font_normal.render("Made by: " + self.best_name, True, (255, 0, 0))
            text5 = self.font_normal.render("This game is made by " + self.credits, True, (255, 0, 0))
        else:
            text = self.font_normal.render("Time: " + str(self.elapsed_time), True, (255, 0, 0))
            text2 = self.font_normal.render("##### NO NEW RECORD #####", True, (255, 0, 0))
            text3 = self.font_normal.render("Current record: " + str(self.best_point) + "s", True, (255, 0, 0))
            text4 = self.font_normal.render("Made by: " + self.best_name, True, (255, 0, 0))
            text5 = self.font_normal.render("This game is made by " + self.credits, True, (255, 0, 0))

        #END While
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.update_fps()

            self.display.fill((0, 0, 0))

            self.display.blit(text, (5, 0))
            self.display.blit(text2, (5, 50))
            self.display.blit(text3, (5, 100))
            self.display.blit(text4, (5, 125))
            self.display.blit(text5, (5, 170))

            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
