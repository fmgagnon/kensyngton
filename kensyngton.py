# l'audace a un nom : une liste et un dictionnaire pour, respectivement, le journal et la planche de jeu.
journal = []
# proposition : chaque entrée a un index numérique, un flag pour indiquer si le mouvement est forcé et les trois informations communiquées par mvt.



import random

# d’accord, ce n’est pas joli, mais ça permet d’interroger facilement l’état de chacun des points du jeu.
#	en faisant, par exemple, planche[‘A1’].
# Les valeurs sont ‘R’, ‘B’ et ‘’ (vide)
# Guillaume : Voir issue sur le github pour la notation
planche = {'A1': '', 'A2': '', 'A3': '', 'B1': '', 'B2': '', 'B3': '', 'C1': '', 'C2': '', 'C3': '', 'D1': '', 'D2': '', 'D3': '', 'E1': '', 'E2': '', 'E3': '', 'F1': '', 'F2': '', 'F3': '', 'G1': '', 'G2': '', 'G3': '', 'H1': '', 'H2': '', 'H3': '', 'I1': '', 'I2': '', 'I3': '', 'J1': '', 'J2': '', 'J3': '', 'K1': '', 'K2': '', 'K3': '', 'L1': '', 'L2': '', 'L3': '', 'M1': '', 'M2': '', 'M3': '', 'N1': '', 'N2': '', 'N3': '', 'O1': '', 'O2': '', 'O3': '', 'P1': '', 'P2': '', 'P3': '', 'Q1': '', 'Q2': '', 'Q3': '', 'R1': '', 'R2': '', 'R3': '', 'S1': '', 'S2': '', 'S3': '', 'T1': '', 'T2': '', 'T3': '', 'U1': '', 'U2': '', 'U3': '', 'V1': '', 'V2': '', 'V3': '', 'W1': '', 'W2': '', 'W3': '', 'X1': '', 'X2': '', 'X3': '', 'NIL': ''}

# pour que les fonctions puissent communiquer entre elles, je propose une liste appelée mvt qui comprend les infos et est ensuite encastrée dans le journal de jeu.
# mvt = [coul, orig, dest]
# coul peut être rouge ou bleu.

# Tentative d'utiliser des classes pour manipuler les éléments du plateau
# C'est une proposition de design pour l'instant, il faut regarder si c'est mieux qu'utiliser des objets de type liste dans lesquels on va piocher
class Point:
    def __init__(self, name):
        self.name = name      
        self.etat = planche[self.name] #Définir une exception ici
        
# On "classifie" le tableau de jeu, j'ai essayé d'en faire une fonction pour n'importe quel dictionnaire mais j'ai échoué lamentablement
# mais ça marche comme ça avec la planche de jeu
cles = planche.keys()
for i in cles:
   vars()[i] = Point(i)
        

class Triangle:
    #Une classe pour assigner et récupérer l'état des triangles du plateau de jeu"
    def __init__(self, sommets): #sommets est une liste de 3 Points -> exception si mauvais nombre de Points
        self.name = sommets[0][0]
    def etat(self): # peut être complet par un joueur, 'mort' càd non reremplissable (demande conscience de l'état précédent) ou autre
        if sommets[0]==sommets[1]==sommets[2]:
            self.etat=sommets[0]
            
        
class Carre:
    #Une classe pour assigner et récupérer l'état des carrés du plateau de jeu"
        def __init__(self, name):
            self.name = name 
            self.etat = etat
    
class Hex:
    #Une classe pour assigner et récupérer l'état des hexagones du plateau de jeu"
    def __init__(self, name, coul):
        self.name = name
        self.coul = coul
        
def fin():
    print coul + "a gagné!"        
	quit()

def triangle(point):
    return point[0]

