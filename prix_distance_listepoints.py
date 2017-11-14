# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:02:33 2017

@author: Romain
"""

def prix(nb_routeurs,nb_backbone,Pr,Pb,B):
    #Pr est le prix d'un routuer
    #Pb est le prix d'un backbone
    #B est le budget
    prix = nb_routeurs * Pr + nb_backbone * Pb
    if prix <= B:
        return prix
    else:
        print("Le prix est de", prix, "€, budget maximal de",B ,"€ atteint !")
    
def distance(pointA,pointB): #où pointA = (xA,yA) et pointB = (xB,yB)
    dist = ((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)**0.5
    return dist
    
def maj_liste_points_explores(liste, point_a_ajouter):
    liste.append(point_a_ajouter)
    return liste
    
if __name__=='__main__':
    pointA = (3,5)
    pointB = (2,4)
    print(distance(pointA,pointB))
    
    nb_routeurs = 10
    nb_backbone = 500
    Pr = 100
    Pb = 1
    B = 1400
    print(prix(nb_routeurs,nb_backbone,Pr,Pb,B))
    
    liste = []
    point_a_ajouter = (8,1)
    print(maj_liste_points_explores(liste, point_a_ajouter))
    
    print(maj_liste_points_explores(liste, (2,5)))