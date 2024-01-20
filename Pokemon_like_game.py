
# Modification date: Sat Dec 25 22:55:20 2021

# Production date: Sun Sep  3 15:43:57 2023

import random
import pygame
import pokemon
import button
from ability import Ability


# Initialize the pygame
pygame.init()

# Create the screen(width, height)
win = pygame.display.set_mode((800, 600))

# Background
Battlefield_Background = pygame.image.load("Battlefield_Background.png")

# Title and icon
pygame.display.set_caption("Pokemon Like Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


#buttons
#normal
punch_option = pygame.image.load(r'normal\abilities\punch\punch_option.png')
#fire
flying_match_option = pygame.image.load(r'fire\abilities\flying_match\flying_match_option.png')


#abilities
#normal
punch_ability = Ability("punch", 30, "normal")
#fire
flying_match_ability = Ability("flying_match", 40, "fire")


#name = input("Enter your name: ")
name = "Emirhan"
Player = pokemon.Pokemon(name, "Sphirit","ally")
Enemy = pokemon.Pokemon("Enemy", "Sphirit", "enemy")
flying_match_option_button = button.Button(400, 480, flying_match_option, 1)
punch_option_button = button.Button(400, 430, punch_option, 1)


def redrawGameWindow():
    win.blit(Battlefield_Background, (0,0))
    Player.draw(win)
    Enemy.draw(win)

def ability_used(button, ability, place, counter, being_used, counter2, Enemy):
    Enemy.hurt = being_used
    if button.draw(win):
        #print("counter", counter)
        if not being_used:
            Enemy.hurt = False
        #if counter % 2 == 0:
        Enemy.hurt = True
        being_used = True
        counter = 1
        #print("counter %2")
        #else:
        #    Enemy.hurt = False
        #    being_used = False
    if being_used:
        print(being_used, Enemy.hurt, "---")
        print(counter2)
        if counter2 > 14:
            counter2 = 0
            being_used = False
            Enemy.hurt = False
            print("geçti")
            #counter = 0
        else:
            being_used = ability.draw_ability(win, place, being_used)
            #print(button, ability, place, counter, being_used, counter2, Enemy)
            counter2 += 1
            print("counter + 1")
    print(being_used, Enemy.hurt)
    
    return [counter, being_used, counter2]


counter0 = 0
counter02 = 0
used0 = False
ability_an_list = [counter0, used0, counter02]
counter1 = 0
counter12 = 0
used1 = False
ability_an_list2 = [counter1, used1, counter12]
ability_an_counter = 0
#game loop
running = True
while running:
    clock.tick(30)
	#win.fill((202, 228, 241))

    #event handler
    for event in pygame.event.get():
		#quit game
        if event.type == pygame.QUIT:
            running = False
    redrawGameWindow()


    ability_an_list = ability_used(flying_match_option_button, flying_match_ability, "ally", ability_an_list[0], ability_an_list[1], ability_an_list[2], Enemy)

    ability_an_list2 = ability_used(punch_option_button, punch_ability, "ally", ability_an_list2[0], ability_an_list2[1], ability_an_list2[2], Enemy)

    """
    if flying_match_option_button.draw(win):
        new_counter += 1
        if new_counter % 2 == 0:
            Enemy.hurt = True
            flying_match_ability.draw_ability(win, "ally")
        else:
            Enemy.hurt = False
    if punch_option_button.draw(win):
        new_counter += 1
        if new_counter % 2 == 0:
            Enemy.hurt = True
            punch_ability.draw_ability(win, "ally")
        else:
            Enemy.hurt = False
	"""
    pygame.display.update()

pygame.quit()


#winner = Player.combat(Enemy)
#input(str(winner) + " Won!")
