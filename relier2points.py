<<<<<<< HEAD
<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:59:02 2017

@author: Antoine
"""

def relier2points(point1, point2):
    """
    Retourne le chemin le plus court pour relier 2 points dans une matrice donnée
    sous forme d'une liste de couple de coordonnées (x,y)
    On utilise l'algorithme de Bresenham
    """
    x1, x2, y1, y2 = point1[0], point2[0], point1[1], point2[1] #Récupération des coordonnées des 2 points donnés en paramètre
     
    dx = x2 - x1 #On calcule la distance relative entre le point 1 et 2 horizontalement
    dy = y2 - y1 #On calcule la distance relative entre le point 1 et 2 verticalement
    pente = abs(dy) > abs(dx) #Si la pente verticale est supérieure à la pente horizontale pente vaut True sinon elle vaut False
 
    #On tourne la ligne si la pente verticale est supérieur à celle horizontale, la variable pente nous servira pour savoir si la on a tourné la ligne ou non
    if abs(dy) > abs(dx):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    #Si le point 1 est situé après le point 2 (d'un point de vue horizontal) on echange leurs coordonnées
    echange = False
    if x1 > x2:
        x1, x2 = x2, x1 #On inverse x1 et x2
        y1, y2 = y2, y1 #On inverse y1 et y2
        echange = True #On garde en memoire le fait que les points sont inversés, cela servira à la fin pour retourner la liste de points en sens inverse
 
    '''
    NOTE : On s'arrange toujours pour avoir un pente verticale inférieure à la pente horizontale et 
    pour aller de gauche à droite (cela permet de faire tourner un algorithme général et modifier la liste
    finale de points en fonction des conditions initiales plutôt que de faire tourner un algorithme par cas
    qui rendrait le code beaucoup plus long)
    Par cas on entend par exemple "le point 2 est a gauche du point 1", "le point 2 est sur la diagonale droite inférieure" etc... 
    '''
    
    # On recalcule les nouveaux dx et dy dans le cas où la ligne aurait été retournée ou les points inversés
    dx = x2 - x1
    dy = y2 - y1
 
    # On calcul l'erreur qui vaut la valeur entière de la distance horizontale entre les 2 points divisée par 2
    erreur = int(dx / 2.0) 
    if y1 < y2: #Si le point 1 est plus bas que le point 2
        pasY = 1 #on incrémentera la valeur de y qui correspond à l'ordonnée suivante
    else:
        pasY = -1 #On décrémentera la valeur de y qui correspond à l'ordonnée suivante, en clair on prendra le point en dessous de celle actuelle
    #En résumé si le point 1 est au dessus du point 2 on sait qu'il faudra choisir entre le pixel du dessous et celui à côté alors que dans l'autre cas il faudra choisir entre celui du dessus et celui à côté
    
    y = y1 #on initialise y qui correspond à l'ordonnée du premier point par lequel passer
    points = [] #On initialise le tableau des points à emprunter
    # Boucle qui calcule les différents points à emprunter pour aller du point 1 au point 2
    for x in range(x1, x2 + 1): #Pour x allant de l'abscisse du premier point à celle du dernier +1
        if pente: #si la ligne a été tournée
            coord = (y, x) #on retourne le point en inversant x et y
        else:
            coord = (x, y) #sinon on retourne le "vrai" point
        points.append(coord) #On ajoute le point à la liste des points à emprunter
        erreur -= abs(dy) #On soustrait différence de hauteur entre les 2 points à l'erreur 
        if erreur < 0: #Si l'erreur est négative
            y += pasY #On choisit le point juste au dessus ou en dessous en fonction de la valeur de pasY
            erreur += dx #On ajoute à l'erreur la distance entre le point 1 et le point2
 
    if echange: #si on a inversé les points on retourne la liste des points à l'envers
        points.reverse()
    return points
    
    

if __name__=='__main__':
    points = relier2points((1,5),(3,0))
=======
=======
>>>>>>> 55ff5a68429f593d75dd89b37ea088f5a5e45920
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:59:02 2017

@author: Antoine
"""

