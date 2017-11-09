def placement_routeurV1(plan,data):
	map_travail=plan
	liste_routeur=[]
	budget = data[x]			#Addapter
	hauteur_map = data[y]		#Addapter
	largeur_map = data[z]		#Addapter
	perim_routeur = data[w]		#Addapter
	cout=0
	while budget-coup>=0:  																				#Tant que l'on a du budget on effectue le test
		liste_score_routeur=[]
		for i in range(hauteur_map):  																	#On test chaque case de la matrice
			coordX=i					
			for k in range(largeur_map):
				coordY=k
				if map_travail[i][k]== '.' or map_travail[i][k] == 'w':									#Si il est possible de mettre un routeur sur la case		
					liste_case_couverte = #fonctiondearthur(map_travail,coordX,coordY,perim_routeur) 	#On regarde les case couvertes
					score=len(liste_case_couverte)*1000													#On calacul le score
					liste_score_routeur.append([score,coordX,coordY])
					
					
		liste_score_routeur = sorted(mylist, key=lambda x: x[0]).      									#Quand toute les case on été testé, on classe les routeur par leur score
		liste_routeur.append([liste_score_routeur[0][1],liste_score_routeur[0][2]]). 					#On garde le meilleur et on le met en place
		cout=cout+prix_routeur																			#On met à jour le budget pour vérifier quer l'on peut continuer
		
#Modification de la matrice pour que lesz cases déjà couverte ne puissent plus rapporter de points
		
		liste_case_couverte=#fonctiondearthur(map_travail,liste_score_routeur[0][1],liste_score_routeur[0][2],perim_routeur)
		for i in range(len(liste_case_couverte)):
			map_travail[liste_case_couverte[i][0]][liste_case_couverte[i][1]]]="w"
			
	return (liste_routeur).       																		#Dès que l'on a plus de budget, on renvoie la liste des routeurs
			
		
				