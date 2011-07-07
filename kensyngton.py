# l'audace a un nom : une liste et un dictionnaire pour, respectivement, le journal et la planche de jeu.
journal = []
# proposition : chaque entrée a un index numérique, un flag pour indiquer si le mouvement est forcé et les trois informations communiquées par mvt.



import random

# d’accord, ce n’est pas joli, mais ça permet d’interroger facilement l’état de chacun des points du jeu.
#	en faisant, par exemple, planche[‘A1’].
# Les valeurs sont ‘R’, ‘B’ et ‘’ (vide)
planche = {'A1': '', 'A2': '', 'A3': '', 'B1': '', 'B2': '', 'B3': '', 'C1': '', 'C2': '', 'C3': '', 'D1': '', 'D2': '', 'D3': '', 'E1': '', 'E2': '', 'E3': '', 'F1': '', 'F2': '', 'F3': '', 'G1': '', 'G2': '', 'G3': '', 'H1': '', 'H2': '', 'H3': '', 'I1': '', 'I2': '', 'I3': '', 'J1': '', 'J2': '', 'J3': '', 'K1': '', 'K2': '', 'K3': '', 'L1': '', 'L2': '', 'L3': '', 'M1': '', 'M2': '', 'M3': '', 'N1': '', 'N2': '', 'N3': '', 'O1': '', 'O2': '', 'O3': '', 'P1': '', 'P2': '', 'P3': '', 'Q1': '', 'Q2': '', 'Q3': '', 'R1': '', 'R2': '', 'R3': '', 'S1': '', 'S2': '', 'S3': '', 'T1': '', 'T2': '', 'T3': '', 'U1': '', 'U2': '', 'U3': '', 'V1': '', 'V2': '', 'V3': '', 'W1': '', 'W2': '', 'W3': '', 'X1': '', 'X2': '', 'X3': '', 'NIL': ''}

# pour que les fonctions puissent communiquer entre elles, je propose une liste appelée mvt qui comprend les infos et est ensuite encastrée dans le journal de jeu.
# mvt = [coul, orig, dest]
# coul peut être rouge ou bleu.

def fin():
    print coul + "a gagné!"        
	quit()

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
	#	un carré ou un triangle formé récemment a-t-il été reformé?
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
                

def phaseun_rouge():
    # Je sépare les deux pour que la programmation de l'AI soit plus claire.
    # Rouge = AI

    point = 'NIL'       # un petit bidouillis pour pouvoir initier la boucle.

    while planche['point'] != '':
        # choisit un point (pour l'instant au hasard)
        point =    # ça prendrait un petit code pour choisir un point...
       
    planche['point'] = 'R'       # on indique le pion sur la plane
    journal.append("R " + point)  # le mouvement est indiqué dans le journal

def phaseun_bleu():
    # Ici, le code pour le joueur humain.
    tour = 0

    while tour == 0:
        # interroge sur le pion à placer
        point = raw_input("Sur quel point mettre un pion? ")
        if point not in planche:
            print "Ce point n'existe pas."
        if planche['point'] != '':
            print "Ce point est occupé."
        else:
            planche['point'] = 'B'       # on indique le pion sur la plane
            journal.append("B " + point)  # le mouvement est indiqué dans le journal
            tour = 1                     # on brise la boucle pour finir le tour


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
