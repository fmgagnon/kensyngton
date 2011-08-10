#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import random





## INITIALISATION DES LISTES DU JEU

    # Un journal des coups joués dans une partie pour pouvoir rendre compte de la partie après coup :
journal = []


    # Le plateau de jeu, 'planche' répertorie les noms des points:
planche = ['A1','B1','C1','I1','J1','K1','C2','D2','E2','G2','H2','I2','H3','G3','F3','S3','R3','Q3','H4','Q4',
    'P4','O4','J4','I4','J5','O5','N5','M5','L5','K5','O6','P6','V6','W6','X6','N6','P7','Q7','R7','T7','U7',
    'V7','Aa','Ba','Bb','Cb','Db','Dc','Ec','Ed','Gd','Fd','Fe','Se','Sf','Rf','Tf','Tg','Ug','Uh','Vh',
    'Wh','Wi','Xi','Xj','Nj','Mj','Mk','Lk','Ll','Kl','Al']

    # Dictionnaire pour définir les triangles qui sont proches les uns des autres. À un nom de triangle est associé la liste de ses voisins directs. C'est une information nécessaire pour avoir la géométrie du plateau. 
voisins = {'A':['B','K'], 'B': ['A','C'],'C':['B','D','I'],'D':['C','E'],'E':['D','G'],'F':['G','S'],'G':['E','F','H'],'H':['G','I','Q'],'I':['C','H','J'],'J':['I','K','O'],'K':['A','J','L'],'L':['K','M'],'M':['L','N'],'N':['M','O','X'],'O':['J','N','P'],'P':['O','Q','V'],'Q':['H','P','R'],'R':['Q','S','T'],'S':['F','R'],'T':['R','U'],'U':['T','V'],'V':['U','P','W'],'W':['V','X'],'X':['W','N']}

    
    # On crée une liste contenant le noms des triangles du jeu
triangles = voisins.keys()
    
    # On crée une liste contenant les noms des hexagones du jeu, nommés h_1,h_2,...,h_a...
hexagones = []
for p in planche:
    if 'h_'+p[1] not in hexagones:
        hexagones.append('h_' + p[1])


    # On crée une liste contenant les noms des carrés du jeu. Les carrés sont nommés en fonction des deux hexagones qu'ils séparent (par exemple : 'c_12' ou 'c_3e')
carres = [] 
for k in voisins.keys():  # On cherche parmi les triangles voisins les points qui sont sur le même hexagone
    for t in voisins[k]:
        Z = []
        for p in planche:            
            if (p[0] == t or p[0] == k):
                Z.append(p[1])
        Z1 = []           
        for i in Z:
            if Z.count(i) == 2 and i not in Z1:
                Z1.append(i)
        Z1 = sorted(Z1)
        a = Z1[0] + Z1[1]
        if a not in carres: 
            carres.append('c_'+a)






## CLASSES POUR LES POINTS


class Point:
    def __init__(self, name):
        self.name = name      
        self.etat = 'vide'       # Peut prendre les valeurs : 'vide', 'R', 'B'
        self.precedent = 'vide'  # Peut prendre les valeurs : 'vide', 'R', 'B'
        self.triangle = globals()[name[0]]  # ajouter à la liste déterminée correctement, j'ai cherché longtemps la fonction !
        self.triangle_nom = name[0]  # utile ?
        self.hexagone = globals()['h_'+name[1]]  # ajouter à la liste déterminée correctement
        self.hexagone_nom = 'h_'+name[1] # utile ?
        self.carres = []              # sera ajouté après le remplissage des triangles et des hexagones
        self.carres_noms = []       # utile ?
     
    def changement(self, nouvel_etat): #etat est un str, méthode à appliquer quand un mouvement a été déclaré valide pour changer l'état d'un point
        self.precedent = self.etat
        self.etat = nouvel_etat




## INITIALISATION DES CLASSES DU TABLEAU DE JEU    
# On "classifie" le tableau de jeu, on crée des instance de la classe Point pour chaque point et on les range dans des listes de 3, 4 et 6 élements pour représenter les triangles, carrés et hexagones du tableau de jeu.
# J'utilise la fonction "globals()" pour créer des variables ayant le nom d'élements préexistant (dans les listes planche, triangle, carres et hexagone)

for i in triangles:
    globals()[i] = [] #initialise les listes qui vont servir de triangle
        
   
for j in carres:
    globals()[j] = [] #initialise les listes qui vont servir de carrés
        
for k in hexagones:
    globals()[k] = [] #initialise les listes qui vont servir d'hexagone   
        
        
        
        
        
for i in planche:
   globals()[i] = Point(i) # On créé ici un objet de la classe "Point" pour chaque maille du tableau de jeu. Ça permet de déterminer et manipuler leur état facilement.
           
   if globals()[i] not in globals()[i[0]]:
       globals()[i[0]].append(globals()[i]) # ajoute le point i au triangle adéquat, chaque triangle est une liste de Points    
   if globals()[i] not in globals()['h_'+i[1]]:
       globals()['h_'+i[1]].append(globals()[i]) # ajoute le point i à l'hexagone adéquat, chaque hexagone est une liste de Points



# l'ajout des carrés est un peu plus compliqué, chaque point peut appartenir à 2 carrés
# On remplit les carrés mais on donne aussi une valeur à tous les attributs Point.carres, Point.carres_nom pour tous les point de la planche      