def legal():

	# vérifie si un geste est légal
	# plusieurs choses :
	#	les points sont-ils contigus?


	#	le point de départ est-il occupé par un pion de la couleur du joueur?
	if planche[mvt[1]] != mvt[0]:
		leg = "Vous n'avez pas de pion sur ce point."



	#	le point de destination est-il inoccupé?
	if planche[mvt[2]] != '':
		leg = "Le point de destination est occupé"
	#	un carré ou un triangle formé récemment a-t-il été reformé? Chaque point appartenant à un triangle et un seul on peut ếcrire une fonction
	#   triangle qui à un point associe son triangle. C'est un peu plus compliqué pour les carrés.
	#   3 états pour un triangle : mover (occupé par un joueur), mort (était occupé un tour avant) ou '' (quelconque)
	#   pout faire ça, autant définir une classe triangle, une classe carré et une classe hexagone pour pouvoir tester l'état des figures géométriques,
	#   que le grand cric me croque, c'est de la programmation orientée objet (géométrique)!
	
    if triangle(mvt[2]).etat = mort or carre(mvt[2]).etat = mort: # c'est du "pseudo code" après avoir défini les classes on verra comment écrire correctement
        
		leg = "Il n'est pas permis de reformer un carré ou un triangle avant deux coups."	


	else:
		leg = "ok"


	return leg

def question():
	leg = ''
	while leg != "ok":
		print leg
		# demande quel mouvement effectuer -> mvt
		legal(mvt)
	return mvt


def carre():

def triangle():


def verif():
	# vérifie si un carré ou un triangle a été complété
	# si oui, appeler les fonctions idoines.

		carre(coul, lettre)


		triangle(coul, deuxlettres)

	# Vérifie si un hexagone de la bonne couleur a été complété
                si oui : fin(coul,hex)
                


def phasedeux_bleu():
    # Ici, le code pour le joueur humain.

    while True:
        # interroge sur le point d'origine
        orig = raw_input("Quel pion déplace-t-on? ")
        dest = raw_input("Vers quel point? ")
        if orig not in planche:
            print "Ce point d'origine n'existe pas."
        if dest not in planche:
            print "Ce point de destination n'existe pas."
        if planche['orig'] != 'B':
            print "Vous n'avez pas de pion sur ce point."
        if planche['point'] != '':
            print "Ce point est occupé."
        # ici : teste si les points sont contigus.
            print "Ces deux point ne sont pas contigus."
        else:
            planche['orig'] = ''        # on vide le point d'origine
            planche['dest'] = 'B'       # on indique le pion sur la plane
            journal.append("B:" + orig + ">" + dest)  # le mouvement est indiqué dans le journal
            break                 # on brise la boucle pour finir le tour



def phaseun_rouge():
    # Je sépare les deux pour que la programmation de l'AI soit plus claire.
    # Rouge = AI

    point = 'NIL'       # un petit bidouillis pour pouvoir initier la boucle.

    while planche['point'] != '':
        # choisit un point (pour l'instant au hasard)
        point =    # ça prendrait un petit code pour choisir un point...
       
    planche['point'] = 'R'       # on indique le pion sur la plane
    journal.append("R:" + point)  # le mouvement est indiqué dans le journal

def phaseun_bleu():
    # Ici, le code pour le joueur humain.

    while True:
        # interroge sur le pion à placer
        point = raw_input("Sur quel point mettre un pion? ")
        if point not in planche:
            print "Ce point n'existe pas."
        if planche['point'] != '':
            print "Ce point est occupé."
        else:
            planche['point'] = 'B'       # on indique le pion sur la plane
            journal.append("B:" + point)  # le mouvement est indiqué dans le journal
            break                     # on brise la boucle pour finir le tour


def phaseun(quicommence):
    # Une phase facile à programmer : Les joueurs placent, tour à tour, des pions.
    # C'est ici que quicommence est traité.
    i = 0
    if quicommence = 1:
        while i < 14:
            phaseun_rouge()
            phaseun_bleu()
            i += 1
    else:
        while i < 14;
            phaseun_rouge()
            phaseun_bleu()
            i += 1

def phasedeux():
    # La phase du jeu la plus importante...    

# Le jeu en tant que tel devrait appeler deux boucles principales : Le premier tour, où les joueurs emplissent la planche, et le second, où il s'agit de déplacements.

# La variable quicommence sert à décider... bon... devine... comme le jeu est symétrique, le même joueur commence les deux phases.
quicommence = randint(0,2)
phaseun(quicommence)
phasedeux(quicommence)
