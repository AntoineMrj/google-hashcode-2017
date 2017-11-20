# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:50:02 2017

@author: Antoine
"""

import numpy as np
import threading
from multiprocessing import Process, Pipe

def distance(pointA,pointB): #où pointA = (xA,yA) et pointB = (xB,yB)
    dist = ((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)**0.5
    return dist

def relier2points(point1, point2):
    """
    Retourne le chemin le plus court pour relier 2 points dans une matrice donnée
    sous forme d'une liste de couple de coordonnées (x,y)
    On utilise l'algorithme de Bresenham
    """
    x1, x2, y1, y2 = point1[0], point2[0], point1[1], point2[1] #Récupération des coordonnées des 2 points donnés en paramètre
     
    dx = x2 - x1 #On calcule la distance relative entre le point 1 et 2 horizontalement
    dy = y2 - y1 #On calcule la distance relative entre le point 1 et 2 verticalement
    pente = abs(dy) > abs(dx) #Si la pente verticale est supérieure à la pente horizontale pente vaut True sinon elle vaut False
 
    #On tourne la ligne si la pente verticale est supérieur à celle horizontale, la variable pente nous servira pour savoir si la on a tourné la ligne ou non
    if abs(dy) > abs(dx):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    #Si le point 1 est situé après le point 2 (d'un point de vue horizontal) on echange leurs coordonnées
    echange = False
    if x1 > x2:
        x1, x2 = x2, x1 #On inverse x1 et x2
        y1, y2 = y2, y1 #On inverse y1 et y2
        echange = True #On garde en memoire le fait que les points sont inversés, cela servira à la fin pour retourner la liste de points en sens inverse
 
    '''
    NOTE : On s'arrange toujours pour avoir un pente verticale inférieure à la pente horizontale et 
    pour aller de gauche à droite (cela permet de faire tourner un algorithme général et modifier la liste
    finale de points en fonction des conditions initiales plutôt que de faire tourner un algorithme par cas
    qui rendrait le code beaucoup plus long)
    Par cas on entend par exemple "le point 2 est a gauche du point 1", "le point 2 est sur la diagonale droite inférieure" etc... 
    '''
    
    # On recalcule les nouveaux dx et dy dans le cas où la ligne aurait été retournée ou les points inversés
    dx = x2 - x1
    dy = y2 - y1
 
    # On calcul l'erreur qui vaut la valeur entière de la distance horizontale entre les 2 points divisée par 2
    erreur = int(dx / 2.0) 
    if y1 < y2: #Si le point 1 est plus bas que le point 2
        pasY = 1 #on incrémentera la valeur de y qui correspond à l'ordonnée suivante
    else:
        pasY = -1 #On décrémentera la valeur de y qui correspond à l'ordonnée suivante, en clair on prendra le point en dessous de celle actuelle
    #En résumé si le point 1 est au dessus du point 2 on sait qu'il faudra choisir entre le pixel du dessous et celui à côté alors que dans l'autre cas il faudra choisir entre celui du dessus et celui à côté
    
    y = y1 #on initialise y qui correspond à l'ordonnée du premier point par lequel passer
    points = [] #On initialise le tableau des points à emprunter
    # Boucle qui calcule les différents points à emprunter pour aller du point 1 au point 2
    for x in range(x1, x2 + 1): #Pour x allant de l'abscisse du premier point à celle du dernier +1
        if pente: #si la ligne a été tournée
            coord = (y, x) #on retourne le point en inversant x et y
        else:
            coord = (x, y) #sinon on retourne le "vrai" point
        points.append(coord) #On ajoute le point à la liste des points à emprunter
        erreur -= abs(dy) #On soustrait différence de hauteur entre les 2 points à l'erreur 
        if erreur < 0: #Si l'erreur est négative
            y += pasY #On choisit le point juste au dessus ou en dessous en fonction de la valeur de pasY
            erreur += dx #On ajoute à l'erreur la distance entre le point 1 et le point2
 
    if echange: #si on a inversé les points on retourne la liste des points à l'envers
        points.reverse()
    return points


def relierRouteurs(liste_routeurs, backbone):
    
    """Cette fonction permet de déterminer l'arbre couvrant minimum reliant tous les routeurs présents dans liste_routeurs. L'algorithme utilisé
    est l'algorithme de Prim."""

    #===================================================
    #DETERMINATION DES LISTES 'ARBRE', 'DIST' ET 'PRED'
    #===================================================
    
    n = len(liste_routeurs)
    arbre = [backbone] #l'arbre initial contient les coordonnées du backbone
    dist = [+float('inf')]*n #on initialise la liste des distances à +infini
    pred = [None]*n #on initialise la liste des prédecessuers à None
    
    while len(arbre) < n+1: #tant que l'on a pas ajouté tout les routeurs de liste_routeurs dans arbre
        
        for i in range(n): #pour chaque routeur_i dans liste_routeurs
            
                dist_i = distance(arbre[-1],liste_routeurs[i]) #on calcule la distance entre le routeur_i est le dernier routeur entré dans l'arbre
                
                if dist[i] != None: #si le routeur n'est pas déjà dans l'arbre en cours de construction
                    if dist_i < dist[i]: #si la distance calculée est inférieure à la dernière distance enregistrée dans la liste 'dist'
                        dist[i] = dist_i #alors on met à jour la liste 'dist' avce la nouvelle distance qui vient d'être calculée
                        pred[i] = arbre[-1] #et on met à jour la liste 'pred' en indiquant que le prédecesseur du routeur_i est le dernier routeur entré dans l'arbre
        
        mini = +float('inf') #ici...
        for d in dist: #...on caclule...
          if d != None: #...le minimum de...
            if d < mini: #...la liste 'dist'.
                mini = d
        

        for j in range(len(dist)): #pour chaque distance_j dans la liste 'dist'
            if dist[j] == mini: #si la distance_j correspond à la distance minimum
                arbre.append(liste_routeurs[j]) #alors on fait rentrer dans l'arbre le routeur_j qui est à la distance minimum de l'arbre
                dist[j] = None #on met à jour la distance du routeur_j à None puisqu'il vient de rentrr dans l'arbre
                break #on force l'arrêt de la boucle for pour éviter qu'un 2ème routeur, étant aussi à la distance minimum de l'arbre, rentre dans l'arbre

    
    #============================================================================
    #RELIER LES ROUTEURS A LEUR PREDECESSEUR AVEC LA FIBRE EN PARTANT DU BACKBONE
    #============================================================================

    fibre = [] #on initialise la liste 'fibre' qui contiendra toutes les coordonnées des points où passe la fibre
    
    for i in range(0,len(liste_routeurs)): #pour chaque routeur_i dans liste_routeurs
        portion_chemin_i = relier2points(pred[i],liste_routeurs[i]) #on détermine la liste des coordonnées des points reliant le routeur_i à son prédecesseur_i en utilisant la fontion d'Antoine
        fibre += portion_chemin_i #on incrémente la liste 'fibre' de la liste calculée précédemment
        
    """On a maintenant la liste de tous les points fibrés, mais pour que le simulateur en ligne puisse l'interpréter, il faut l'ordonner de telle
    façon que:
            - le premier point fibré de la liste soit voisin du backbone
            - tous les points fibrés suivants devont être voisins au moins à:
                    > l'un des points situés devant eux dans la liste
                    > ou à l'un des routeurs posés
    
    Pour cela, on ne va pas modoifier la liste 'fibre' directement, mais on va créer une 2ème liste 'fibre_ordonee' dans laquelle on fera rentrer
    au fur et à mesure les points fibrés dans le bon ordre.
    
    Enfin, on créera une 3ème et dernière liste 'fibre_finale' qui sera identique à 'fibre_ordonee' mais sans le backbone et sans les doublons.
    C'est cette liste que la fonction renvoie.
    """
    
    fibre_ordonee = [backbone] #on initialise la liste ordonnée avec le backbone
    fibre_finale = [] #on initialise la liste finale
    fin = False #cette variable booléenne permet de s'assurer que tous les éléments de 'fibre' sont bien dans 'fibre_ordonee', on l'initialise donc à False
    
    while fin == False: #tant que tous les éléments de 'fibre' ne sont pas dans 'fibre_ordonee'
        
        i = 0
        while i < len(fibre): #pour chaque point_fibré_i de la liste 'fibre'
            #si le point_fibré_i a un voisin dans la liste ordonée ou dans la liste des routeurs
            #ET s'il n'est pas un routeur ou un point déja dans la liste ordonée
            if ((((fibre[i][0]+1,fibre[i][1]) in fibre_ordonee) or ((fibre[i][0]+1,fibre[i][1]) in liste_routeurs)) \
            or (((fibre[i][0]-1,fibre[i][1]) in fibre_ordonee) or ((fibre[i][0]-1,fibre[i][1]) in liste_routeurs)) \
            or (((fibre[i][0],fibre[i][1]+1) in fibre_ordonee) or ((fibre[i][0],fibre[i][1]+1) in liste_routeurs)) \
            or (((fibre[i][0],fibre[i][1]-1) in fibre_ordonee) or ((fibre[i][0],fibre[i][1]-1) in liste_routeurs)) \
            or (((fibre[i][0]+1,fibre[i][1]+1) in fibre_ordonee) or ((fibre[i][0]+1,fibre[i][1]+1) in liste_routeurs)) \
            or (((fibre[i][0]-1,fibre[i][1]-1) in fibre_ordonee) or ((fibre[i][0]-1,fibre[i][1]-1) in liste_routeurs)) \
            or (((fibre[i][0]+1,fibre[i][1]-1) in fibre_ordonee) or ((fibre[i][0]+1,fibre[i][1]-1) in liste_routeurs)) \
            or (((fibre[i][0]-1,fibre[i][1]+1) in fibre_ordonee) or ((fibre[i][0]-1,fibre[i][1]+1) in liste_routeurs)) \
            and (fibre[i] not in fibre_ordonee and fibre[i] not in liste_routeurs)):
                fibre_ordonee.append(fibre[i]) #alors on l'ajoute à la liste ordonée
                fibre.remove(fibre[i]) #et on le supprime de la liste 'fibre'
                i-=1 #on décrémente l'indice i de 1 (car sinon 'index out of range")
            i+=1 #on incrémente i de 1
        
        test = True
        for point in fibre: #pour chaque point dans 'fibre'
            if point not in fibre_ordonee: #s'il n'est pas dans 'fibre_ordonee'
                test = False #alors le test renvoie False
            else: #sinon
                test = test and True #alors le test renvoie True AND la valeur du test précédent (donc si un seul point de 'fibre' n'est pas dans 'fibre_ordonee', le test renvoie False)
        
        if test == True: #si tous les points de 'fibre' sont dans 'fibre_ordonee'
            fin = True #alors c'est fini
        else: #sinon
            fin = False #ce n'est pas fini ^^
            
        #print(test) #j'affiche la valeur de test pour être sûr que l'algo tourne pas dans le vide ^^
    
    for point in fibre_ordonee: #on élimine les doublons
        if point not in fibre_finale: #si le point de 'fibre_ordonee' n'est pas déjà dans 'fibre_finale'
            fibre_finale.append(point) #alors il n'a pas de doublon et on peut l'ajouter à 'fibre_finale'

    for point in fibre_finale: #on élimine le backbone dans 'fibre_finale'
        if point == backbone:
            fibre_finale.remove(point)
    
    return fibre_finale


