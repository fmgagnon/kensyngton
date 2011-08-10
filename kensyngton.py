#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from random import randint





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
for k in voisins.keys():  # On parcoure tous les noms de triangles, on sélectionne le triangle k
    for t in voisins[k]:    # on selectionne les voisins d'un triangle k
        Z = []              # initialisation de la liste qui va contenir les noms de points sur des triangles voisins
        for p in planche:            
            if (p[0] == t or p[0] == k):
                Z.append(p[1])  # on remplit une liste avec les seconds caractères des noms de points qui sont sur deux triangles voisins
        Z1 = []           # initialisation d'une seconde liste qui va servir à séparer les doublons
        for i in Z:
            if Z.count(i) == 2 and i not in Z1: # on cherche les caractères qui sont présent 2 fois dans la liste, ils caractérisent un carré, par exemple le carré c_1a contient les points A1, B1 et Aa, Ba
                Z1.append(i)
        Z1 = sorted(Z1) # on range les caractères du nom du carré dans l'ordre lexicographique
        a = Z1[0] + Z1[1] # on crée une chaine de caractère, 1a dans le cas du carré c_1a
        if a not in carres: # on verifie qu'on a pas déjà traité ce carré
            carres.append('c_'+a) # on ajoute le carré en question (par exemple c_1a) à la liste carres qui contient tous les noms de carrés






## CLASSES POUR LES POINTS


class Point:
    def __init__(self, name):
        self.name = name         # Propriété pour récupérer le nom du Point sous forme de chaîne de caractères
        self.etat = 'vide'       # Peut prendre les valeurs : 'vide', 'R', 'B'
        self.precedent = 'vide'  # Peut prendre les valeurs : 'vide', 'R', 'B'
        self.moved = 'non'       # Permet de savoir si le Point a changé d'état ce tour ci. C'est utile pour la determination correcte de la condition de reformation des triangles et des carrés. La propriété est mise à 'oui' lors d'un changement et est remise à 'non' à la fin de chaque tour pour tous les points n'ayant pas bougé.
        if name != 'NIL':
            self.triangle = globals()[name[0]]  # ajouter à la liste triangle correspondante
            self.triangle_nom = name[0]  # propriété donnant le nom du triangle, utile ?
        
        if name != 'NIL':
            self.hexagone = globals()['h_'+name[1]]  # ajouter à la liste hexagone correspondante
            self.hexagone_nom = 'h_'+name[1] # propriété donnant le nom de l'hexagone, utile ?
        self.carres = []              # sera ajouté après le remplissage des triangles et des hexagones, pour remplir les listes carrés.
        self.carres_noms = []       # propriété donnant le nom du carré, utile ?
     
    def changement(self, nouvel_etat): # nouvel_etat est une chaîne de caractères, méthode à appliquer quand un mouvement a été déclaré valide pour changer l'état d'un point.
        self.precedent = self.etat   
        self.etat = nouvel_etat
        self.moved = 'oui'




## INITIALISATION DES CLASSES DU TABLEAU DE JEU    
# On "classifie" le tableau de jeu, on crée des instance de la classe Point pour chaque point et on les range dans des listes de 3, 4 et 6 élements pour représenter les triangles, carrés et hexagones du tableau de jeu. On crée aussi 3 listes générales : "triangles", "carres" et "hexagones". Chacune de ces trois liste contient tous les triangles, carrés et hexagones respectivement. Ce sont 3 listes de listes, chacune contient tous les points. On peut les utiliser pour parcourir tous les points du plateau facilement.
# J'utilise la fonction "globals()" pour créer des variables ayant le nom d'élements préexistant (dans les listes planche, triangle, carres et hexagone)

indice = 0
for i in triangles:
    globals()[i] = [] #initialise les listes qui vont servir de triangle
    triangles[indice] = globals()[i]  # on remplit la liste "triangles" avec les differents triangles (qui sont des listes). On peut donc ainsi accéder à tous les points du plateau en parcourant la liste triangles et les listes qu'elle contient. On passe donc d'une liste de noms de triangles à une liste contenant les triangles (on est en train de remplacer complètement le contenu de cette liste).
    indice += 1  

indice = 0   
for j in carres:
    globals()[j] = [] #initialise les listes qui vont servir de carrés
    carres[indice] = globals()[j]  # même chose qu'avec triangles, la liste carres est une liste de liste qui contient tous les points
    indice += 1  
    
