def placement_routeurV1(plan,data):
	map_travail=plan
	liste_routeur=[]
	budget = data[x]			#Addapter
	hauteur_map = data[y]		#Addapter
	largeur_map = data[z]		#Addapter
	cout=0
	while budget-coup>=0:  #tant que l'on a du budget on test
		liste_score_routeur=[]
		for i in range(hauteur_map):
			coordX=i
			for k in range(largeur_map):
				if map_travail[i][k]== '.' or map_travail[i][k] == 'w':					
					coordY=K
					liste_case_couverte = #fonctiondearthur(map_travail,coordX,coordY)
					score=len(liste_case_couverte)*1000
					liste_score_routeur.append([score,coordX,coordY])
		liste_score_routeur = sorted(mylist, key=lambda x: x[0])
		liste_routeur.append([liste_score_routeur[0][1],liste_score_routeur[0][2]])
		cout=cout+prix_routeur
		#fonction de modification de map
	return (liste_routeur)
			
		
				
				
				
	