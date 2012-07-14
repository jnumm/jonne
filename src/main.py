#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012, Tuomas Numminen
# Copyright (C) 2012, Juhani Numminen
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
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

def piirraPeli(piirtoikkuna, pelihahmo, sijainti, tausta, tausta_sijainti, elama ,tausta2, tausta_sijainti2):
	
    piirtoikkuna.fill((0, 0, 0))
    
    piirtoikkuna.blit(tausta, (tausta_sijainti,0))
    piirtoikkuna.blit(tausta, (tausta_sijainti - tausta.get_width(),0))
    
    fontti = pygame.font.Font(None, 24)
    teksti = fontti.render("Health: " + str(elama), True, (255,0,0))
    naytto.blit(teksti, (0,0))
	     
    
    piirtoikkuna.blit(tausta2, (tausta_sijainti2,200))
    piirtoikkuna.blit(tausta2, (tausta_sijainti2 - tausta2.get_width(),200))
    # Let's move the boxes. 
    for laatikko_x in laatikko:
        piirtoikkuna.blit(laatikko1, (laatikko_x,350))
        
    # Update Fps to the titlebar.
    pygame.display.set_caption("FPS: " + str(random.randint(60, 80)))
        
    
    piirtoikkuna.blit(pelihahmo, sijainti)
   
    pygame.display.flip()                         
    
def ohjaus(sijainti):    
    #sijainti[0] = 2;
    #sijainti[1] = 5;
    true = True
    
    napit=pygame.key.get_pressed()
    if napit[pygame.K_RIGHT]:
    
        sijainti[0]=sijainti[0]+5
    if napit[pygame.K_LEFT]:
        sijainti[0]=sijainti[0]-5

    if sijainti[1]==155  and napit[pygame.K_SPACE]: 
        sijainti[2]=1

    if sijainti[2]==1:
        # If we are jumping, go up.
        sijainti[1]=sijainti[1]-5
    else: 
        # If we are not jumping, go down.
        if sijainti[1] < 155:
            sijainti[1]=sijainti[1]+5
            
    # If we are too high, stop jumping.
    if sijainti[2]==1 and sijainti[1]<45:
        sijainti[2]=0
    
    if napit[pygame.K_p]:
        print "P pantu!"
        while true:
            print "pausel'"
            napit = pygame.key.get_pressed()
            if napit[pygame.K_a]:
                print "exittaa"
                break
            break 
        print "ny pitäs jatkuu..."

def paivita_fps():
    # Update the FPS to the title bar.
    pygame.display.set_caption("Fps: " + str(random.randint(60, 80)))
    
                        # (x, y)                                         (x,y)
def piste_hahmon_sisalla(hahmon_sijainti, hahmon_leveys, hahmon_korkeus, piste):
    if hahmon_sijainti[0] > piste[0]:
        return False
    elif hahmon_sijainti[0] + hahmon_leveys < piste[0]:
        return False
    elif hahmon_sijainti[1] > piste[1]:
        return False
    elif hahmon_sijainti[1] + hahmon_korkeus < piste[1]:
        return False
    else:
		return True

         # (x, y)         kuva    (x, y)          kuva      
def isku(hahmo1_sijainti, hahmo1, hahmo2_sijainti, hahmo2):
    if piste_hahmon_sisalla(hahmo1_sijainti, hahmo1.get_width(), hahmo1.get_height(), hahmo2_sijainti):
        return True
    if piste_hahmon_sisalla(hahmo1_sijainti, hahmo1.get_width(), hahmo1.get_height(), (hahmo2_sijainti[0], hahmo2_sijainti[1] + hahmo2.get_height())):
		return True
    if piste_hahmon_sisalla(hahmo1_sijainti, hahmo1.get_width(), hahmo1.get_height(), (hahmo2_sijainti[0] + hahmo2.get_width(), hahmo2_sijainti[1])):
		return True
    if piste_hahmon_sisalla(hahmo1_sijainti, hahmo1.get_width(), hahmo1.get_height(), (hahmo2_sijainti[0] + hahmo2.get_width(), hahmo2_sijainti[1] + hahmo2.get_height())):
		return True

    return False

##  Load images
naytto = pygame.display.set_mode((640, 400))
                #  x    y  hyppaa
hahmon_tiedot = [100, 100, 0]
#x = 100
#y = 100

nopeus = 10

tekijat = "Tuomas Numminen & Juhani Numminen"

