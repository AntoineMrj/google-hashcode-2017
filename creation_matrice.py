# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Purpose: renvoie la matrice complète du fichier d'entré
# Author:      Bastien
# Created:    11/11/2017
#-------------------------------------------------------------------------------

#entré : nom du fichier d'entré
def creationMatrice(file_name):
	matrice = []    #matrice pincipale
	ligneMatrice = []   #ligne d'une matrice

	fichier_map = open(file_name, "r")  #on ouvre le fichier d'entré en mode lecture

	for i in range(0, 3):   #on parcours l'entête
		variable_inutile = fichier_map.readline()   #on stock temporairement les éléments trouvés
		variable_inutile = []   #on vide les éléments trouvés précédemment

	while 1:    #on parcours l'ensemble des caractères de la map
		char = fichier_map.read(1)  #on récupère le caractère suivant
		if char == '\n':    #si c'est une fin de ligne
			matrice.append(ligneMatrice)    #on ajoute la ligne de matrice créée à la matrice principale
			ligneMatrice = []   #on reset la ligne de matrice pour passer  la suivante
		elif not char:  #si aucun caractère n'est récupéré, fin de fichier, on sort de la boucle
			break
		else:   #sinon (caractère trouvé)
			ligneMatrice.append(char)   #on ajoute le caractère récupéré à la fin de la ligne de matrice en cours de création

	fichier_map.close() #on ferme le fichier ouvert

	return matrice  #on renvoie la matrice créée
