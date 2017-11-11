# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:37:50 2017

@author: Antoine
"""
import relier2points as re


'''
Prend en paramètre une liste de routeurs et retourne un liste de coordonnées de fibres pour tous les relier de façon optimale
Principe de résolution : 
1- Contruction du graphe complet à n(n-1)/2 arêtes avec n le nombre de routeurs
2- Recherche de l'arbre couvrant minimal grace à l'algorithme de Prim
'''

def relierRouteurs(listeRouteurs): 
    
    listeAretesC = [] #liste d'aretes du graphe complet de la forme (taille,sommet courant, sommet auquel on le relie,coordonnées des points de l'arete)
    
    #===============================
    # GENERATION DU GRAPHE COMPLET
    #===============================
    
    for i in range(len(listeRouteurs)): #on éxecute une boucle n-1 fois avec n le nombre de routeurs
        for j in range(len(listeRouteurs)): #on relie le sommet courant à tous les sommets sauf lui même
            if listeRouteurs[i] != listeRouteurs[j]:
                tuple = (len(re.relier2points(listeRouteurs[i],listeRouteurs[j])),listeRouteurs[i],listeRouteurs[j],re.relier2points(listeRouteurs[i],listeRouteurs[j]))
                listeAretesC.append(tuple) #on ajoute l'arête à la liste
                #print(listeRouteurs[i],'->',listeRouteurs[j]) -> à décommenter pour afficher les relations entres les sommets
    listeAretesC.sort() #On trie les arêtes dans l'ordre croissant (par poids)
    
    #===============================
    #      ALGORITHME DE PRIM
    #===============================
    succ = [] 
    arbreMini = [] #arbre couvrant minimal contenant la liste des points où mettre de la fibre pour relier tous les routeurs
    sommet = listeAretesC[0][1] #On prend arbitrairement comme premier sommet le sommet de départ de la première arrête de la liste des arêtes du graphe complet
    listeSommetsRelies = [] #Liste contenant les sommets déjà reliés

    while len(listeSommetsRelies)+1<len(listeRouteurs): #Tant que tous les routeurs ne sont pas reliés
        #on ajoute à la liste des successeurs toutes les arrêtes ayant 'sommet' comme sommet de départ
        for k in range(len(listeAretesC)):
            if (listeAretesC[k][1] == sommet) and (listeAretesC[k][2] not in listeSommetsRelies) and (listeAretesC[k][1] not in listeSommetsRelies):
                #print('ajout de : ',listeAretesC[k]) ->à décommenter pour afficher les arêtes qu'on ajoute à la liste des successeurs
                succ.append(listeAretesC[k])
        succ.sort() #déjà trié normalement a voir si je l'enlève
        #print('Arrête choisie',succ[0]) -> à décommenter pour afficher l'arêtes qu'on décide d'ajouter à l'arbre couvrant minimal
        arbreMini.append(succ[0]) #On ajoute a l'arbre couvrant minimal l'arrête de poids minimale des successeurs
        listeSommetsRelies.append(succ[0][1]) #On ajoute le sommet courant à la liste des sommets reliés
        sommet = succ[0][2] #Le prochain sommet correspondra au successeur du sommet précédent
        succ = [] #On réinitialise la liste des successeurs
        
    #===============================================
    # CONVERSION DE L'ARBRE EN UNE LISTE DE POINTS
    #===============================================
    
    arbreFinal = []
    
    for l in range(len(arbreMini)):
        for m in range(len(arbreMini[l][3])):
            if arbreMini[l][3][m] not in arbreFinal: #On ne recopie pas les doublons
                arbreFinal.append(arbreMini[l][3][m])
    
    return arbreFinal

    
if __name__=='__main__':
    
    '''map="map0.in"
    matrice = lecture_entete.creationMatrice(map)
    affichage_matrice(matrice)'''
    
    listeR = ((17,3),(4,5),(20,8),(7,6),(11,23))
    arbreMini = relierRouteurs(listeR)
    print('ARBRE MINIMAL : ',arbreMini)

    