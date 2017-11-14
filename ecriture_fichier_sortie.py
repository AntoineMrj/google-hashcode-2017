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
