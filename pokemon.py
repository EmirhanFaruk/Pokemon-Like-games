
# Modification date: Sat Dec 25 18:29:54 2021

# Production date: Sun Sep  3 15:43:57 2023

import random
import pygame

# The Pokemon Pics
#Pokemon names: normal = {claws, spikes}, fire = {charcoal(bruh thats stupid), Sphirit}, wa'er = {Spit, dirty water}, grass = {literal grass, Leaf}
#normal(?)
#claws_stand = [pygame.image.load(r'normal\claws\claws_stand_1.png'), pygame.image.load(r'normal\claws\claws_stand_2.png'), pygame.image.load(r'normal\claws\claws_stand_3.png')]
#spikes_stand = [pygame.image.load(r'normal\spikes\spikes_stand_1.png'), pygame.image.load(r'normal\spikes\spikes_stand_2.png'), pygame.image.load(r'normal\spikes\spikes_stand_3.png')]
#fire
#charcoal_stand = [pygame.image.load('fire\charcoal\charcoal_stand_1.png'), pygame.image.load(r'fire\charcoal\charcoal_stand_2.png'), pygame.image.load(r'fire\charcoal\charcoal_stand_3.png')]
sphirit_stand = [pygame.image.load(r'fire\sphirit\sphirit_stand_1.png'), pygame.image.load(r'fire\sphirit\sphirit_stand_2.png'), pygame.image.load(r'fire\sphirit\sphirit_stand_3.png')]
#wa'er
#spit_stand = [pygame.image.load(r'water\spit\spit_stand_1.png'), pygame.image.load(r'water\spit\spit_stand_2.png'), pygame.image.load(r'water\spit\spit_stand_3.png')]
#dirty_water_stand = [pygame.image.load(r'water\dirty_water\dirty_water_stand_1.png'), pygame.image.load(r'water\dirty_water\dirty_water_stand_2.png'), pygame.image.load(r'water\dirty_water\dirty_water_stand_3.png')]
#grass
#literal_grass_stand = [pygame.image.load(r'grass\literal_grass\literal_grass_stand_1.png'), pygame.image.load('grass\literal_grass\literal_grass_stand_2.png'), pygame.image.load('grass\literal_grass\literal_grass_stand_3.png')]
#leaf_stand = [pygame.image.load(r'grass\leaf\leaf_stand_1.png'), pygame.image.load('grass\leaf\leaf_stand_2.png'), pygame.image.load('grass\leaf\leaf_stand_3.png')]


# Animations
#normal(?)
#claws_hurt = pygame.image.load(r'normal\claws\claws_hurt.png')
#spikes_hurt = pygame.image.load(r'normal\spikes\spikes_hurt.png')
#fire
#burning_coal_hurt = pygame.image.load(r'fire\charcoal\charcoal_hurt.png')
sphirit_stand_hurt = pygame.image.load(r'fire\sphirit\sphirit_hurt.png')
#wa'er
#spit_hurt = pygame.image.load(r'water\spit\spit_hurt.png')
#dirty_water_hurt = pygame.image.load(r'water\dirty_water\dirty_water_hurt.png')
#grass
#literal_grass_hurt = pygame.image.load(r'grass\literal_grass\literal_grass_hurt.png')
#leaf_hurt = pygame.image.load(r'grass\leaf\leaf_hurt.png')








class Pokemon:
    def __init__(self, name, pokemontype = "random", place = "enemy"):
        #pokemon properties etc
        self.name = name
        self.health = random.randint(200, 401)
        self.place = place
        self.hurt = False
        self.counting = 0








        #self.crit_hurt = False
        #getting random element/getting the wanted pokemon
        self.pokemontype_dict = {"Claws": "normal", "Spikes": "normal", "Charcoal": "fire", "Sphirit": "fire", "Spit": "water", "Dirty water": "water", "Literal grass": "grass", "Leaf": "grass"}
        self.pokemontype = pokemontype
        if self.pokemontype == "random" or not pokemontype in self.pokemontype_dict.keys():
            self.pokemontype = random.choice(self.pokemontype_dict.keys())
            self.element = self.pokemontype_dict[pokemontype]       
        else:
            self.element = self.pokemontype_dict[self.pokemontype]
        #print(self.element)
        #getting the abilities
        self.abilities = [["Punch", 30, "normal", ""]]#[attack_name, damage, element, strong or not(for the bots)]
        self.normal_abilities = [["Kick", 40, "normal", ""]]
        self.fire_abilities = [["Flying match", 40, "fire", ""]]
        self.water_abilities = [["Strong spit", 40, "water", ""]]
        self.grass_abilities = [["Thornbush", 40, "grass", ""]]
        self.all_abilities = [self.normal_abilities, self.fire_abilities, self.water_abilities, self.grass_abilities]


        #giving the pokemon a new ability
        if self.element == "normal":
            self.abilities.append(random.choice(self.all_abilities[0]))
        elif self.element == "water":
            self.abilities.append(random.choice(self.all_abilities[2]))
        elif self.element == "grass":
            self.abilities.append(random.choice(self.all_abilities[3]))
        elif self.element == "fire":
            self.abilities.append(random.choice(self.all_abilities[1]))

        #getting the animations
        self.pokemonanimations_dict = {"Claws": "normal", "Spikes": "normal", "Charcoal": "fire", "Sphirit": [sphirit_stand, sphirit_stand_hurt], "Spit": "water", "Dirty water": "water", "Literal grass": "grass", "Leaf": "grass"}
        

        for pokemon in self.pokemonanimations_dict.keys():
            if self.pokemontype == pokemon:
                self.pokemonanimations = self.pokemonanimations_dict[pokemon]

    
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


    #def p_attack(self, other)

        

