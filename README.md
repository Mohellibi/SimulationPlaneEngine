# SimulationPlaneEngine
Projet Python Avion 

Rapport de Projet


Préquel :

Pour ce projet j'ai choisis de faire le code avec l'aide de trois librairies, j'ai utilisé tkinter pour l'interface, random, et aussi json pour créer une sauvegarde sur un fichier à part. Mon programme est plutôt orienté objet, il est fait en grande partie grâce aux objets et aux méthodes de tkinter. 
Tout ce dont j'ai eu besoin à été sur le site http://tkinter.fdex.eu/ .

Explication graphique :

Réservoir vide :                     réservoir plein :                  pompe en panne :

									pompe à l’arrêt :

									pompe en marche :
Alimentation de chaque moteur : les tuyaux se colores pour montrer
 quel réservoir alimente quel moteur avec  une couleur par réservoirs.

Partie 1 :

Pour le début j'ai commencer à créer les deux fenêtres,  'système de carburant' et 'tableau de bord'. J'ai définis, leur tailles, leur titres, leur positions sur l’écran lors du lancement du script sur Vscode.J'ai ensuite créer les boutons sur le tableau de bord, et j'ai créer les widgets (rond, rectangle, ligne,...) sur le canevas du système de carburant. Chacun avec des variables d'etat (exemple :etat_P12 = 0 ou 1 ou 2) , (0 : en marche , 1 : à l’arrêt ,  2 : en panne)

Ensuite il à fallut que je puisse interagir directement avec des cliques de la souris sur le système de carburant. Grâce à la méthode bind() du canevas j'ai associer les événements clique gauche, clique droit ,et la position du curseur de la souris pour déclencher des pannes, bouger les vannes et activer les pompes de secours (fonctions clique_gauche(event) et clique_droit(event)).  J'ai fait la même chose pour les boutons chaque boutons à une fonction associer qui bouge une des vannes ou active une des pompes de secours. 

A ce niveau je pouvais bouger les vannes, les pompes, vider les réservoirs, et casser les pompes grâce aux cliques de souris ou aux boutons mais rien ne réagissais encore avec rien. J'ai donc créer une fonction tuyaux_carburant(), qui colore les tuyaux pour indiquer quelles réservoirs alimentent quel moteurs et si un moteur n'est pas alimenter son tuyaux est noir. 

Cette fonctions utilise les variables d’états créer plus tôt, et beaucoup de conditions 'if',  je l'es faite de manière à ce qu' aucunes situations incohérentes ne se produisent,
exemple : deux réservoirs qui alimentent un même moteur, ou un réservoir qui alimentent plus de moteurs qu'il n'a de pompes en marche.
Juste après j'ai créer une fonction remplir_reservoirs() du même type qui a pour bute de modifier les variables d’états (exemple :etat_tank1 = 'plein')et l’apparence des réservoirs en fonction des variables d’états des vannes VT12, VT23 et des réservoirs. 
Ces deux fonctions tuyaux_carburant() et remplir_reservoirs() seront appeler à chaque clique sur le canevas de système de carburant ou à chaque boutons pressés sur le tableau de bord. 

A cette étape, l'interface est fonctionnelle chaque fermetures de pompes, pannes, ou ouvertures de vannes changent l'alimentation des moteurs de manière graphique (avec la couleur des tuyaux).

Partie 2 :
 
Pour les exercices j'ai choisis de créer un boutons vert sur le tableau de bord qui appelle une fonction mode_exercice(), quand on clique elle déclenche une ou plusieurs panne(s), avec la contrainte que un exercice doit toujours pouvoir être résolus, j'ai créer des variables aléatoires à l'aide de la librairie random. En fonction de celle qui tombe une ou plusieurs panne de réservoirs ou pompes ou les deux.

Ensuite en fonction des pannes lancer j'ai créer un algorithme qui compte le nombre de coup minimum il faut pour résoudre l'exercice. Par exemple si un réservoir se vide le pilote doit privilégier l'ouverture de VT12 ou VT23, si il alimente le moteur directement avec un autre réservoir il perd des points sur la notes de l'exercice. Le nombre des coups est calculer en rajoutant un à chaque action, puis la note compare le nombre des coup avec le nombre des coups minimum et plus l’écart est grand plus la note baisse.

Quand le pilote passe en mode exercice il ne doit utiliser que le tableau de bord, on lui demande alors un nom d'utilisateur, et un bouton apparaît pour afficher ses notes, si il est nouveau il faut faire au moins un exercice pour afficher ces notes. Si le pilote est reconnue ces notes s'affichent avec la moyenne et un commentaire sur ça performance. 
La dernière fonction BD_Historique(pseudo, liste_de_note) est appeler dans la fonction mode exercice, elle utilise la libraire json pour stocker le pseudo et les notes dans un dictionnaires qui lui même est stocker dans un fichier (en .json) pour le sauvegarder, j'ai appeler ce fichier historique.json .

Les fenêtres lors du lancement du programme : 


EXPLICATION :

sur la fenêtre Système carburant simplifié:

-pour déclencher des pannes il faut utiliser le clique droit de la souris sur une pompe ou un réservoir

-pour activer des pompes de secours ou tourner une vannes il faut utiliser le clique gauche 

-clique gauche sur le boutons notes pour afficher les notes (seulement en mode exercice)

sur la fenêtre Tableau de bord:

-pour activer le mode exercice il faut cliquer sur le boutons vert (clique gauche)

-quand le mode exercice s'active il faut s'identifier pour continuer (entrer son nom dans le terminale)

- les boutons active les vannes et les pompes avec le clique gauche
