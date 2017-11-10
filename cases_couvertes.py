def cases_couvertes(matrice, coordX_routeur, coordY_routeur, radius, largeur_matrice, hauteur_matrice):
	#matrice de travail
    map_travail = matrice

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
    if (map_travail[y][x] == '.'):

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
                        if (map_travail[y_coord][x_coord] == '.'):
                            #on compare la position de la colonne de la case étudié et la colonne du routeur
                            if (y_coord < y):
                                y_origin_case_test = y_coord
                                y_fin_case_test = y
                            elif (y_coord > y):
                                y_origin_case_test = y
                                y_fin_case_test = y_coord
                            else:
                                y_origin_case_test = y
                            #on compare la position de la ligne de la case étudié et la ligne du routeur
                            if (x_coord < x):
                                x_origin_case_test = x_coord
                                x_fin_case_test = x
                            elif (x_coord > x):
                                x_origin_case_test = x
                                x_fin_case_test = x_coord
                            else:
                                x_origin_case_test = x
                                
                            #on parcours l'ensemble du carré entre la case étudiée et le routeur pour vérifier la présence d'un mur ou non
                            #on parcours chaque colonne
                            for y_coord_case_test in range(y_origin_case_test, y_fin_case_test+1):
                                #on parcours chaque ligne
                                for x_coord_case_test in range(x_origin_case_test, x_fin_case_test+1):
                                    #si présence d'une cellule mur '#'
                                    if (map_travail[y_coord_case_test][x_coord_case_test] == '#'):
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
                            if (presence_mur == False):
                            	#ajout de la case étudiée à la liste des cases couvertes
                            	liste_cases_couvertes.append([x_coord, y_coord])

    else:
        #si cellule incorrect (vie ou mur) on envoie 0 pour stoper la fonction
        return 0

    #fin
    return liste_cases_couvertes
