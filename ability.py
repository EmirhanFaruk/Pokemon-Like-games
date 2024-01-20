
# Modification date: Sat Dec 25 22:01:24 2021

# Production date: Sun Sep  3 15:43:57 2023

import pygame

#normal abilities
punch_animations = [pygame.image.load(r'normal\abilities\punch\punch_1.png'), pygame.image.load(r'normal\abilities\punch\punch_2.png'), pygame.image.load(r'normal\abilities\punch\punch_3.png')]
#kick_animations = [pygame.image.load(r'normal\abilities\kick_1.png'), pygame.image.load(r'normal\abilities\kick_2.png'), pygame.image.load(r'normal\abilities\kick_3.png')]
#fire abilities
#f = pygame.image.load(r'fire\abilities\flying_match_1.png')
flying_match_animations = [pygame.image.load(r'fire\abilities\flying_match\flying_match_1.png'), pygame.image.load(r'fire\abilities\flying_match\flying_match_2.png'), pygame.image.load(r'fire\abilities\flying_match\flying_match_3.png')]

#water abilities
#strong_spit_animations = [pygame.image.load(r'water\abilities\strong_spit_1.png'), pygame.image.load(r'water\abilities\strong_spit_2.png'), pygame.image.load(r'water\abilities\strong_spit_3.png')]
#grass abilities
#thornbush_animations = [pygame.image.load(r'grass\abilities\thornbush_1.png'), pygame.image.load(r'grass\abilities\thornbush_2.png'), pygame.image.load(r'grass\abilities\thornbush_3.png')]


class Ability:
    def __init__(self, name, damage, element):
        self.damage = damage
        self.element = element
        self.counting = 0
        self.name = name
        self.used = False
        self.pokemonabilityanimations_dict = {"punch": punch_animations, "flying_match": flying_match_animations}
        self.abilityanimations = self.pokemonabilityanimations_dict[name]
    
    def draw_ability(self, win, user, used = True):
        self.used = used
        #print(self.used)
        print(self.counting, self.used)
        if self.counting >= 14:
            self.counting = 0
            print("self.counting = 0")
            self.used = False
            return self.used
        else:
            if self.used:
                if user == "ally":
                    win.blit(self.abilityanimations[self.counting//5], (585, 80))
                else:
                    win.blit(self.abilityanimations[self.counting//5], (95, 250))
                #print(self.counting)
                self.counting += 1
                return self.used

"""
def draw(self, win):
        if self.counting > 17:
            self.counting = 0
        if self.place == "ally":
            if self.hurt:
                win.blit(self.pokemonanimations[1], (95, 250))
            else:
                win.blit(self.pokemonanimations[0][self.counting//6], (95, 250))
        else:
            if self.hurt:
                win.blit(self.pokemonanimations[1], (585, 80))
            else:
                win.blit(self.pokemonanimations[0][self.counting//6], (585, 80))
        #print(self.counting)
        self.counting += 1
"""