indice = 0      
for k in hexagones:
    globals()[k] = [] #initialise les listes qui vont servir d'hexagones   
    hexagones[indice] = globals()[k] # même chose qu'avec triangles et carres   
    indice += 1   
        
        
        
for i in planche:
   globals()[i] = Point(i) # On créé ici un objet de la classe "Point" pour chaque maille du tableau de jeu. Ça permet de déterminer et manipuler leur état facilement.
           
   if globals()[i] not in globals()[i[0]]:
       globals()[i[0]].append(globals()[i]) # ajoute le point i au triangle adéquat, chaque triangle est une liste de Points    
   if globals()[i] not in globals()['h_'+i[1]]:
       globals()['h_'+i[1]].append(globals()[i]) # ajoute le point i à l'hexagone adéquat, chaque hexagone est une liste de Points

# l'ajout des carrés est un peu plus compliqué, chaque point peut appartenir à 2 carrés
# On remplit les carrés mais on donne aussi une valeur aux attributs Point.carres et Point.carres_nom pour tous les point de la planche.      

for t in triangles:         # On parcoure tous les triangles du plateau de jeu 
    for i in range(3):  # puis tous les points de chaque triangle.
        v = t[i]            #
        w = t[(i + 1) % 3]  # on selectionne alors les points deux à deux dans chaque triangle : pour le triangle A par exemple, on selectionne d'abord v,w = A1,Aa puis v,w = Aa,Al puis v,w = Al,A1
        z = sorted([w.name[1], v.name[1]]) # on fait une liste triée lexicographiquement [v.name,w.name] ou [w.name,v.name] avec le second caractère des noms des points des triangles, pour le triangle A on aurait [1,a],[a,l] et [1,l]
        if ((z[0] in [str(i) for i in range(1,8)]) or (z[1] in [str(i) for i in range(1,8)])):  # On ajoute les carrés auquels appartient chaque point à la propriété Point.carres et le nom de ces carrés à la propriété Point.carres_noms. On selectionne tous les couples de caractères qui se retrouvent dans le second caractère des noms de deux points différents dans un triangle, dès qu'un des deux caractères au moins est un chiffre entre 1 et 7. En effet les carrés entre 2 hexagones externes (dénotés par une lettre minuscule) existent mais il sont extérieurs au plateau et donc ne peuvent être remplis (la moitié de leur points sont hors du plateau).
            
            if v not in globals()['c_'+z[0]+z[1]]: # on vérifie que le point n'a pas déjà été traité (on va passer plusieurs fois sur chaque point)
                globals()['c_'+z[0]+z[1]].append(v) # on remplit la liste correspondant au carré avec les bons points, par exemple on remplit la liste c_1a avec les point A1, B1, Aa et Ba
                v.carres.append(globals()['c_'+z[0]+z[1]])     # on attribue une valeur à la propriété Point.carres pour le point v      
                v.carres_noms.append('c_'+z[0]+z[1])            # idem pour la valeur Point.carres_noms pour le point v
                    
            if w not in globals()['c_'+z[0]+z[1]]:              # on fait de même pour le point w
                globals()['c_'+z[0]+z[1]].append(w)
                w.carres.append(globals()['c_'+z[0]+z[1]])
                w.carres_noms.append('c_'+z[0]+z[1]) 
                 


## TESTS

    # Deux triangles sont-ils voisins?
def est_voisin(str1, str2): #vérifie si deux points sont sur des triangles voisins ou si deux triangles sont voisins
    if str1[0] in voisins[str2[0]]:
        return True

    
    # Un mouvement est-il légal?    