def relier2points(point1, point2):
    """
    Retourne le chemin le plus court pour relier 2 points dans une matrice donnée
    sous forme d'une liste de couple de coordonnées (x,y)
    On utilise l'algorithme de Bresenham
    """
    x1, x2, y1, y2 = point1[0], point2[0], point1[1], point2[1] #Récupération des coordonnées des 2 points donnés en paramètre
     
    dx = x2 - x1 #On calcule la distance relative entre le point 1 et 2 horizontalement
    dy = y2 - y1 #On calcule la distance relative entre le point 1 et 2 verticalement
    pente = abs(dy) > abs(dx) #Si la pente verticale est supérieure à la pente horizontale pente vaut True sinon elle vaut False
 
    #On tourne la ligne si la pente verticale est supérieur à celle horizontale, la variable pente nous servira pour savoir si la on a tourné la ligne ou non
    if abs(dy) > abs(dx):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    #Si le point 1 est situé après le point 2 (d'un point de vue horizontal) on echange leurs coordonnées
    echange = False
    if x1 > x2:
        x1, x2 = x2, x1 #On inverse x1 et x2
        y1, y2 = y2, y1 #On inverse y1 et y2
        echange = True #On garde en memoire le fait que les points sont inversés, cela servira à la fin pour retourner la liste de points en sens inverse
 
    '''
    NOTE : On s'arrange toujours pour avoir un pente verticale inférieure à la pente horizontale et 
    pour aller de gauche à droite (cela permet de faire tourner un algorithme général et modifier la liste
    finale de points en fonction des conditions initiales plutôt que de faire tourner un algorithme par cas
    qui rendrait le code beaucoup plus long)
    Par cas on entend par exemple "le point 2 est a gauche du point 1", "le point 2 est sur la diagonale droite inférieure" etc... 
    '''
    
    # On recalcule les nouveaux dx et dy dans le cas où la ligne aurait été retournée ou les points inversés
    dx = x2 - x1
    dy = y2 - y1
 
    # On calcul l'erreur qui vaut la valeur entière de la distance horizontale entre les 2 points divisée par 2
    erreur = int(dx / 2.0) 
    if y1 < y2: #Si le point 1 est plus bas que le point 2
        pasY = 1 #on incrémentera la valeur de y qui correspond à l'ordonnée suivante
    else:
        pasY = -1 #On décrémentera la valeur de y qui correspond à l'ordonnée suivante, en clair on prendra le point en dessous de celle actuelle
    #En résumé si le point 1 est au dessus du point 2 on sait qu'il faudra choisir entre le pixel du dessous et celui à côté alors que dans l'autre cas il faudra choisir entre celui du dessus et celui à côté
    
    y = y1 #on initialise y qui correspond à l'ordonnée du premier point par lequel passer
    points = [] #On initialise le tableau des points à emprunter
    # Boucle qui calcule les différents points à emprunter pour aller du point 1 au point 2
    for x in range(x1, x2 + 1): #Pour x allant de l'abscisse du premier point à celle du dernier +1
        if pente: #si la ligne a été tournée
            coord = (y, x) #on retourne le point en inversant x et y
        else:
            coord = (x, y) #sinon on retourne le "vrai" point
        points.append(coord) #On ajoute le point à la liste des points à emprunter
        erreur -= abs(dy) #On soustrait différence de hauteur entre les 2 points à l'erreur 
        if erreur < 0: #Si l'erreur est négative
            y += pasY #On choisit le point juste au dessus ou en dessous en fonction de la valeur de pasY
            erreur += dx #On ajoute à l'erreur la distance entre le point 1 et le point2
 
    if echange: #si on a inversé les points on retourne la liste des points à l'envers
        points.reverse()
    return points
    
    

if __name__=='__main__':
    points = relier2points((1,5),(3,0))
<<<<<<< HEAD
>>>>>>> 55ff5a68429f593d75dd89b37ea088f5a5e45920
=======
>>>>>>> 55ff5a68429f593d75dd89b37ea088f5a5e45920
    print(points)