#entête : nombre de cables posés, liste des coordonnées des cases de cable, nombre de routeur, liste des coordonnées des routeurs
def ecrire_fichier(nb_cabl, liste_coord_cabl, nb_rout, liste_coord_rout):
    with open("coord.out", "w") as fichier: #ouvre le fichier de sortie (le créé si non existant)
        if nb_cabl == len(liste_coord_cabl):    #on verifie les donnees liees aux cables
            fichier.write(str(nb_cabl) + "\n")  #on ecrit le nombre de cable dans le fichier

            for coord_cabl in range(0, nb_cabl):    #on parcours chacunes des coordonnees des cables
                fichier.write(str(liste_coord_cabl[coord_cabl][0]) + " ")   #on ecrit la coordonnee x dans le fichier
                fichier.write(str(liste_coord_cabl[coord_cabl][1]) + "\n")  #on ecrit la coordonnee y dans le fichier
        else:   #si erreur dans les donnees liees aux cables
            print("Le nombre de cable specifie n'est pas egal au nombres de coordonne de cable") #on affiche un message d'erreur

        if nb_rout == len(liste_coord_rout):    #on verifie les donnees liees aux routeurs
            fichier.write(str(nb_rout) + "\n")  #on ecrit le nombre de routeur dans le fichier

            for coord_rout in range(0, nb_rout):    #on parcours chacunes des coordonnees des routeurs
                fichier.write(str(liste_coord_rout[coord_rout][0]) + " ")   #on ecrit la coordonnee x dans le fichier
                fichier.write(str(liste_coord_rout[coord_rout][1]) + "\n")  #on ecrit la coordonnee y dans le fichier
        else:   #si erreur dans les donnees liees aux routeurs
            print("Le nombre de routeur specifie n'est pas egal au nombres de coordonne de routeur")    #on affiche un message d'erreur

        fichier.close() #on ferme le fichier ouvert