def legal(mvt):
    leg = "ok"   

    	#	les points sont-ils contigus?
    if (mvt[1].name[0] == mvt[2].name[0] or (mvt[1].name[1] == mvt[2].name[1] and est_voisin(mvt[1],mvt[2]))) == False:
        leg = "Les deux points ne sont pas contigus." # Le mouvement est possible si les deux points sont sur le même triangle ou sur deux triangles voisins et sur le même hexagone
   
   
	    #	le point de départ est-il occupé par un pion de la couleur du joueur?
	elif mvt[1].etat != mvt[0]:
		leg = "Vous n'avez pas de pion sur ce point."


	    #	le point de destination est-il inoccupé?
	elif mvt[2].etat != 'vide':
		leg = "Le point de destination est occupé."
		
		
		
		
    elif mvt[2].triangle[0].precedent == mvt[2].triangle[1].precedent == mvt[2].triangle[2].precedent == mvt[0]:   
        leg = "Il n'est pas permis de reformer un triangle avant deux coups."      
     # Si les 3 points appartenaient le tour précédent au joueur, il ne peut pas reformer le triangle.
     
     
    else: 
        for i in mvt[2].carres: 
            if i[0].precedent+i[1].precedent+i[2].precedent+i[3].precedent == 4 * mvt[0]:
    # Si les 4 points appartenaient le tour précédent au joueur, il ne peut pas reformer le carré.  
                leg = "Il n'est pas permis de reformer un carré avant deux coups."	
            
        
    return leg




def verif(mvt): # À faire
	# vérifie si un carré ou un triangle a été complété
	# si oui, appeler les fonctions idoines (mvt_force() ou fin(coul)).
    # vérifier si un hexagone de la bonne couleur a été complété, si oui déclarer la victoire.
         
    return [] # Il faut réécrire les vérifications pour les carrés et les triangles en tenant compte de la structure des objets de type Points
 







## PHASES DE JEU


    # Dernière phase : la fin
def fin(coul):
    print coul + " a gagné!"        
    quit()


    # Le joueur force un mouvement d'un pion rouge (ordinateur)
def forcerouge():
    return 0

    # L'ordinateur force un mouvement d'un pion bleu (joueur)
def forcebleu():
    return 0

    # Déplacement de l'ordinateur
def phasedeux_rouge(): # À faire
    # Il faut écrire la fonction d'intelligence artificielle....
    # Une partie va être générale et ressembler beaucoup à phasedeux_bleu(). Le gros du codage va consiste à remplacer raw_input du joueur humain par une décision automatique (pas trop stupide). On pourra donc créer une fonction à part pour le choix du mouvement par l'intelligence artificielle.
    return[]



    # Déplacement du joueur humain.      
def phasedeux_bleu():
    # Ici, le code pour le joueur humain.
    # Créer la liste mvt à partir des données fournies par le joueur et utiliser la fonction legal(mvt)
    while True:
        # interroge sur le point d'origine et de destination
        orig = raw_input("Quel pion déplace-t-on? ")
        dest = raw_input("Vers quel point? ")
        if orig not in planche: 
            print "Ce point d'origine n'existe pas."
        elif dest not in planche: 
            print "Ce point de destination n'existe pas."
            
        else:
            mvt = ['B',globals()[orig],globals()[dest],0] # Transforme la chaine de caractère fournie par raw_input() en Point pour le traitement.
            leg = legal(mvt)
        
        
            if leg != 'ok':
                print leg # Renvoie une erreur et redemande un point de départ et d'arrivée
        
            else:
                print leg
                globals()[orig].changement('vide') # On vide le point d'origine
                globals()[dest].changement('B')     # On remplit le point de destination
                verif(mvt) # Fonction vide pour l'instant, sert à faire des mouvements si un triangle ou un carré a été reformé
                journal.append("B:" + orig + ">" + dest)  # le mouvement est indiqué dans le journal, ici orig et dest sont des chaînes de caractères.
                break                 # on brise la boucle pour finir le tour



    # Pions de l'ordinateur.
