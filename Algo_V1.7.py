# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Purpose: Placer le routeur
# Author:      Guilllaume
# MAJ:     10/11/2017
#-------------------------------------------------------------------------------
import numpy as np
import threading
from multiprocessing import Process, Pipe



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


#entrée : la matrice (avec les cases déjà couvertes remplacées (x)), coordonnées du routeur,
#         rayon du routeur, largeur et hauteur de la matrice
def cases_couvertes(matrice, coordX_routeur, coordY_routeur, radius, largeur_matrice, hauteur_matrice):
	#matrice de travail
	map_travail_1 = matrice

	#variables passées dans la fonction
	x = coordX_routeur
	y = coordY_routeur
	h = hauteur_matrice
	l = largeur_matrice

	#coordonnées d'origine du carré autour du routeur
	x_origin = x - radius
	y_origin = y - radius
	#coordonnées de fin du carré autour du routeur
	x_fin = x + radius
	y_fin = y + radius

	#coordonnées d'origine du carré entre la case étudiée et le routeur
	x_origin_case_test = 0
	y_origin_case_test = 0
	#coordonnées de fin du carré entre la case étudiée et le routeur
	x_fin_case_test = 0
	y_fin_case_test = 0

	#variable vérifiant la présence d'un mur ou non
	presence_mur = False

	#listes des cases couvertes
	liste_cases_couvertes = []

	#on vérifie la position du routeur (cellule '.')
	if (map_travail_1[y][x] == '.') or (map_travail_1[y][x] == 'w'):

		#mise à jour des cases couvertes sur la map
		#on parcours chaque ligne du carré étudié
		for y_coord in range(y_origin, y_fin+1):
			#on vérifie que la ligne de la case étudiée soit à l'intérieur de la matrice
			if (y_coord >= 0 and y_coord < h):
				#on parcours chaque colonne du carré étudié
				for x_coord in range (x_origin, x_fin+1):
					#on vérifie que la colonne de la case étudiée soit à l'intérieur de la matrice
					if (x_coord >= 0 and x_coord < l):
						#on vérifie que la case étudiée s'agit d'une cellule '.'
						if (map_travail_1[y_coord][x_coord] == '.'):
							#on compare la position de la colonne de la case étudié et la colonne du routeur
							if (y_coord < y):
								y_origin_case_test = y_coord
								y_fin_case_test = y
							elif (y_coord > y):
								y_origin_case_test = y
								y_fin_case_test = y_coord
							else:
								y_origin_case_test = y
								y_fin_case_test = y
							#on compare la position de la ligne de la case étudié et la ligne du routeur
							if (x_coord < x):
								x_origin_case_test = x_coord
								x_fin_case_test = x
							elif (x_coord > x):
								x_origin_case_test = x
								x_fin_case_test = x_coord
							else:
								x_origin_case_test = x
								x_fin_case_test = x

							#on parcours l'ensemble du carré entre la case étudiée et le routeur pour vérifier la présence d'un mur ou non
							#on parcours chaque colonne
							for y_coord_case_test in range(y_origin_case_test, y_fin_case_test+1):
								#on parcours chaque ligne
								for x_coord_case_test in range(x_origin_case_test, x_fin_case_test+1):
									#si présence d'une cellule mur '#'
									if (map_travail_1[y_coord_case_test][x_coord_case_test] == '#'):
										#activation de la variable de présence
										presence_mur = True
									else:
										#reset de la variable de présence
										presence_mur = False
									#on vérifie l'état de la variable de présence
									if (presence_mur):
										#si présence d'un mur on stop le parcours des lignes restantes
										break
								#on vérifie l'état de la variable de présence
								if (presence_mur == True):
									#si présence d'un mur on stop le parcours des colonnes restantes
									break
							#on vérifie l'état de la variable de présence
							if (presence_mur == False): #ajout de la case étudiée à la liste des cases couvertes
								#matrice[y_coord][x_coord]='x'           #affichage cord
								liste_cases_couvertes.append([x_coord, y_coord])
								#matrice[y][x]='r'           #affichage corrd routeur


	else:
		#si cellule incorrect (vie ou mur) on envoie 0 pour stoper la fonction
		return 0

	#fin
	return liste_cases_couvertes

def calcule_score(carte,boneinf,bonesup,largeur_map,hauteur_map,perim_routeur,conn):
	temoin=0
	temoin2=0
	liste_score1=[]
	for i in range(boneinf,bonesup):
		coordY=i
		for k in range(largeur_map):
			coordX=k
			#temoin = temoin +2
			#if temoin == 1000:
			#	temoin = 0
			#	temoin2 = temoin2 +1
			#	print(temoin2*1000,"/",largeur_map*hauteur_map," cases traitées")
			if carte[i][k] == '.' or carte[i][k] == 'w':	
				liste_case_couverte = cases_couvertes(carte,coordX,coordY,perim_routeur,largeur_map,hauteur_map)
				if liste_case_couverte!=0:
					score=len(liste_case_couverte)*1000	#On calacul le score
					liste_score1.append([score,coordX,coordY])
	conn.send(liste_score1)
	conn.close()
	
