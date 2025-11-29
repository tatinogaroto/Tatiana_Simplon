#EXERCICE SIMPLON FORMATION IA
#Tatiana Souza
#tnogaroto@gmail.com

#DEBUT
print("Bonjour ! C’est l’exercice de positionnement de Simplon !\n")

print("Je voudrais vraiment participer à la formation Développeur IA chez Simplon.")
print("Mais pour ça, il y a un défi très important que je dois faire.\n")

print("Chaque année, mes voisins gagnent le concours de décoration de Noël.")
print("Mais cette fois, on va être les champions. J’ai acheté un million de lumières, sur un panneau de 1000 x 1000.\n")

print("Le Père Noël va m’envoyer des instructions pour allumer et éteindre ces lumières.")
print("Si on suit bien toutes les instructions, on va gagner le concours.\n")

print("J’ai besoin de toi.\n")

#INPUT_Q1
Q1 = input("On commence ? Es-tu prêt ? (oui/non) \n").lower()
if Q1 == "oui":
    print("\nSuper ! C'est parti !\n")
else:
    print("\nOh non, tu n'as pas le choix, on doit gagner le concours cette année ! J'ai besoin de toi !\n") 


#CREATION GRID 1000x1000
print("D'abord, on crée une grille de 1000x1000 et on vérifie que toutes les lumières sont éteintes...\n") 
print("A..\nAT..\nATE..\nATEN..\nATEND..\nATENDE..\nATTEND..\nATTENDE..\nATTENDRE..\n") 

SIZE = 1000
grid = [[0] * SIZE for _ in range(SIZE)]

#VERIFICATION
sumON = sum(sum(row) for row in grid)

print("Grille créée avec succès !")
print(f"\nNombre total de lumières allumées : {sumON}")
print("\nTout est bon ! Toutes les lumières sont éteintes !\n")

#INPUT_Q2
Q2 = input("C'était facile ! On continue !\n\nDing Dong !\nLa lettre du Père Noël est arrivée !\nVeux-tu l'ouvrir ? (oui/non) ").lower()
if Q2 == "oui":
    print("\nOn l'ouvre !\n")
else:
    print("\nComment peux-tu ignorer le Père Noël ?\n")
    print("On va l'ouvrir quand même !!\n")

print("A..\nAT..\nATE..\nATEN..\nATEND..\nATENDE..\nATTEND..\nATTENDE..\nATTENDRE..\n") 


#INPUT_Q3
print("Voici les instructions :")
print("(turn on 887,9 through 959,629\n"
      "turn on 454,398 through 844,448\n"
      "turn off 539,243 through 559,965\n"
      "turn off 370,819 through 676,868\n"
      "turn off 145,40 through 370,997\n"
      "turn off 301,3 through 808,453\n"
      "turn on 351,678 through 951,908\n"
      "toggle 720,196 through 897,994\n"
      "toggle 831,394 through 904,860)")

print("\nLe Père Noël veut savoir combien de lumières resteront allumées à la fin de ces instructions.\n")
print("Oh non ! Je ne peux pas lire ces instructions comme ça...")

Q3 = input("Tu sais comment les lire ? (oui/non) ").lower()
if Q3 == "oui":
    print("\nSuper ! J'ai aussi eu une idée ! On doit les transformer ! Au travail !\n")
else:
    print("\nPas de problème ! J'ai une idée ici ! On doit les transformer ! Au travail !\n")

print("A..\nAT..\nATE..\nATEN..\nATEND..\nATENDE..\nATTEND..\nATTENDE..\nATTENDRE..\n") 

print("Ça a marché !\n")

#DEF FONCTIONS ON OFF TG
def ON(grid,x1,y1,x2,y2):
    for y in range(y1,(y2 + 1)):
        for x in range(x1,(x2+1)):
            grid[y][x] = 1

def OFF(grid,x1,y1,x2,y2):
    for y in range(y1,(y2 + 1)):
        for x in range(x1,(x2+1)):
            grid[y][x] = 0 

def TG(grid,x1,y1,x2,y2):
    for y in range(y1,(y2 + 1)):
        for x in range(x1,(x2+1)):
            grid[y][x] = 1 - grid[y][x]  

