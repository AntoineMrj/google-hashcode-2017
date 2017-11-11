# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Purpose: renvoie l'entête complète du fichier d'entré dans une liste
# Author:      Bastien
# Created:    11/11/2017
#-------------------------------------------------------------------------------

#entré : nom du fichier d'entré
def lectureEntete(file_name):
    fichier_map = open(file_name, "r")  #on ouvre le fichier d'entré en mode lecture
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
