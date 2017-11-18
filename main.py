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

	listeRouteurs = l1 = [[205, 125], [205, 104], [205, 83], [205, 62], [181, 131], [181, 110], [181, 89], [181, 68], [181, 47], [160, 34], [158, 123], [158, 71], [139, 34], [137, 123], [137, 71], [118, 34], [97, 34], [93, 123], [93, 71], [76, 34], [72, 123], [72, 71], [116, 143], [51, 93], [48, 128], [48, 49], [116, 93], [160, 145], [139, 145], [95, 145], [74, 145], [51, 72], [116, 122], [116, 72], [33, 115], [33, 94], [33, 73], [33, 52], [136, 108], [136, 56], [71, 108], [71, 56], [158, 108], [158, 56], [93, 108], [93, 56], [160, 93], [139, 93], [95, 93], [74, 93], [116, 55], [59, 34], [51, 114], [202, 50], [181, 34], [59, 143], [181, 143], [33, 135], [116, 114], [196, 129], [137, 145], [51, 70], [215, 52], [137, 93], [72, 93], [204, 108], [204, 87], [190, 45], [47, 45], [46, 137], [204, 71], [157, 108], [157, 56], [136, 129], [136, 77], [92, 108], [92, 56], [71, 129], [71, 77], [41, 50], [190, 140], [207, 136], [58, 142]]
	#listeRouteurs = outils.placement_routeurV1(matrice,entete) #à décommenter pour faire tourner l'algo 30min
	arbreMini = outils.relierRouteurs(listeRouteurs) #Renvoie la liste des coordonnées de toutes les fibres à placer (routeurs compris)
	outils.ecrire_fichier(len(arbreMini),arbreMini,len(listeRouteurs),listeRouteurs)
