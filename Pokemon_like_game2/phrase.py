
# Modification date: Sun Dec 26 14:42:48 2021

# Production date: Sun Sep  3 15:43:57 2023

#Pour les chaines des charactères colorées
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import time
import sys



class Phrase:
    #couleur des lettres
    @staticmethod
    def crouge(phrase):
        return f"{Fore.RED}{phrase}"
    @staticmethod
    def cbleu(phrase):
        return f"{Fore.BLUE}{phrase}"
    @staticmethod
    def ccyan(phrase):
        return f"{Fore.CYAN}{phrase}"
    @staticmethod
    def cvert(phrase):
        return f"{Fore.GREEN}{phrase}"
    @staticmethod
    def cblanc(phrase):
        return f"{Fore.WHITE}{phrase}"
    @staticmethod
    def cnoir(phrase):
        return f"{Fore.BLACK}{phrase}"
    
    #couleur du background
    @staticmethod
    def brouge(phrase):
        return f"{Back.RED}{phrase}"
    @staticmethod
    def bbleu(phrase):
        return f"{Back.BLUE}{phrase}"
    @staticmethod
    def bcyan(phrase):
        return f"{Back.CYAN}{phrase}"
    @staticmethod
    def bvert(phrase):
        return f"{Back.GREEN}{phrase}"
    @staticmethod
    def bblanc(phrase):
        return f"{Back.WHITE}{phrase}"
    @staticmethod
    def bnoir(phrase):
        return f"{Back.BLACK}{phrase}"

    @staticmethod
    def delay_print(s):#ça marche pas avec les couleurs
        # print one character at a time
        # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
        return