# -*- coding: utf-8 -*-

import lecture_entete    #code de Bastien

#-------------------------------------------------------------------------------
# Purpose: renvoie les cases qui seront couvertes en excluant les cases déja  couvertes avant et renvoie aussi le score que le routeur vas nous apporter
# Author:      Arthur MILLET
# Created:     31/10/2017
#-------------------------------------------------------------------------------


def creation_backbone():      #on affiche le backbone sur la map

    coord_y_backbone = int(entete[6])    #on recupère les coord sur le return de la lecture entete
    coord_x_backbone = int(entete[7])
    matrice[coord_y_backbone][coord_x_backbone]='b'    #il prend la valeur de b


def affichage_matrice(mat):     #entrée : la matrice

        for i in range (0, len(mat)):       #on parcours la totalité des lignes de la matrice
            for j in range(0, len(mat[i])):     #on parcours la totalité du noimbre de colonnes de la matrice
                print(mat[i][j], end="")        #on affiche l'élément sans retour à  la ligne
            print()


def lecture_cases_couvertes(mat):    #ajoute dans une liste les cases couvertes

    liste_cases_couvertes = []

    for i in range (0, len(mat)):   #on parcours la totalité des lignes de la matrice

        for j in range(0, len(mat[i])):                      #on parcours la totalité du noimbre de colonnes de la matrice
            if mat[i][j]=='x' or mat[i][j]=='r' or mat[i][j]=='b' :     #r et b = cible marqué par la wifi pour le comptage des points  ->  POSE UN SOUCIS AVEC b CAR COMMENT SAVOIR SI IL EST WIFI???
                mon_tuple=(i,j)                             #creation tuple de la position
                liste_cases_couvertes.append(mon_tuple)       #ajout de la position

    return liste_cases_couvertes


def calcul_cases_couvertes(mat, routeur_y, routeur_x, p_routeur,n_routeur):    #entrée : la matrice, coord du router à ajouter, porté du routeur  (on peut rajouter le nb de cases couvertes ?!)

    #affichage cases couvertes avant
    cases_couvertes1=lecture_cases_couvertes(matrice)
    print("Nombre de cases couvertes avec le routeur :", n_routeur-1 ," -> ", len(lecture_cases_couvertes(matrice)))
    print("Les cases couvertes au début sont :", lecture_cases_couvertes(matrice))

    matrice[routeur_y][routeur_x]='r'    #ajout du nouveau routeur

    for i in range (0, len(mat)):        #ajout des cible marqué par la wifi
        for j in range(0, len(mat[i])):

            if abs(routeur_y - i) <= p_routeur and abs(routeur_x - j) <= p_routeur :
                #if (i , j) != (routeur_y , routeur_x) :     #si la case n'est pas la case du routeur
                if matrice[i][j] != 'r' :                 #si la case n'est pas la case du routeur
                    if matrice[i][j] != '#' :       #si c'est pas un mur
                        if matrice[i][j] != '-' :       #si c'est pas une case à ne pas remplir
                            if matrice[i][j] != 'b' :       #si c'est pas le backbone
                                matrice[i][j]='x'            #POUR L INSTANT PAS DE SOUCIS DE BORDURE AVEC LA MAT

    #affichage cases couvertes apres
    print("Nombre de cases couvertes avec le routeur :", n_routeur ," -> ", len(lecture_cases_couvertes(matrice)))
    print("Les cases couvertes à la fin sont :", lecture_cases_couvertes(matrice))
    print()

    return affichage_matrice(matrice) , print(len(cases_couvertes1)*1000) , print(len(lecture_cases_couvertes(matrice))*1000), print("le routeur", n_routeur, "rapporte en plus: ",len(lecture_cases_couvertes(matrice))*1000 - len(cases_couvertes1)*1000)

# sortie :  affiche la matrice avec les modifs cad nouvelle cases couvertes grace à ce routeur (sans compter 2x les n+x cases couvertes),
# ancien score, nouveau score (=le nombres de cases couvertes total), le delta entre les deux


if __name__ == '__main__':

#-------------------------------------------------

    """ LECTURE DE LA MAP  : Code lecture_entete.py """

    map="map0.in"               #Choix de la map   ( ex : charleston_road.in )
    entete = lecture_entete.lectureEntete(map)
    #print(entete)               #affichage de l'entète, on attrape ici toute les info du fichier .in (en char)
    print()
    matrice = lecture_entete.creationMatrice(map)    #notre matrice

#-------------------------------------------------

    print("Nom de la Map : ",map), print()      #nom de la map

    creation_backbone()             #affiche sur la carte "b"
    affichage_matrice(matrice)      #affichage de la map

    """ ROUTEUR X """

    #coord_y_routeur1 = int(input("Entrer y (ligne) du routeur 1 :"))    #position du routeur à ajouter
    #coord_x_routeur1 = int(input("Entrer x (colonne) du routeur 1 :"))

    #ATTENTION A LA TAILLE DE LA MAT, faut borner à l'interieur des murs!
    #ET SI ON CHOISI UNE CASES OU C EST UN MUR ON REDEMANDE A L UTILISATEUR UNE NOUVELLE CASE (pareil si c'est pas un entier rentrer)

    """ ROUTEUR 1 """

    coord_x_routeur1 = 6   #colone(j)
    coord_y_routeur1 = 3   #ligne (i)

    print()
    calcul_cases_couvertes(matrice , coord_y_routeur1 , coord_x_routeur1 , int(entete[2]), 1)   #ajout du routeur et des points avec le wifi sur la carte
    print()

    """ ROUTEUR 2 """

    coord_x_routeur2 = 9   #colone(j)
    coord_y_routeur2 = 3   #ligne (i)

    print()
    calcul_cases_couvertes(matrice , coord_y_routeur2 , coord_x_routeur2 , int(entete[2]), 2)