def lectureEntete(file_link):
    fichier_map = open(file_link, "r")  #on ouvre le fichier à lire en mode lecture
    premiere_ligne_entete = fichier_map.readline()  #on lit la première ligne
    deuxieme_ligne_entete = fichier_map.readline()  #on lit la deuxième ligne
    troisieme_ligne_entete = fichier_map.readline() #on lit la troisième ligne

    liste_premiere_ligne_entete = premiere_ligne_entete.split() #on sépare les éléments de la première ligne
    liste_deuxieme_ligne_entete = deuxieme_ligne_entete.split() #on sépare les éléments de la deuxième ligne
    liste_troisieme_ligne_entete = troisieme_ligne_entete.split()   #on sépare les éléments de la troisième ligne

    nb_ligne = liste_premiere_ligne_entete[0]  #nb_ligne : nombre de ligne
    nb_col = liste_premiere_ligne_entete[1]  #nb_col : nombre de colonne
    portee_routeur = liste_premiere_ligne_entete[2]  #portee_routeur : portée d'un routeur

    prix_fil = liste_deuxieme_ligne_entete[0] #prix_fil : prix d'un fil
    prix_routeur = liste_deuxieme_ligne_entete[1] #prix_routeur : prix d'un routeur
    budget_max = liste_deuxieme_ligne_entete[2]  #budget_max : budget maximum

    coord_y_backbone = liste_troisieme_ligne_entete[0]    #coord_y_backbone : coordonnée y du routeur principal
    coord_x_backbone = liste_troisieme_ligne_entete[1]    #coord_x_backbone : coordonnée x du routeur principal

    fichier_map.close() #on ferme le fichier ouvert

    return nb_ligne, nb_col, portee_routeur, prix_fil, prix_routeur, budget_max, coord_y_backbone, coord_x_backbone #on renvoie l'ensemble des éléments


