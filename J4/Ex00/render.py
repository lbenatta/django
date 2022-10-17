
# open the file using open() function
file = open("myCV.template")

# Reading from file
print(file.read())

from string import Template
temp_str = 'Hi $name, welcome to $site'
temp_obj = Template(temp_str)
temp_obj.substitute(name='John Doe', site='StackAbuse.com')
#'Hi John Doe, welcome to StackAbuse.com'



with open('myCV.template') as f:
    dtypes = ['float', 'object']
    #skip_header=1
    tableau=[]
    lire=csv.reader(f)                            #chargement des lignes du fichier csv
    f_to_array = np.array(f)
	#while readings != 0 or readings != '':    ne fonctionne pas
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')
    for ligne in lire:                            #Pour chaque ligne...
        print(ligne, end='\n')                    #...affichage de la ligne dans la console ...
        tableau.append(ligne)                     #...on ajoute la ligne dans la liste ...
                                                  #...de liste nommée tableau
#Création d'un fichier à partir de la liste tableau
with open('dataset_train.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
    ecrire=csv.writer(f)                        # préparation à l'écriture
    for i in tableau:                           # Pour chaque ligne du tableau...
        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne
print('',end='\n')
# # print('longueur du tableau : ',len(tableau))


# $> cat settings.py
# name = "duoquadragintian"
# $> cat file.template
# <p>"-Who are you?
# -A {name}!"</p>
# $> python3 render.py file.template
# $> cat file.html
# <p>"-Who are you?
# -A duoquadragintian!"</p>