"""
class Pokemon:
    def __init__(self, name, pokemontype = "random", place = "enemy"):
        #pokemon properties
        self.name = name
        self.health = random.randint(100, 201)
        self.place = place
        self.hurt = False
        #self.crit_hurt = False
        #getting random element/getting the wanted pokemon
        self.pokemontype_dict = {"Claws": "normal", "Spikes": "normal", "Charcoal": "fire", "Sphirit": "fire", "Spit": "water", "Dirty water": "water", "Literal grass": "grass", "Leaf": "grass"}
        self.pokemontype = pokemontype
        if self.pokemontype == "random" or not pokemontype in self.pokemontype_dict.keys():
            self.pokemontype = random.choice(self.pokemontype_dict.keys())
            self.element = self.pokemontype_dict[pokemontype]       
        else:
            self.element = self.pokemontype_dict[self.pokemontype]
        print(self.element)
        #getting the abilities
        self.abilities = [["Punch", 30, "normal", ""]]#[attack_name, damage, element, strong or not(for the bots)]
        self.normal_abilities = [["Kick", 40, "normal", ""]]
        self.fire_abilities = [["Flying match", 40, "fire", ""]]
        self.water_abilities = [["Strong spit", 40, "water", ""]]
        self.grass_abilities = [["Thornbush", 40, "grass", ""]]
        self.all_abilities = [self.normal_abilities, self.fire_abilities, self.water_abilities, self.grass_abilities]


        #giving the pokemon a new ability
        if self.element == "normal":
            self.abilities.append(random.choice(self.all_abilities[0]))
        elif self.element == "water":
            self.abilities.append(random.choice(self.all_abilities[2]))
        elif self.element == "grass":
            self.abilities.append(random.choice(self.all_abilities[3]))
        elif self.element == "fire":
            self.abilities.append(random.choice(self.all_abilities[1]))
    
        #getting the animations
        self.pokemonanimations_dict = {"Claws": "normal", "Spikes": "normal", "Charcoal": "fire", "Sphirit": [sphirit_stand, sphirit_stand_hurt], "Spit": "water", "Dirty water": "water", "Literal grass": "grass", "Leaf": "grass"}
        self.pokemonabilityanimations_dict = {"punch": punch_animations, "flying_match": flying_match_animations}

        for pokemon in self.pokemonanimations_dict.keys():
            if self.pokemontype == pokemon:
                self.pokemonanimations = self.pokemonanimations_dict[pokemon]




    #Combat        
    def combat(self, other):
        while other.health > 0 or self.health > 0:
            #printing situation containing healths etc
            print("\n" + (str(other.name) + " " + str(other.health) + " " + str(other.element) + "\n" + str(self.name) + " " + str(self.health) + " " + str(self.element) + "\nWhat ability are you going to use?"))
            ab_len1 = len(self.abilities)
            ab_num_list = []
            for i in range(ab_len1):#printing abilities
                ab_num_list.append(i + 1)
                print(i + 1, str(self.abilities[i][0]))
            self.choice = 0
            while self.choice == 0:#getting and making sure self.choice is a number from the abilities
                try:
                    self.choice = int(input("\n: "))
                    if not self.choice in ab_num_list:
                        continue
                except:
                    print("Please choose a number from the ability list.")
                    self.choice = 0
                    continue
            #damage calculation, if its gonna be effective or not
            sentence = ""
            self.choice -= 1
            if self.choice < 0:
                self.choice = 0
            elif self.choice > len(self.abilities) - 1:
                self.choice = len(self.abilities) - 1
                
            if (self.abilities[self.choice][2] == "fire" and other.element == "grass") or (self.abilities[int(self.choice)][2] == "water" and other.element == "fire") or (self.abilities[int(self.choice)][2] == "grass" and other.element == "water"):
                attack1 = self.abilities[self.choice][1] * 2
                sentence = "It\'s very effective!"
            elif (self.abilities[self.choice][2] == "grass" and other.element == "fire") or (self.abilities[int(self.choice)][2] == "fire" and other.element == "water") or (self.abilities[int(self.choice)][2] == "water" and other.element == "grass"):
                attack1 = self.abilities[self.choice][1] // 2
                sentence = "It\'s not very effective."
            else:
                attack1 = self.abilities[self.choice][1]

            #attacking the enemy
            print(f"{self.name} is attacking with the move {self.abilities[self.choice][0]}! {sentence}\n{other.health} - {attack1} = {other.health - attack1}\n")
            other.health -= attack1
            if other.health <= 0:
                return self.name

            #enemy attack ai(?)
            attackp = []
            for i in range(len(other.abilities)):
                if other.abilities[i][3] == "strong":
                    attackp.append(i)
                elif other.abilities[i][3] == "":#this elif and the other one is useless
                    continue
                elif other.abilities[i][3] == "weak":
                    continue
            #comparing attacks(which is kind of useless bc there is only 1 ability other than the punch)
            suggested_attack = 0
            if len(attackp) > 0:
                for i in range(len(attackp)):
                    last_attack = attackp[i]#its not the last ability that was used by the bot, its just for the loop
                    if other.abilities[suggested_attack][3] == "weak":
                        suggested_attack_damage = other.abilities[suggested_attack][1] // 2
                    elif other.abilities[suggested_attack][3] == "strong":
                        suggested_attack_damage = other.abilities[suggested_attack][1] * 2
                    else:
                        suggested_attack_damage = other.abilities[suggested_attack][1]
                    
                    if other.abilities[last_attack][3] == "weak":
                        last_attack_damage = other.abilities[last_attack][1] // 2
                    elif other.abilities[last_attack][3] == "strong":
                        last_attack_damage = other.abilities[last_attack][1] * 2
                    else:
                        last_attack_damage = other.abilities[last_attack][1]
                    
                    if suggested_attack_damage <= last_attack_damage:
                        suggested_attack = last_attack
            else:
                suggested_attack = 0#random.randint(1, len(other.abilities)-1)
                for i in range(len(other.abilities)):
                    if other.abilities[i][3] == "weak":
                        if other.abilities[suggested_attack][1] < other.abilities[i][1] // 2:
                            suggested_attack = i
                    if other.abilities[i][3] == "strong":
                        if other.abilities[suggested_attack][1] < other.abilities[i][1] * 2:
                            suggested_attack = i
                    if other.abilities[i][3] == "":
                        if other.abilities[suggested_attack][1] < other.abilities[i][1]:
                            suggested_attack = i

            #enemy attack damage calculation, also calculate what ability to use
            sentence2 = ""
            if (other.abilities[suggested_attack][2] == "fire" and self.element == "grass") or (other.abilities[suggested_attack][2] == "water" and self.element == "fire") or (other.abilities[suggested_attack][2] == "grass" and self.element == "water"):
                attack2 = other.abilities[suggested_attack][1] * 2
                other.abilities[suggested_attack][3] = "strong"
                sentence2 = "It\'s very effective!"
            elif (other.abilities[suggested_attack][2] == "grass" and self.element == "fire") or (other.abilities[suggested_attack][2] == "fire" and self.element == "water") or (other.abilities[suggested_attack][2] == "water" and self.element == "grass"):
                attack2 = other.abilities[suggested_attack][1] // 2
                other.abilities[suggested_attack][3] = "weak"
                sentence2 = "It\'s not very effective."
            else:
                attack2 = self.abilities[suggested_attack][1]
            
            #enemy attacking
            print(f"{other.name} is attacking with the move {other.abilities[suggested_attack][0]}! {sentence2}\n{self.health} - {attack2} = {self.health - attack2}")
            self.health -= attack2
            if self.health <= 0:
                return other.name

    def draw(self, win):
        self.counting = 0
        if self.place == "ally":
            if self.hurt:
                win.blit(self.pokemonanimations[1], (80, 242))
            else:
                win.blit(self.pokemonanimations[0][self.counting//6], (80, 242))
        else:
            if self.hurt:
                win.blit(self.pokemonanimations[1], (570, 72))
            else:
                win.blit(self.pokemonanimations[0][self.counting//6], (570, 72))
        self.counting += 1
"""