xliike = nopeus
yliike = nopeus

alku_kuva = pygame.image.load("../gfx/alku.png")
alku_kuva2 = pygame.image.load("../gfx/alku2.png")

laatikko1 = pygame.image.load("../gfx/toxin.png")

laatikko = [3,300,600]

tiedosto = open("../hiscore.txt","r")
paras_piste = int(tiedosto.readline())
paras_nimi = tiedosto.readline()
tiedosto.close()

menu = []
menu.append((alku_kuva, alku_kuva2))

tausta2 = pygame.image.load("../gfx/test13.png")
tausta = pygame.image.load("../gfx/test12.png")
tausta_sijainti = 0
tausta_sijainti2 = 0

ukko = pygame.image.load("../gfx/face2.png")

hiiri = [0,0]

kello = pygame.time.Clock()

nimi = raw_input ("Your nickname: ")

## Game start: menu
naytetaanMenu = True
while naytetaanMenu:
    nappiaPainettu = False
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.MOUSEMOTION:
			hiiri=tapahtuma.pos
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            nappiaPainettu = True 
    
    paivita_fps()
    
    aktiivinenKuva = draw_menu(naytto, menu, hiiri)
    
    if nappiaPainettu and aktiivinenKuva > -1:
		naytetaanMenu = False
		break

koskettaako = 0

elama = 10
aloitus_aika = time.clock()

# Game while
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    ohjaus(hahmon_tiedot)
    #print hahmon_tiedot
    
    # Gamelogic
    tausta_sijainti = tausta_sijainti - 1
    tausta_sijainti2 = tausta_sijainti2 - 5
    #print "taustan sijainti", tausta_sijainti, "ja taustan leveys", tausta.get_width()
    tausta_sijainti = tausta_sijainti % 640
    tausta_sijainti2 = tausta_sijainti2 % 640
    
    for indeksi in range(len(laatikko)):
		laatikko[indeksi] = laatikko[indeksi] - 7 
		if laatikko[indeksi]<-200:
			laatikko[indeksi] = 900
	
	# touch
    osui = 0
    for indeksi in range(len(laatikko)):
        if isku(hahmon_tiedot, ukko, (laatikko[indeksi], 350), laatikko1):
            osui = 1
		 
    if osui == 1 and koskettaako == 0:
        koskettaako = 1
        elama=elama-1
    
    if osui == 0:
        koskettaako = 0
               #              x                 y
    sijainti = (hahmon_tiedot[0], hahmon_tiedot[1])
    piirraPeli(naytto, ukko, sijainti, tausta, tausta_sijainti, elama ,tausta2, tausta_sijainti2)

    kello.tick(40)
    if elama == 0:
		break
    
    if tapahtuma.type == pygame.KEYDOWN:
		if tapahtuma.key == pygame.K_ESCAPE:
			break 
    
        

mennyt_aika = int(round(time.clock() - aloitus_aika))
fontti = pygame.font.Font(None, 24) 

if mennyt_aika > paras_piste:
    tiedosto2 = open("../hiscore.txt", "w")
    tiedosto2.write(str(mennyt_aika) + "\n" )
    tiedosto2.write (nimi)
    tiedosto2.close()
    
    teksti = fontti.render("Time: " + str(mennyt_aika) + " s      This game is made by " + tekijat, True, (255,0,0))
    teksti2 = fontti.render("##### NEW RECORD #####",True,(50,255,0))
    teksti3 = fontti.render("Previous record: "  + str(paras_piste) + "s", True, (255,0,0))
    teksti4 = fontti.render("Made by: " + paras_nimi, True, (255,0,0))
else:    
    teksti = fontti.render("Time: " + str(mennyt_aika) + " s      This game is made by " + tekijat, True, (255,0,0))
    teksti2 = fontti.render("##### NO NEW RECORD #####" + "s", True, (255,0,0))
    teksti3 = fontti.render("Current record: " + str(paras_piste) + "s", True, (255,0,0))
    teksti4 = fontti.render("Made by: " + paras_nimi, True, (255,0,0))
#END While
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    paivita_fps()
    
    naytto.fill((0, 0, 0))

    naytto.blit(teksti, (0,0))
    naytto.blit(teksti2, (0,50))
    naytto.blit(teksti3, (0,100))
    naytto.blit(teksti4, (0,125))
    
    pygame.display.flip()   
            
