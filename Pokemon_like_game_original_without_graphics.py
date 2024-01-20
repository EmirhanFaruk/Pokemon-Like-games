
# Modification date: Fri Dec 24 19:07:48 2021

# Production date: Sun Sep  3 15:43:57 2023

import random

class Pokemon:
    def __init__(self, name, possible_element = ["normal", "fire", "water", "grass"]):
        #pokemon properties
        self.name = name
        self.health = random.randint(100, 201)
        #getting random element
        self.element = random.choice(possible_element)
        self.abilities = [["Punch", 30, "normal", ""]]#[attack_name, damage, element, strong or not(for the bots)]
        self.normal_abilities = [["Kick", 40, "normal", ""]]
        self.fire_abilities = [["Flying match", 40, "fire", ""]]
        self.water_abilities = [["Strong spit", 40, "water", ""]]
        self.grass_abilities = [["Thornbush", 40, "grass", ""]]
        self.all_abilities = [self.normal_abilities, self.fire_abilities, self.water_abilities, self.grass_abilities]


        #giving the pokemon a new ability
        if self.element == "fire":
            self.abilities.append(random.choice(self.all_abilities[1]))
        elif self.element == "water":
            self.abilities.append(random.choice(self.all_abilities[2]))
        elif self.element == "grass":
            self.abilities.append(random.choice(self.all_abilities[3]))
        elif self.element == "normal":
            self.abilities.append(random.choice(self.all_abilities[0]))
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


name = input("Enter your name: ")
Player = Pokemon(name, ["water"])
Enemy = Pokemon("Enemy", ["fire"])
winner = Player.combat(Enemy)
input(str(winner) + " Won!")
