# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Purpose:
# Author:      Bastien
# Created:    X/10/2017
#-------------------------------------------------------------------------------

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

    fichier_map = open(file_link, "r")  #on ouvre le fichier à  lire

    for i in range(0, 3):   #on parcours l'entète
        variable_inutile = fichier_map.readline()   #on stock temporairement les éléments trouvés
        variable_inutile = []   #on vide les éléments trouvés précédemment

    while 1:    #on parcours l'ensemble des caractères de la map
        char = fichier_map.read(1)  #on récupère le caractère suivant
        if char == '\n':    #si c'est une fin de ligne
            matrice.append(ligneMatrice)    #on ajoute la ligne de matrice créée Ã  la matrice principale
            ligneMatrice = []   #on reset la ligne de matrice pour passer  la suivante
            pass
        elif not char:  #si aucun caractère n'est récupéré, fin de fichier, on sort de la boucle
            break
        else:   #sinon (caractère trouvé)
            ligneMatrice.append(char)   #on ajoute le caractère récupéré à  la fin de la ligne de matrice en cours de création

    fichier_map.close() #on ferme le fichier ouvert

    return matrice  #on renvoie la matrice créée

""" Main -> Dans le code calcul_cases_couvertes de Arthur """