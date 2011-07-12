# l'audace a un nom : une liste et un dictionnaire pour, respectivement, le journal et la planche de jeu.
journal = []
# proposition : chaque entrée a un index numérique, un flag pour indiquer si le mouvement est forcé et les trois informations communiquées par mvt.



import random

# d’accord, ce n’est pas joli, mais ça permet d’interroger facilement l’état de chacun des points du jeu.
#	en faisant, par exemple, planche[‘A1’].
# Les valeurs sont ‘R’, ‘B’ et ‘’ (vide)
# Guillaume : Je propose de revoir la numérotation des points et d'utiliser une liste de points qui seront des instances de la classe point.
#planche = {'A1': '', 'A2': '', 'A3': '', 'B1': '', 'B2': '', 'B3': '', 'C1': '', 'C2': '', 'C3': '', 'D1': '', 'D2': '', 'D3': '', 'E1': '', 'E2': '', 'E3': '', 'F1': '', 'F2': '', 'F3': '', 'G1': '', 'G2': '', 'G3': '', 'H1': '', 'H2': '', 'H3': '', 'I1': '', 'I2': '', 'I3': '', 'J1': '', 'J2': '', 'J3': '', 'K1': '', 'K2': '', 'K3': '', 'L1': '', 'L2': '', 'L3': '', 'M1': '', 'M2': '', 'M3': '', 'N1': '', 'N2': '', 'N3': '', 'O1': '', 'O2': '', 'O3': '', 'P1': '', 'P2': '', 'P3': '', 'Q1': '', 'Q2': '', 'Q3': '', 'R1': '', 'R2': '', 'R3': '', 'S1': '', 'S2': '', 'S3': '', 'T1': '', 'T2': '', 'T3': '', 'U1': '', 'U2': '', 'U3': '', 'V1': '', 'V2': '', 'V3': '', 'W1': '', 'W2': '', 'W3': '', 'X1': '', 'X2': '', 'X3': '', 'NIL': ''}



####################################################################################################

# Nouvelle nomenclature pour le plateau de jeu. 'planche' répertorie les noms des points.
planche = ['A1','B1','C1','I1','J1','K1','C2','D2','E2','G2','H2','I2','H3','G3','F3','S3','R3','Q3','H4','Q4',
'P4','O4','J4','I4','J5','O5','N5','M5','L5','K5','O6','P6','V6','W6','X6','N6','P7','Q7','R7','T7','U7',
'V7','Aa','Ba','Bb','Cb','Db','Dc','Ec','Ed','Gd','Fd','Fe','Se','Sf','Rf','Tf','Tg','Ug','Uh','Vh',
'Wh','Wi','Xi','Xj','Nj','Mj','Mk','Lk','Ll','Kl','Al','NIL']
planche1 = planche
planche1.remove('NIL')
# Dictionnaire pour définir les triangles qui sont proches les uns des autres. À un nom de triangle est associé la liste de ses voisins directs. C'est une information nécessaire pour avoir la géométrie du plateau. 
voisins = {'A':['B','K'], 'B': ['A','C'],'C':['B','D','I'],'D':['C','E'],'E':['D','G'],'F':['G','S'],'G':['E','F','H'],'H':['G','I','Q'],'I':['C','H','J'],'J':['I','K','O'],'K':['A','J','L'],'L':['K','M'],'M':['L','N'],'N':['M','O','X'],'O':['J','N','P'],'P':['O','Q','V'],'Q':['H','P','R'],'R':['Q','S','T'],'S':['F','R'],'T':['R','U'],'U':['T','V'],'V':['U','P','W'],'W':['V','X'],'X':['W','N']}

# On crée une liste contenant le noms des triangles du jeu
triangles = voisins.keys()

# On crée une liste contenant les noms des hexagones du jeu, nommés h_1,h_2,...,h_a...
hexagones = []
for p in planche1:
    if 'h_'+p[1] not in hexagones:
        hexagones.append('h_' + p[1])


# On crée une liste contenant les noms des carrés du jeu. Les carrés sont nommés en fonction des deux hexagones qu'ils séparent (par exemple : 'c_12' ou 'c_3e')
carres = [] 
for k in voisins.keys():  # réécrire en plus simple
    for t in voisins[k]:
        Z = []
        for p in planche1:            
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

