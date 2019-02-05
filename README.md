Pandiculation

***Projet Poly#***
===================
Surfez sur un réseau wifi doté d'une couverture parfaite dans votre bar préféré!

Equipe
-----------------
Antoine MARJAULT<br/>
Arthur MILLET<br/>
Bastien JEAN<br/>
Guillaume POTIER<br/>
Romain ANDRIEUX<br/>

Répartition des tâches
-----------------------
- Bastien JEAN: Lecture entête + création matrice + écriture fichier sortie<br/>
- Guillaume POTIER: Algorithme placement routeurs<br/>
- Arthur MILLET: Calcul cases couvertes + affichage graphique des routeurs<br/>
- Antoine MARJAULT: Algorithme pour relier 2 routeurs<br/>
- Romain ANDRIEUX: Algorithme de l'arbre couvrant minimum<br/>

Stratégies mises en oeuvre
----------------------------
1. Placement des routeurs:<br/>
   Force brute --> on parcours chaque case de la map et on calcule le nombre de cases couvertes par un routeur placé en chaque case, puis on retient la position du routeur qui en couvre le maximum<br/>
2. Connexion des routeurs au backbone:<br/>
   Détermination de l'arbre couvrant minimum en utilisant l'algorithme de Prim<br/>

|Placer routeurs | Temps d'exécution |
|----------------|:-----------------:|
|charleston_road |6mn                |               
|rue_de_londres  |50mn               |               
|opera           |3h                 | 
|lets_go_higher  |14h                | 

|Relier routeurs | Temps d'exécution |
|----------------|:-----------------:|
|charleston_road |1s                 |               
|rue_de_londres  |20s                |               
|opera           |13mn25s            |               
|lets_go_higher  |2h40mn             |               


Organisation du code
---------------------
- Fichier main.py: fichier principal à éxécuter, qui appelle plusieurs sous-fonctions
- Fichier outils.py: comprend toutes les sous-fonctions utiles, lancées à partir du main.py

Nous avons utilisé uniquement des fonctions (pas de classes).<br/>
Modules utilisés: threading<br/>

Lien vers la vidéo : http://filex.univ-nantes.fr/get?k=32NxSDf8Y6SnPzcDKHd