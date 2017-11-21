# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Purpose: Affichage de la matrice
# Author:      Arthur
# MAJ:     21/11/2017
#-------------------------------------------------------------------------------

from tkinter import *

def creationMatrice(file_link):
	matrice = []    #matrice pincipale
	ligneMatrice = []   #ligne d'une matrice

	fichier_map = open(file_link, "r")  #on ouvre le fichier à  lire

	for i in range(0, 1):       #pour virer n ligne au dessus de la map
		variable_inutile = fichier_map.readline()
		variable_inutile = []

	while 1:    #on parcours l'ensemble des caractères de la map
		char = fichier_map.read(1)  #on récupère le caractère suivant
		if char == '\n':    #si c'est une fin de ligne
			matrice.append(ligneMatrice)    #on ajoute la ligne de matrice créée Ã  la matrice principale
			ligneMatrice = []   #on reset la ligne de matrice pour passer  la suivante
			pass
		elif not char:  #si aucun caractère n'est récupéré, fin de fichier, on sort de la boucle
			break
		else:
			ligneMatrice.append(char)   #on ajoute le caractère récupéré à  la fin de la ligne de matrice en cours de création

	fichier_map.close() #on ferme le fichier ouvert

	return matrice  #on renvoie la matrice créée

def affichage_matrice(mat):     #entrée : la matrice

		for i in range (0, len(mat)):       #on parcours la totalité des lignes de la matrice
			for j in range(0, len(mat[i])):     #on parcours la totalité du noimbre de colonnes de la matrice
				print(mat[i][j], end="")        #on affiche l'élément sans retour à  la ligne
			print()

def Clic(event):

    global a
    print("passage : ",nbclic())

    num_map = a
    map="map1-passage {0}".format(num_map)
    #map="all_maps"

    matrice = creationMatrice(map)

    for j in range (0, len(matrice)):       #on parcours la totalité des lignes de la matrice
        for i in range(0, len(matrice[j])):     #on parcours la totalité du noimbre de colonnes de la matrice
            r = 1
            # on dessine un cercle dans la zone graphique
            if matrice[j][i]=='.':
                item = Canevas.create_oval(i-r, j-r, i+r, j+r, outline='blue')
            elif matrice[j][i]=='w':
                item = Canevas.create_oval(i-r, j-r, i+r, j+r, outline='black')
            elif matrice[j][i]=='R':
                item = Canevas.create_oval(i-r, j-r, i+r, j+r, outline='pink')
            elif matrice[j][i]=='#':
                item = Canevas.create_oval(i-r, j-r, i+r, j+r, outline='white')
            else:
                item = Canevas.create_oval(i-r, j-r, i+r, j+r, outline='red')  #cases extérieur

def nbclic():
    global a
    a=a+1
    return a

a=0 #num map

if __name__ == '__main__':

    # Création de la fenêtre principale (main window)
    Mafenetre = Tk()
    Mafenetre.title('Affichage graphique Polyhash')
    Mafenetre.geometry('800x700')
    Mafenetre['bg']='grey'

    # Image de fond
    photo = PhotoImage(file="vert.gif")

    # texte d'entrée
    Label1 = Label(Mafenetre, text = 'Polyhash team !', fg = 'red')

    # Positionnement du widget avec la méthode pack()
    Label1.pack()

    # Création du Canvas
    Largeur = 550
    Hauteur = 550
    Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    Canevas.pack()

    # La méthode bind() permet de lier un événement avec une fonction :
    # un clic gauche dans la fenetre provoquera l'appel de la fonction utilisateur Clic()
    Canevas.bind('<Button-1>', Clic)
    Canevas.pack(padx =5, pady =5)

    Mafenetre.mainloop()