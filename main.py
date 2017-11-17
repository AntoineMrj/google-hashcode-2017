# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:50:02 2017

@author: Antoine
"""

import outils
 
if __name__ == "__main__":
    
#-------------------------------------------------
	""" LECTURE DE LA MAP  : Code lecture_entete.py """
	map="charleston_road.in"               #Choix de la map   ( ex : charleston_road.in )
	entete = outils.lectureEntete(map)
	#print(entete)               #affichage de l'entète, on attrape ici toute les info du fichier .in (en char)
	matrice = outils.creationMatrice(map)    #notre matrice
#-------------------------------------------------

#	affichage_matrice(matrice)
	#print(cases_couvertes(matrice,19,5,3,22,8))

	backbone = [int(entete[6]), int(entete[7])]   #on recupère les coord du backbone pour les ajouter à la liste de routeurs
	listeRouteurs = [[181, 131], [205, 125], [158, 123], [137, 123], [93, 123], [72, 123], [181, 110], [205, 104], [181, 89], [205, 83], [158, 71], [137, 71], [93, 71], [72, 71], [181, 68], [205, 62], [181, 47], [160, 34], [139, 34], [118, 34], [97, 34], [76, 34], [116, 143], [51, 93], [48, 128], [48, 49], [116, 93], [160, 145], [139, 145], [95, 145], [74, 145], [51, 72], [116, 122], [116, 72], [33, 115], [33, 94], [33, 73], [33, 52], [136, 108], [71, 108], [136, 56], [71, 56], [158, 108], [93, 108], [158, 56], [93, 56], [160, 93], [139, 93], [95, 93], [74, 93], [116, 55], [59, 34], [51, 114], [202, 50], [181, 34], [59, 143], [181, 143], [33, 135], [116, 114], [194, 130], [137, 145], [51, 70], [215, 52], [137, 93], [72, 93], [204, 109], [204, 88], [190, 45], [44, 47], [46, 137], [204, 71], [136, 129], [71, 129], [157, 108], [92, 108], [136, 77], [71, 77], [157, 56], [92, 56], [56, 45], [207, 136], [41, 51], [190, 141], [58, 142]]
	#listeRouteurs = outils.placement_routeurV1(matrice,entete) #à décommenter pour faire tourner l'algo 30min
	arbreMini = outils.relierRouteurs(listeRouteurs,backbone) #Renvoie la liste des coordonnées de toutes les fibres à placer (routeurs compris)
	outils.ecrire_fichier(len(arbreMini),arbreMini,len(listeRouteurs),listeRouteurs)