for t in triangles:         # commenter
    for i in range(3): 
        v = globals()[t][i] 
        w = globals()[t][(i + 1) % 3]
        z = sorted([w.name[1], v.name[1]])
        if ((z[0] in [str(i) for i in range(1,8)]) or (z[1] in [str(i) for i in range(1,8)])):  
            
            if v not in globals()['c_'+z[0]+z[1]]:
                globals()['c_'+z[0]+z[1]].append(v)
                v.carres.append(globals()['c_'+z[0]+z[1]])          
                v.carres_noms.append('c_'+z[0]+z[1])
                    
            if w not in globals()['c_'+z[0]+z[1]]:
                globals()['c_'+z[0]+z[1]].append(w)
                w.carres.append(globals()['c_'+z[0]+z[1]])
                w.carres_noms.append('c_'+z[0]+z[1]) 
                 
                 



## TESTS

    # Deux triangles sont-ils voisins?
def est_voisin(str1, str2): #vérifie si deux points sont sur des triangles voisins ou si deux triangles sont voisins
    if str1[0] in voisins[str2[0]]:
        return True
      


        


    
# pour que les fonctions puissent communiquer entre elles, je propose une liste appelée mvt qui comprend les infos et est ensuite encastrée dans le journal de jeu.
# mvt = [coul, orig, dest, forced]
# coul peut être rouge (R) ou bleu (B).   
    
def legal(mvt):
    leg = "ok"   
	# vérifie si un geste est légal
	# plusieurs choses :
	#	les points sont-ils contigus?

    if (mvt[1].name[0] == mvt[2].name[0] or (mvt[1].name[1] == mvt[2].name[1] and est_voisin(mvt[1],mvt[2]))) == False:
        leg = "Les deux points ne sont pas contigus." # Le mouvement est possible si les deux points sont sur le même triangle ou sur deux triangles voisins et sur le même hexagone
        
   

	#	le point de départ est-il occupé par un pion de la couleur du joueur?
	if mvt[1].etat != mvt[0]:
		leg = "Vous n'avez pas de pion sur ce point."



	#	le point de destination est-il inoccupé?
	if mvt[2].etat != 'vide':
		leg = "Le point de destination est occupé."
		
	#	un carré ou un triangle formé récemment a-t-il été reformé? Chaque point appartenant à un triangle et un seul on peut ếcrire une fonction
	
	for i in mvt[2].carres:
	    if [i[0].precedent, i[1].precedent, i[2].precedent, i[3].precedent] == 4 * mvt[0]:
    # Si les 4 points appartenaient le tour précédent au joueur, il ne peut pas reformer le carré.
    # Vérifier s'il n'y a pas des conditions supplémentaires en cas de mouvement forcé
        
		    leg = "Il n'est pas permis de reformer un carré avant deux coups."	
		
    if mvt[2].triangle[0].precedent == mvt[2].triangle[1].precedent == mvt[2].triangle[2].precedent == mvt[0]:   
        leg = "Il n'est pas permis de reformer un triangle avant deux coups."
     # Si les 3 points appartenaient le tour précédent au joueur, il ne peut pas reformer le triangle.
     # Vérifier s'il n'y a pas des conditions supplémentaires en cas de mouvement forcé  
    return leg


def question():
	leg = ''
	while leg != "ok":
		print leg
		# demande quel mouvement effectuer -> mvt
		legal(mvt)
	return mvt


def verif():
	# vérifie si un carré ou un triangle a été complété
	# si oui, appeler les fonctions idoines.

         
         return [] # Il faut réécrire les vérifications pour les carrés et les triangles en tenant compte de la structure des Poins()
         















## PHASES DE JEU


    # Dernière phase : la fin
def fin(coul):
    print coul + " a gagné!"        
    quit()


    # Le joueur force un mouvement d'un pion rouge (ordinateur)
def forcerouge():


    # L'ordinateur force un mouvement d'un pion bleu (joueur)
def forcebleu():


    # Déplacement de l'ordinateur
def phasedeux_rouge():



    # Déplacement du joueur humain.      
def phasedeux_bleu():
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



    # Pions de l'ordinateur.
def phaseun_rouge():
    point = 'NIL'       # un petit bidouillis pour pouvoir initier la boucle.

    while planche['point'] != '':
        # choisit un point (pour l'instant au hasard)
        point = chr(randint(65,89)) + str(randint(1,3))
       
    planche['point'] = 'R'       # on indique le pion sur la plane
    journal.append("R:" + point)  # le mouvement est indiqué dans le journal


    # Pions du joueur humain.
def phaseun_bleu():
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


    # Mise en place des pions
def phaseun(quicommence):
    # Une phase facile à programmer : Les joueurs placent, tour à tour, des pions.
    # C'est ici que quicommence est traité.
    i = 0
    if quicommence == 1:
        while i < 14:
            phaseun_rouge()
            phaseun_bleu()
            i += 1
    else:
        while i < 14:
            phaseun_rouge()
            phaseun_bleu()
            i += 1

    #
def phasedeux():
    # La phase du jeu la plus importante...    
    return []


# Le jeu en tant que tel devrait appeler deux boucles principales : Le premier tour, où les joueurs emplissent la planche, et le second, où il s'agit de déplacements.

# La variable quicommence sert à décider... bon... devine... comme le jeu est symétrique, le même joueur commence les deux phases.
quicommence = random.randint(0,2)
#phaseun(quicommence)
#phasedeux(quicommence)
legal(['R',A1,M5])
fin('Rouge')