def calcule_score2(carte,boneinf,bonesup,largeur_map,hauteur_map,perim_routeur,conn):
	liste_score2=[] 
	for i in range(boneinf,bonesup):
		coordY=i
		for k in range(largeur_map):
			coordX=k
			if carte[i][k] == '.' or carte[i][k] == 'w':
				liste_case_couverte = cases_couvertes(carte,coordX,coordY,perim_routeur,largeur_map,hauteur_map)
				if liste_case_couverte!=0:
					score=len(liste_case_couverte)*1000	#On calacul le score 
					liste_score2.append([score,coordX,coordY])
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
#on calcule le nombre de case à couvrir
	for i in range(hauteur_map):
		for k in range(largeur_map):
			if map_travail[i][k] == '.':
				case_restante=case_restante+1
	print("Case à couvrir :",case_restante," Budget :",budget)	

#Tant que l'on a du budget ou qu'il reste des case à couvrir on fait le test
	while budget-cout>prix_routeur and case_restante> 0:
		liste_score_routeur=[]

		parent_conn1, child_conn1 = Pipe()
		t1 = Process( target=calcule_score2, args=(map_travail,0,int(hauteur_map/4),largeur_map,hauteur_map,perim_routeur,child_conn1 ) )
		parent_conn2, child_conn2 = Pipe()
		t2 = Process( target=calcule_score2, args=(map_travail,int(hauteur_map/4),int(2*hauteur_map/4),largeur_map,hauteur_map,perim_routeur,child_conn2 ) )
		parent_conn3, child_conn3 = Pipe()
		t3 = Process( target=calcule_score2, args=(map_travail,int(2*hauteur_map/4),int(3*hauteur_map/4),largeur_map,hauteur_map,perim_routeur,child_conn3 ) )
		parent_conn4, child_conn4 = Pipe()
		t4 = Process( target=calcule_score2, args=(map_travail,int(3*hauteur_map/4),hauteur_map,largeur_map,hauteur_map,perim_routeur,child_conn4 ) )
		
		
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		liste_score1 = parent_conn1.recv()
		liste_score2 = parent_conn2.recv()
		liste_score3 = parent_conn3.recv()
		liste_score4 = parent_conn4.recv()

		
		t1.join()
		t2.join()
		t3.join()
		t4.join()
		liste_score_routeur = liste_score1 + liste_score2 +liste_score3 + liste_score4
		print("Trie de la liste")
		liste_score_routeur.sort(reverse=True) #Quand toute les case on été testé, on classe les routeur par leur score
		print("Liste triée")
#		print("score routeur trié :",liste_score_routeur)      #Quand toute les case on été testé, on classe les routeur par leur score
#		print(" ")
		liste_routeur.append([liste_score_routeur[0][2],liste_score_routeur[0][1]])#On garde le meilleur et on le met en place
#		print("coordonné routeur",liste_score_routeur[0][1],liste_score_routeur[0][2])
#		print(" ")
		cout=cout+prix_routeur			#On met à  jour le budget pour vérifier quer l'on peut continuer
		print("cout :",cout," budget :",budget)
		
		#Modification de la matrice pour que les cases déjà  couverte ne puissent plus rapporter de points
		liste_case_couverte = cases_couvertes(map_travail,liste_score_routeur[0][1],liste_score_routeur[0][2],perim_routeur,largeur_map,hauteur_map)		
#		print("case à remplacer :",liste_case_couverte)
#		print(" ")
		for i in range(len(liste_case_couverte)):
			map_travail[liste_case_couverte[i][1]][liste_case_couverte[i][0]]="w"			
		map_travail[liste_score_routeur[0][2]][liste_score_routeur[0][1]] = "R"


		#on enregistre la carte dans un fichier à part
		passage = passage +1
		numpassage = str(passage)
		nommap = "map1-passage " + numpassage
		np.savetxt(nommap, map_travail, delimiter="",fmt="%s")
		case_restante=case_restante-len(liste_case_couverte)
		
		print("routeur",liste_routeur)
		print("case restante à couvrir :",case_restante)
		print(" ")
#		affichage_matrice(map_travail)
	return "finale :",liste_routeur


				
			

if __name__ == '__main__':

#-------------------------------------------------
	""" LECTURE DE LA MAP  : Code lecture_entete.py """
	map="charleston_road.in"               #Choix de la map   ( ex : charleston_road.in )
	entete = lectureEntete(map)
	#print(entete)               #affichage de l'entète, on attrape ici toute les info du fichier .in (en char)
	matrice = creationMatrice(map)    #notre matrice
#-------------------------------------------------

#	affichage_matrice(matrice)
	print(placement_routeurV1(matrice,entete))
	#print(cases_couvertes(matrice,19,5,3,22,8))
	