def creationMatrice(file_link):
    matrice = []    #matrice pincipale
    ligneMatrice = []   #ligne d'une matrice

    fichier_map = open(file_link, "r")  #on ouvre le fichier à  lire

    for i in range(0, 3):   #on parcours l'entète
        variable_inutile = fichier_map.readline()   #on stock temporairement les éléments trouvés
        variable_inutile = []   #on vide les éléments trouvés précédemment

    while 1:    #on parcours l'ensemble des caractères de la map
        char = fichier_map.read(1)  #on récupère le caractère suivant
        if char == '\n':    #si c'est une fin de ligne
            matrice.append(ligneMatrice)    #on ajoute la ligne de matrice créée Ã  la matrice principale
            ligneMatrice = []   #on reset la ligne de matrice pour passer  la suivante
            pass
        elif not char:  #si aucun caractère n'est récupéré, fin de fichier, on sort de la boucle
            break
        else:   #sinon (caractère trouvé)
            ligneMatrice.append(char)   #on ajoute le caractère récupéré à  la fin de la ligne de matrice en cours de création

    fichier_map.close() #on ferme le fichier ouvert

    return matrice  #on renvoie la matrice créée

#entrée : la matrice (avec les cases déjà couvertes remplacées (x)), coordonnées du routeur,
#         rayon du routeur, largeur et hauteur de la matrice
def cases_couvertes(matrice, coordX_routeur, coordY_routeur, radius, largeur_matrice, hauteur_matrice):

    #matrice de travail
    map_travail = matrice

    #variables passées dans la fonction
    x = coordX_routeur
    y = coordY_routeur
    l = largeur_matrice
    h = hauteur_matrice

    #coordonnées d'origine du carré autour du routeur
    x_origin = x - radius
    y_origin = y - radius
    #coordonnées de fin du carré autour du routeur
    x_fin = x + radius
    y_fin = y + radius

    #coordonnées d'origine du carré entre la case étudiée et le routeur
    deb_x_mur = 0
    deb_y_mur = 0
    #coordonnées de fin du carré entre la case étudiée et le routeur
    fin_x_mur = 0
    fin_y_mur = 0

    #listes des cases couvertes
    liste_cases_couvertes = []

    #listes des cases non couvertes
    liste_cases_non_couvertes = []

    #on vérifie la position du routeur (cellule '.')
    if (map_travail[y][x] == '.'):

        #mise à jour des cases couvertes sur la map
        #on parcours chaque ligne du carré étudié
        for y_coord in range(y_origin, y_fin + 1):
            #on vérifie que la ligne de la case étudiée soit à l'intérieur de la matrice
            if (y_coord >= 0 and y_coord < h):
                #on parcours chaque colonne du carré étudié
                for x_coord in range (x_origin, x_fin + 1):
                    #on vérifie que la colonne de la case étudiée soit à l'intérieur de la matrice
                    if (x_coord >= 0 and x_coord < l):
                        #on ajoute temporairement la cases à la liste de celles couvertes
                        liste_cases_couvertes.append([x_coord, y_coord])
                        #on regarde si la case testée n'est pas déjà non couverte
                        if [x_coord, y_coord] not in liste_cases_non_couvertes:
                            #on vérifie que la case étudiée s'agit d'une cellule '.'
                            if (map_travail[y_coord][x_coord] == '#'):
                                #on compare la position de la ligne de la case étudié et la ligne du routeur
                                if (x_coord < x):
                                    deb_x_mur = x_origin
                                    fin_x_mur = x_coord
                                elif (x_coord > x):
                                    deb_x_mur = x_coord
                                    fin_x_mur = x_fin
                                else:
                                    deb_x_mur = x_origin
                                    fin_x_mur = x_fin
                                #on compare la position de la colonne de la case étudié et la colonne du routeur
                                if (y_coord < y):
                                    deb_y_mur = y_origin
                                    fin_y_mur = y_coord
                                elif (y_coord > y):
                                    deb_y_mur = y_coord
                                    fin_y_mur = y_fin
                                else:
                                    deb_y_mur = y_origin
                                    fin_y_mur = y_fin
                                #on met à jour la liste des cases non couverte par le mur actuel
                                for y_mur in range (deb_y_mur, fin_y_mur + 1):
                                    for x_mur in range (deb_x_mur, fin_x_mur + 1):
                                        if [x_mur, y_mur] not in liste_cases_non_couvertes:
                                            liste_cases_non_couvertes.append([x_mur, y_mur])
                        else:
                            pass
        #on supprimer les cases non couvertes de la liste des cases couvertes
        for i in range (0, len(liste_cases_non_couvertes)):
            liste_cases_couvertes.remove(liste_cases_non_couvertes[i])

    else:
        #si cellule incorrect (vide ou mur) on envoie 0 pour stoper la fonction
        return 0

    #fin
    return liste_cases_couvertes

