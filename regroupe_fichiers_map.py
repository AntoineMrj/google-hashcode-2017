#entrée : numéro de la map, nombre de fichier
def regroupe(num_map, nb_files):

	n_map = num_map
	nb_f = nb_files

	for num_file in range(1, nb_f + 1):
		filename = "map{}-passage {}".format(n_map, num_file)

		#print (filename)
		fichier = open(filename, "r") #ouvre le fichier en mode lecture
		content = fichier.read() #on lit le contenu du fichier

		with open("all_maps", "a") as fichier_sortie: #ouvre le fichier de sortie (le crée si non existant)
			fichier_sortie.write(content) #on ecris le contenu lu précédemment
			fichier_sortie.write("\n") #on saute une ligne
			fichier_sortie.close() #on ferme le fichier

		fichier.close() #on ferme le fichier

if __name__ == '__main__':
	regroupe(1, 84) #map 1 avec 84 fichiers