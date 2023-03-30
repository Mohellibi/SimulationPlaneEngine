import json
    
#ça c'est pour lire un fichier.json tu recupere dans historique
with open('historique.json', 'r') as file1:
    historique = json.load(file1)

#ça c'est pour ecrire dans un fichier.json tu renvoie ce que tu veux dedans
with open('historique.json', 'w') as file2:
        json.dump(historique, file2)