#Il manque encore une information pour définir carrés et hexagones. On peut remarquer que sur un triangle, chacun des sommets appartient à un hexagone différent. On peut alors abandonner la notation A1,A2,A3 pour prendre la notation Ax,Az,Ah où x,z,h sont les numéros des hexagones. Il faut remarquer qu'on doit comptabiliser 19 hexagones, 7 complets au centre et 12 incomplets à l'extérieur. Cette notation a l'avantage de donner dans le nom de chaque point son appartenance à son triangle ET à son hexagone. Trouver son carré est alors facile. Pour conclure, on peut nommer un carré en fonction des deux hexagones qu'il sépare.



###################################################################################################
# Tentative d'utiliser des classes pour manipuler les éléments du plateau
# C'est une proposition de design pour l'instant, il faut regarder si c'est mieux qu'utiliser des objets de type liste dans lesquels on va piocher

#À exécuter à part en tant que module importé, sinon on va avoir des problèmes

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
          
          
          
          
###################################################################################################    
# On "classifie" le tableau de jeu, on crée des instance de la classe Point pour chaque point et on les range dans des listes de 3, 4 et 6 élements pour représenter les triangles, carrés et hexagones du tableau de jeu.
# J'utilise la fonction "var()" pour créer des variables ayant le nom d'élements préexistant (dans les listes planche, triangle, carres, hexagone)

for i in triangles:
    vars()[i] = [] #initialise les listes qui vont servir de triangle

for j in carres:
    vars()[j] = [] #initialise les listes qui vont servir de carrés
    
for k in hexagones:
    vars()[k] = [] #initialise les listes qui vont servir d'hexagone   
    
for i in planche1:
   vars()[i] = Point(i) # On créé ici un objet de la classe "Point" pour chaque maille du tableau de jeu. Ça permet de déterminer et manipuler leur état facilement.
   if vars()[i] not in vars()[i[0]]:
       vars()[i[0]].append(vars()[i]) # ajoute le point i au triangle adéquat, chaque triangle est une liste de Points    
   if vars()[i] not in vars()['h_'+i[1]]:
       vars()['h_'+i[1]].append(vars()[i]) # ajoute le point i à l'hexagone adéquat, chaque hexagone est une liste de Points

# l'ajout des carrés est un peu plus compliqué, chaque point peut appartenir à 2 carrés      
for t in triangles:         # commenter
    for i in range(3): 
        v = vars()[t][i] 
        w = vars()[t][(i + 1) % 3]
        z = sorted([w.name[1], v.name[1]])
        if ((z[0] in [str(i) for i in range(1,8)]) or (z[1] in [str(i) for i in range(1,8)])):  
        
            if v not in vars()['c_'+z[0]+z[1]]:
                vars()['c_'+z[0]+z[1]].append(v)
                v.carres.append(vars()['c_'+z[0]+z[1]])          
                v.carres_noms.append('c_'+z[0]+z[1])
                
            if w not in vars()['c_'+z[0]+z[1]]:
                vars()['c_'+z[0]+z[1]].append(w)
                w.carres.append(vars()['c_'+z[0]+z[1]])
                w.carres_noms.append('c_'+z[0]+z[1])  
            
            
####################################################################################################        
def est_voisin(str1, str2): #vérifie si deux points sont sur des triangles voisins ou si deux triangles sont voisins
           if str1[0] in voisins[str2[0]]:
            return True
        
def fin():
    print coul + "a gagné!"        
	quit()

    
# pour que les fonctions puissent communiquer entre elles, je propose une liste appelée mvt qui comprend les infos et est ensuite encastrée dans le journal de jeu.
# mvt = [coul, orig, dest]
# coul peut être rouge ou bleu.   
    
def legal(mvt):

	# vérifie si un geste est légal
	# plusieurs choses :
	#	les points sont-ils contigus?

    if (mvt[1].name[0] == mvt[2].name[0] or (mvt[1].name[1] == mvt[2].name[1] and est_voisin(mvt[1],mvt[2]))) == False
        leg = "Les deux points ne sont pas contigus" # Le mouvement est possible si les deux points sont sur le même triangle ou sur deux triangles voisins et sur le même hexagone
        
   

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
	
    if triangle(mvt[2]).etat = mort or carre(mvt[2]).etat = mort: # c'est du "pseudo code" après avoir défini les classes on verra comment écrire correctement il faut en particulier réfléchir à comment on désire enregistrer l'état précédent des points. Soit piocher dans le "journal", soit avoir un attribut de la classe "Point" qu'on met à jour après chaque mouvement.
        
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
