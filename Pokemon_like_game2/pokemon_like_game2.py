
# Modification date: Sun Dec 26 14:48:36 2021

# Production date: Sun Sep  3 15:43:57 2023

#Pour faire attendre
import time

#Pour l'IA
import random 

#Pour effacer les vieux trucs dans la console
from clear_screen import clear

import phrase






#print(Phrase.bvert(Phrase.crouge("Hello, ") + Phrase.cbleu("my name is ") + Phrase.cvert("Emirhan.")))

class Pokemon:
    def __init__(self, nom, type, abilités, propriétés, pdv = "===================="):
        #les propriétés de pokémon
        self.nom = nom
        self.type = type
        self.abilités = abilités
        self.attaque = propriétés["attaque"]
        self.defence = propriétés["defence"]
        self.pdv = pdv
        self.bars = len(pdv)
    
    def combat(self, ennemi):
        print(phrase.Phrase.brouge(phrase.Phrase.ccyan(f"{self.nom}") + phrase.Phrase.cblanc(f" VS ") + phrase.Phrase.cnoir(f"{ennemi.nom}")))


Emirhan = Pokemon("Emirhan", "feu", ["fard"], {"attaque": 100, "defence": 100})
Ennemi = Pokemon("Ennemi", "plant", ["qqch inutile"], {"attaque": 10, "defence": 10})

Emirhan.combat(Ennemi)
input()