#DEF FONCTION EXECUTION
def exCMD(grid, comando):
    part = comando.lower().split()
    if part[0] == "toggle":
        x1, y1 = map(int, part[1].split(','))
        x2, y2 = map(int, part[3].split(','))
        TG(grid, x1, y1, x2, y2)
    elif part[0] == "turn" and part[1] == "on":
        x1, y1 = map(int, part[2].split(','))
        x2, y2 = map(int, part[4].split(','))
        ON(grid, x1, y1, x2, y2)
    elif part[0] == "turn" and part[1] == "off":
        x1, y1 = map(int, part[2].split(','))
        x2, y2 = map(int, part[4].split(','))
        OFF(grid, x1, y1, x2, y2)

#INSTRUCTIONS PERE NOEL
comandos = [
    "turn on 887,9 through 959,629",
    "turn on 454,398 through 844,448",
    "turn off 539,243 through 559,965",
    "turn off 370,819 through 676,868",
    "turn off 145,40 through 370,997",
    "turn off 301,3 through 808,453",
    "turn on 351,678 through 951,908",
    "toggle 720,196 through 897,994",
    "toggle 831,394 through 904,860"
]

#EXEC exCMD
for cmd in comandos:
    exCMD(grid, cmd)


#VERIFICATION 2
sumON = sum(sum(row) for row in grid)

print(f"\nAprès avoir exécuté les commandes du Père Noël, on sait maintenant combien de lumières sont allumées !")
print(f"Il y a un total de {sumON} lumières allumées !")
print("Maintenant, on pourrait se reposer... mais quoi ???\n")


#INPUT_Q4
print("\nDing Dong ! Une autre lettre est arrivée !\n")
print("Le Père Noël s'est trompé et maintenant on doit travailler avec la luminosité des lampes !\n")

print("Voici les nouvelles instructions :\n")
print("The phrase 'turn on' actually means that you should increase the brightness of those lights by 1.")
print("The phrase 'turn off' actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.")
print("The phrase 'toggle' actually means that you should increase the brightness of those lights by 2.\n")

Q4 = input("Je pense que j'ai besoin d'un mot d'encouragement pour transformer ces nouvelles instructions...\nTape un mot d'encouragement : ")
if Q4 != "":
    print("\nMerci ! Au travail !\n")
else:
    print("\nMerci ! Au travail !\n")

print("A..\nAT..\nATE..\nATEN..\nATEND..\nATENDE..\nATTEND..\nATTENDE..\nATTENDRE..\n") 

print("C'était plus difficile, mais ça a marché !\n")


#CREATION GRID BRIGHTNESS
teste = [[0] * SIZE for _ in range(SIZE)]

#DEF FONCTIONS BRIGHTNESS
def ON_B(grid, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            grid[y][x] = grid[y][x] + 1

def OFF_B(grid, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            grid[y][x] = max(0, grid[y][x] - 1)

def TG_B(grid, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            grid[y][x] = grid[y][x] + 2

#DEF FONCTION EXECUTION BRIGHTNESS
def exCMD_B(grid, comando):
    part = comando.lower().split()
    if part[0] == "toggle":
        x1, y1 = map(int, part[1].split(','))
        x2, y2 = map(int, part[3].split(','))
        TG_B(grid, x1, y1, x2, y2)
    elif part[0] == "turn" and part[1] == "on":
        x1, y1 = map(int, part[2].split(','))
        x2, y2 = map(int, part[4].split(','))
        ON_B(grid, x1, y1, x2, y2)
    elif part[0] == "turn" and part[1] == "off":
        x1, y1 = map(int, part[2].split(','))
        x2, y2 = map(int, part[4].split(','))
        OFF_B(grid, x1, y1, x2, y2)

#EXEC exCMD_B
for cmd in comandos:
    exCMD_B(teste, cmd)

#VERIFICATION 3
sumBR = sum(map(sum, teste))

print(f"\nGrâce à ton encouragement, j'ai pu calculer la luminosité totale des lampes !\n")
print(f"Brillance totale des lumières : {sumBR}")
print("Le Père Noël sera très content ! On a de grandes chances de gagner le concours cette année ! Merci !")
print("Et j'espère recevoir bientôt des nouvelles de Simplon pour la prochaine étape de la sélection !")

#FIN
print("\nFin de l'exercice !")