def phaseun_rouge():
    # Je sépare les deux pour que la programmation de l'AI soit plus claire.

    # Rouge = AI
    NIL_list = []
    NIL = Point('NIL')       # un petit bidouillis pour pouvoir initier la boucle, on initialise un point factice avec une couleur factice pour lancer la boucle. Ce point est ajouté via un faux hexagone (NIL_list) dans la liste des hexagones.
    NIL.changement('N')     # couleur spéciale pour le cas spécial, pour être sûr de ne pas confondre, 'N' est réservé comme état pour les tests et les cas spéciaux comme le point NIL.
    NIL_list.append(NIL)  # On ajoute le Point NIL à l'hexagone NIL_list.
    hexagones.append(NIL_list) # On ajoute l'hexagone NIL_list à la liste des hexagones.
    n = len(hexagones)-1       # On initialise deux nombres n et m, n permet de selectionner un hexagone au hasard parmi la liste hexagones. On l'initialise pour qu'il sélectionne NIL_list en premier.
    m = len(hexagones[n])-1    # m sert à selectionner un Point dans l'hexagone déterminé au hasard par la valeur n. On l'initialise pour qu'il sélectionne le Point NIL en premier.
          
    while hexagones[n][m].etat != 'vide': # la boucle peut être lancée puisque qu'initialement on teste le point NIL qui a pour état 'N', si le hasard retombe sur le point NIL, on rééssayera puiqu'il est à l'état 'N' et donc ne peut recevoir de pion rouge ('R') ou bleu ('B'). On boucle jusqu'à trouver un point inoccupé.
        n = randint(0,len(hexagones)-1)     # Choisit un hexagone au hasard
        m = randint(0,len(hexagones[n])-1)  # Choisit un Point au hasard dans cet hexagone
            
    hexagones[n][m].changement('R')  # On effectue le changement d'état du m ième point du n ième hexagone.
    hexagones[n][m].precedent = hexagones[n][m].etat  # On ajuste la valeur précédente pour faire comme si le point était déjà occupé avant, cela permet de faire fonctionner les tests dès le premier tour (test pour reformer un triangle ou un carré)
    hexagones.remove(NIL_list)      # On veut supprimer le dernier élément de la liste hexagones (NIL_list) puisqu'il n'est plus nécessaire. Pour ne pas perturber les autres fonctions et éviter d'avoir à traiter un cas spécial dans les autres parties du code.           
    journal.append("R:" + hexagones[n][m].name)  # le mouvement est indiqué dans le journal

    # Pions du joueur humain.
def phaseun_bleu():
    while True:
        # interroge sur le pion à placer
        point = raw_input("Sur quel point mettre un pion? ")
        if point not in planche: 
            print "Ce point n'existe pas."
        elif globals()[point].etat != 'vide': 
            print "Ce point est occupé."
        else:
            globals()[point].changement('B')  # on change l'état du point sur la planche.  
            globals()[point].precedent = globals()[point].etat        # On ajuste la valeur précédente pour faire comme si le point était déjà occupé avant, cela permet de faire fonctionner les tests dès le premier tour (test pour reformer un triangle ou un carré)     
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

def phasedeux(quicommence): 
    # La phase du jeu durant laquelle les joueurs bougent leurs pions.  
    i = 0
    if quicommence == 1: 
        while True:
            
            phasedeux_rouge()
            phasedeux_bleu()
            for k in triangles:  
                for l in k:
                    if l.moved == 'no': # Il faut mettre à jour le paramètre précédent des points qui n'ont pas bougé (pour permettre de reformer un triangle ou un carré, si on ne le fait pas il est impossible de les reformer, ils sont toujours bloqués). Mais il ne faut pas effacer le fait que certains pions ont bougé, leur état a déjà été changé lors de ce tour.
                        l.precedent = l.etat
                    
                    l.moved = 'no' # On met tous les points à 'no' pour le prochain tour
            
    else:   #  il faut faire alterner bleu et rouge au lieu de rouge et bleu
        while True:
            
            phasedeux_bleu()
            phasedeux_rouge()
            for k in triangles:  
                for l in k:
                    if l.moved == 'no': # Il faut mettre à jour le paramètre précédent des points qui n'ont pas bougé (pour permettre de reformer un triangle ou un carré, si on ne le fait pas il est impossible de les reformer). Mais il ne faut pas effacer le fait que certains pions ont bougé, leur état a été changé lors de ce tour.
                        l.precedent = l.etat
                    
                    l.moved = 'no' # On met tous les points à 'no' pour le prochain tour



    # Le jeu en tant que tel devrait appeler deux boucles principales : Le premier tour, où les joueurs emplissent la planche, et le second, où il s'agit de déplacements.

    # Pile ou face.
quicommence = randint(0,2)
phaseun(quicommence) # test de la phase 1, tout devrait fonctionner correctement maintenant.

for k in triangles:  # test pour vérifier l'état des points après la phase 1 (permet de voir si la phase 1 s'est bien déroulée et de tester la phase 2)
    for l in k:      # On pourrait appeler cette boucle après chaque tour de la phase 2 pour aider le jeu en ligne de commande.
        print l.name, ':', l.etat, ':',l.precedent

phasedeux(quicommence) # test de la phase 2, il manque le traitement des mouvements forcés et l'intelligence artificielle.


