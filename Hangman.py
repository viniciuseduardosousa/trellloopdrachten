import os
import random

lives = 5
woordenlijst = ["Kaas","Auto","Prik","Klok","Jas","Tas","Arm"]
willekeurig = random.choice(woordenlijst)
letters = list(willekeurig)

print("Hallo, welkom. \nDit is een galgje spel. \n \n PRESS ENTER TO START \n")

# game beginnen
begin = input()
os.system('clear')
game = input("typ STOP als je wilt stoppen, Anders press alleen enter. \n \n   DIT GELDT VOOR DE HELE GAME")
os.system('clear')

while begin == "":
    
    print(f"Je hebt {lives} Leven(s)")
    vraag = input("Typ letter in \n" )

    if lives == 0:
        print(f"Je hebt verloren. \nWoord was: {willekeurig}")
        os.abort
        break
    
    elif len(vraag) > 1:
        print("FOUT!! max 1 letter")

    elif game == "STOP" or "stop" or "Stop":
        print("ok tot ziens!")
        os.abort
        break




    