def prix(nb_routeurs,nb_fibre,Pf,Pr):
    #Pr est le prix d'un routeur
    #Pb est le prix d'une fibre
    #B est le budget
    prix = nb_routeurs * Pr + nb_fibre * Pf

    return prix
    
def calcule_score2(carte,bonus,largeur_map,hauteur_map,perim_routeur,conn,liste_case):
    liste_score2=[] 
    for i in range(0,len(liste_case)-6,6):
        X=liste_case[i+bonus][0]
        Y=liste_case[i+bonus][1]
        if carte[X][Y] == '.' or carte[X][Y] == 'w':
            liste_case_couverte = cases_couvertes(carte,Y,X,perim_routeur,largeur_map,hauteur_map)
            if liste_case_couverte!=0:
                score=len(liste_case_couverte)*1000 #On calacul le score 
                liste_score2.append([score,X,Y])
    conn.send(liste_score2)
    conn.close()
    
def placement_routeurV1(plan,data):
    map_travail=plan
    liste_routeur=[]
    budget = int(data[5])           
    hauteur_map = int(data[0])      
    largeur_map = int(data[1])      
    perim_routeur = int(data[2])
    prix_routeur = int(data[4])
    taillemap = hauteur_map*largeur_map     
    cout=0
    passage = 0
    case_restante = 0
    liste_case = []
