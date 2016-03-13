# _*_ coding:utf-8 _*
# HAIOS.org PRODUCT (by haikent)
import sys
import os
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Game:
    def __init__(self):
        self.player=random.randint(0,1)
        self.data=[str(x) for x in range(1,10)]
        self.on=True
        self.boxdata={
                       "R1":(0,1,2),
                       "R2":(3,4,5),
                       "R3":(6,7,8),
                       "C1":(0,3,6),
                       "C2":(1,4,7),
                       "C3":(2,5,8),
                       "X1":(0,4,8),
                       "X2":(2,4,6)
                     }
        self.checkData=(
                         ("R1","C1","X1"),("R1","C2"),("R1","C3","X2"),
                         ("R2","C1"),("R2","C2","X1","X2"),("R2","C3"),
                         ("R3","C1","X2"),("R3","C2"),("R3","C3","X1")
                       )


    def gui(self):
       s=tuple(tuple(self.data))
       a='''
         %s ║ %s ║ %s
        ═══╬═══╬═══
         %s ║ %s ║ %s
        ═══╬═══╬═══
         %s ║ %s ║ %s
        '''+bcolors.WARNING #bcolors for color text
       return a%s

    def check(self,x): # x => [0-8]
        if x>=0 and x<=8:
            cd=self.checkData[x]
            for rcx in cd:
                if all((("x","0")[self.player])==self.data[ij] for ij in self.boxdata[rcx]):
                      self.on=False
                      return True
            return False



    def play(self,x):
        x=x-1  # [1-9] => [0-8]
        if x in range(9) and  not (self.data[x]=="x" or self.data[x]=="0") :
             self.data[x]=("x","0")[self.player]
             self.check(x)
             if self.on:
                   self.player=(self.player+1)%2 # change player
        else:
           print "Invalid Position"+bcolors.FAIL



if __name__ == "__main__":
    game=Game()
    while game.on:
        try:
           os.system("clear")
           print game.gui()
           x=input("Player :"+("x","0")[game.player]+" Input[1-9]=")
           game.play(x)
        except NameError:
            print "Invalid input"
    os.system("clear")
    print game.gui()
    print "Player :"+("x","0")[game.player]+" winner"