#on calcule le nombre de case à couvrir
    for i in range(hauteur_map):
        for k in range(largeur_map):
            if map_travail[i][k] == '.':
                case_restante=case_restante+1
                liste_case.append([i,k])
    print("Case à couvrir :",case_restante," Budget :",budget)  

#Tant que l'on a du budget ou qu'il reste des case à couvrir on fait le test
    while budget-cout>prix_routeur and case_restante> 0:
        liste_score_routeur=[]

        parent_conn1, child_conn1 = Pipe()
        t1 = Process( target=calcule_score2, args=(map_travail,0,largeur_map,hauteur_map,perim_routeur,child_conn1,liste_case ) )
        parent_conn2, child_conn2 = Pipe()
        t2 = Process( target=calcule_score2, args=(map_travail,1,largeur_map,hauteur_map,perim_routeur,child_conn2,liste_case ) )
        parent_conn3, child_conn3 = Pipe()
        t3 = Process( target=calcule_score2, args=(map_travail,2,largeur_map,hauteur_map,perim_routeur,child_conn3,liste_case ) )
        parent_conn4, child_conn4 = Pipe()
        t4 = Process( target=calcule_score2, args=(map_travail,3,largeur_map,hauteur_map,perim_routeur,child_conn4,liste_case ) )
        parent_conn5, child_conn5 = Pipe()
        t5 = Process( target=calcule_score2, args=(map_travail,4,largeur_map,hauteur_map,perim_routeur,child_conn5,liste_case ) )
        parent_conn6, child_conn6 = Pipe()
        t6 = Process( target=calcule_score2, args=(map_travail,5,largeur_map,hauteur_map,perim_routeur,child_conn6,liste_case ) )
        
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        liste_score1 = parent_conn1.recv()
        liste_score2 = parent_conn2.recv()
        liste_score3 = parent_conn3.recv()
        liste_score4 = parent_conn4.recv()
        liste_score5 = parent_conn5.recv()
        liste_score6 = parent_conn6.recv()

        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        liste_score_routeur = liste_score1 + liste_score2 +liste_score3 + liste_score4 + liste_score5 + liste_score6
        liste_score_routeur.sort(reverse=True) #Quand toute les case on été testé, on classe les routeur par leur score
        liste_routeur.append([liste_score_routeur[0][1],liste_score_routeur[0][2]])#On garde le meilleur et on le met en place
        liste_case.remove([liste_score_routeur[0][1],liste_score_routeur[0][2]])
        cout=cout+prix_routeur          #On met à  jour le budget pour vérifier quer l'on peut continuer
        print("cout :",cout,)
        
        #Modification de la matrice pour que les cases déjà  couverte ne puissent plus rapporter de points
        liste_case_couverte = cases_couvertes(map_travail,liste_score_routeur[0][2],liste_score_routeur[0][1],perim_routeur,largeur_map,hauteur_map)        

        for i in range(len(liste_case_couverte)):
            map_travail[liste_case_couverte[i][1]][liste_case_couverte[i][0]]="w"           
        map_travail[liste_score_routeur[0][1]][liste_score_routeur[0][2]] = "R"


        #on enregistre la carte dans un fichier à part
        passage = passage +1
        numpassage = str(passage)
        nommap = "map2-passage " + numpassage
        np.savetxt(nommap, map_travail, delimiter="",fmt="%s")
        case_restante=case_restante-len(liste_case_couverte)
        
        print("routeur",liste_routeur)
        print("case restante à couvrir :",case_restante)
        print(" ")
    print("Fini")
    return liste_routeur
