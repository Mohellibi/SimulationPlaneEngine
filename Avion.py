import random
import tkinter as tk
import json
###EXPLICATION 
##sur la fenetre Système carburant simplifié:
#-pour declencher des pannes il faut utiliser le clique droit de la souris sur une pompe ou un reservoir
#-pour activer des pompes de secours ou tourner une vannes il faut utiliser le clique gauche 
#-clique gauche sur le boutons notes pour afficher les notes (seulement en mode exercice)

##sur la fenetre Tableau de bord:
#-pour activer le mode exercice il faut cliquer sur le boutons vert (clique gauche)
#-quand le mode exercice s'active il faut s'identifier pour continuer (entrer son nom dans le terminale)
#- les boutons active les vannes et les pompes avec le clique gauche

###FIN D'EXPLICATION 

###Partie de la fenetre 'Système carburant simplifié'
systeme_carburant = tk.Tk()
systeme_carburant.title("Système carburant simplifié")
# resizable(width=False, height=False) enleve l'autorisation de modifier la taille de la fenetre.
systeme_carburant.resizable(width=False, height=False)

systeme_carburant.geometry("600x500+200+50")

# creation du canvas et initialisation de nombre de coup pour la fonction mode_exercice
Fond = tk.Canvas(systeme_carburant, width=600, height=500, bg= 'beige' )
Fond.pack()
nombre_de_coup = 0

#creation des reservoirs reservoirs et initialisation de leur variables d'etat plein/vide
Tank1 = Fond.create_rectangle(50 ,50, 180, 200, fill = "orange", outline= 'white')
Fond.create_text(100, 100, fill = "black", text = "Tank 1", font= ('bold', 20))
etat_tank1 = 'plein'

Tank2 =Fond.create_rectangle(250 ,50, 350, 200, fill = "green", outline= 'white')
Fond.create_text(300, 100, fill = "black", text = "Tank 2", font= ('bold', 20))
etat_tank2 = 'plein'

Tank3 =Fond.create_rectangle(450 ,50, 580, 200, fill = "yellow", outline= 'white')
Fond.create_text(500, 100, fill = "black", text = "Tank 3", font= ('bold', 20) )
etat_tank3 = 'plein'



#creation des moteurs et initialisation de leur variable d'etat 0 en marche, et 1 a l'arret
Fond.create_rectangle(80 , 350, 130, 450, fill = "gray", outline= 'white')
Fond.create_text(105, 400, fill = "black", text = "M 1", font= ('bold', 15))
etat_M1 = 0
Fond.create_rectangle(280 ,350, 330, 450, fill = "gray", outline= 'white')
Fond.create_text(305, 400, fill = "black", text = "M 2", font= ('bold', 15))
etat_M2 = 0
Fond.create_rectangle(500 ,350, 550, 450, fill = "gray", outline= 'white')
Fond.create_text(525, 400, fill = "black", text = "M 3", font= ('bold', 15))
etat_M3 = 0

#creation des pompes et initialisation de leur variable d'etat 0 en marche, et 1 a l'arret
Fond.create_rectangle(60 , 150, 180, 200, fill = "orange")
pompe_11 = Fond.create_oval( 80, 160 , 110, 190 ,fill = "black", outline = '#000fff000', width = 2)
Fond.create_text(95, 175, fill = "white", text = "P 11")
etatP11 = 0
pompe_12 = Fond.create_oval( 120, 160 , 150, 190 ,fill = "black", outline = 'gray', width = 2)
Fond.create_text(135, 175, fill = "white", text = "P 12")
etatP12 = 1
Fond.create_rectangle(260 , 150, 340, 200, fill = "green")
pompe_21 = Fond.create_oval( 270, 160 , 300, 190 ,fill = "black", outline = '#000fff000', width = 2)
Fond.create_text(285, 175, fill = "white", text = "P 21")
etatP21 = 0
pompe_22 = Fond.create_oval( 310, 160 , 340, 190 ,fill = "black", outline = 'gray', width = 2)
Fond.create_text(325, 175, fill = "white", text = "P 22")
etatP22 = 1
Fond.create_rectangle(450 , 150, 570, 200, fill = "yellow")
pompe_31 = Fond.create_oval( 480, 160 , 510, 190 ,fill = "black", outline = '#000fff000', width = 2)
Fond.create_text(495, 175, fill = "white", text = "P 31")
etatP31 = 0
pompe_32 = Fond.create_oval( 520, 160 , 550, 190 ,fill = "black", outline = 'gray', width = 2)
Fond.create_text(535, 175, fill = "white", text = "P 32")
etatP32 = 1

#tuyau entre le moteur M1 et le reservoir Tank1
tuyau1_MT1 = Fond.create_line(125, 300, 125, 200 , fill = "orange", width= 2)
tuyau2_MT1 = Fond.create_line(105, 300, 105, 350 , fill = "orange", width= 2)
tuyau3_MT1 = Fond.create_line(105, 300, 125, 300 , fill = "orange", width= 2)

#tuyau entre le moteur M1 et le reservoir Tank3
tuyau1_MT2 =Fond.create_line(295, 300, 295, 200 , fill = "green", width= 2)
tuyau2_MT2 =Fond.create_line(295, 300, 305, 300 , fill = "green", width= 2)
tuyau3_MT2 =Fond.create_line(305, 300, 305, 350 , fill = "green", width= 2)

#tuyau entre le moteur M3 et le reservoir Tank3
tuyau1_MT3 =Fond.create_line(515, 300, 515, 200 , fill = "yellow", width= 2)
tuyau2_MT3 =Fond.create_line(515, 300, 525, 300 , fill = "yellow", width= 2)
tuyau3_MT3 =Fond.create_line(525, 350, 525, 300 , fill = "yellow", width= 2)

#tuyaux entre les tuyaux precedent

tuyau_inter1 =Fond.create_line(125, 250, 515, 250 , fill = "black", width= 2)
tuyau_inter12 =Fond.create_line(525, 250, 515, 250 , fill = "black", width= 2)
tuyau_inter122 =Fond.create_line(125, 250, 105, 250 , fill = "black", width= 2)
tuyau_inter123 =Fond.create_line(105, 250, 105, 300 , fill = "black", width= 2)
tuyau_inter2 =Fond.create_line(525, 250, 525, 300 , fill = "black", width= 2)
tuyau_inter3 =Fond.create_line(125, 300, 295, 300 , fill = "black", width= 2)
tuyau_inter4 =Fond.create_line(515, 320, 315, 320 , fill = "black", width= 2)
tuyau_inter42 = Fond.create_line(515, 320, 515, 300 , fill = "black", width= 2)
tuyau_inter422 =Fond.create_line(315, 300, 305, 300 , fill = "black", width= 2)
tuyau_inter423 =Fond.create_line(315, 300, 315, 320 , fill = "black", width= 2)

##tuyau entre les reservoirs

#ligne entre Tank1 et Tank2
tuyaux1 = Fond.create_line(180, 125, 250, 125 , fill = "black", width= 2 ) 
etat_tuyaux1 = 0
#ligne entre Tank2 et Tank3
tuyaux2 = Fond.create_line(350, 125, 450, 125 , fill = "black", width= 2)
etat_tuyaux2 = 0

#variable pour les notes dans la fonction mode_exercice()
nombre_de_coup= 0
point_negatif = 0
liste_de_note = []

# fonction qui grace a des coordonnées creer des vannes fermer ou ouverte
def vannes_ouverte(x1,y1):
    Fond.create_oval(x1, y1, x1 + 35, y1 + 35, fill = "black")
    Fond.create_rectangle(x1+15, y1, x1+20, y1 + 35, fill = "white")
    return x1,y1
def vannes_fermer(x1,y1):
    Fond.create_oval(x1, y1, x1 + 35, y1 + 35, fill = "black")
    Fond.create_rectangle(x1, y1+15, x1+35, y1+20, fill = "white")
    return x1,y1

# fonction qui grace a des coordonnées creer des croix rouge sur les pompes
def panne(x1,y1):
    lignea = Fond.create_line(x1, y1, x1 + 30, y1 + 30, fill = "red", width= 3)
    ligneb = Fond.create_line(  x1, y1 + 30, x1 + 30, y1, fill = "red", width= 3)
    croix = [lignea, ligneb]
    return croix

#initialisation des variables d'etat des vannes et creation au bonne coordonner sur le canvas 
vannes_ouverte(200,107.5)
Fond.create_text(217.5, 100, fill = "black", text = "VT12", font= ('bold', 11))
etat_VT12 = 0
vannes_ouverte(385,107.5)
Fond.create_text(402.5, 100, fill = "black", text = "VT23", font= ('bold', 11))
etat_VT23 = 0
vannes_ouverte(370,232.5)
Fond.create_text(387.5, 225, fill = "black", text = "V13", font= ('bold', 11))
etat_V13 = 0
vannes_ouverte(200,282.5)
Fond.create_text(217.5, 275, fill = "black", text = "V12", font= ('bold', 11))
etat_V12 = 0
vannes_ouverte(385,302.5)
Fond.create_text(402.5, 295, fill = "black", text = "V23", font= ('bold', 11))
etat_V23 = 0

## fonction pour tout ce qui concerne le clique gauche de la sourie sur la canvas
def clique_gauche(event):
    global X, Y, etat_VT12, etat_VT23, etat_V13, etat_V12, etat_V23,  etatP11, etatP12, etatP21, etatP22, etatP31, etatP32,tuyaux1, tuyaux2, etat_tank1, etat_tank2, etat_tank3, ftres1, ftres2, ftres3 
    # renvoie la position de la souris lors du clique gauche
    X = event.x
    Y = event.y
    # gere l'action vanne ouverte/fermer
    if 200 < X < 235 and 107.5 < Y < 142.5:
        if etat_VT12 == 0:
            vannes_fermer(200,107.5)
            etat_VT12 = 1
        elif etat_VT12 == 1:
            vannes_ouverte(200,107.5)
            etat_VT12 = 0
    if 385 < X < 420 and 107.5 < Y < 142.5:
        if etat_VT23 == 0:
            vannes_fermer(385,107.5)
            etat_VT23 = 1
        elif etat_VT23 == 1:
            vannes_ouverte(385,107.5)
            etat_VT23 = 0        
    if 370 < X < 405 and 232.5 < Y < 267.5:
        if etat_V13 == 0:
            vannes_fermer(370,232.5)
            etat_V13 = 1
        elif etat_V13 == 1:
            vannes_ouverte(370,232.5)
            etat_V13 = 0        
    if 200 < X < 235 and 282.5 < Y < 317.5:
        if etat_V12 == 0:
            vannes_fermer(200,282.5)
            etat_V12 = 1
        elif etat_V12 == 1:
            vannes_ouverte(200,282.5)
            etat_V12 = 0        
    if 385 < X < 420 and 302.5 < Y < 337.5:
        if etat_V23 == 0:
            vannes_fermer(385,302.5)
            etat_V23 = 1
        elif etat_V23 == 1:
            vannes_ouverte(385,302.5)
            etat_V23 = 0   
# gere l'action des pompes active ou inactive
    if 120 < X < 150 and 160 < Y < 190:
        if etatP12 == 0:
            Fond.itemconfigure(pompe_12, outline = 'gray')
            etatP12 = 1
        elif etatP12 == 1:
            Fond.itemconfigure(pompe_12, outline = '#000fff000')
            etatP12 = 0
    elif 310 < X < 340 and 160 < Y < 190:
        if etatP22 == 0:
            Fond.itemconfigure(pompe_22, outline = 'gray')
            etatP22 = 1
        elif etatP22 == 1:
            Fond.itemconfigure(pompe_22, outline = '#000fff000')
            etatP22 = 0
    elif 520 < X < 550 and 160 < Y < 190:
        if etatP32 == 0:
            Fond.itemconfigure(pompe_32, outline = 'gray')
            etatP32 = 1
        elif etatP32 == 1:
            Fond.itemconfigure(pompe_32, outline = '#000fff000')
            etatP32 = 0
    # appelle de fontions pour mettre a jour les tuyaux et les reservoirs (les fonctions sont creer plus bas)
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()

## fonction pour tout ce qui concerne le clique droit de la sourie sur la canvas
def clique_droit(event):
    global X, Y, etatP11, etatP12, etatP21, etatP22, etatP31, etatP32, croix11, croix12, croix21, croix22, croix31, croix32, etat_tank1, etat_tank2, etat_tank3, Tank1, Tank2, Tank3, ftres1, ftres2, ftres3
    # renvoie la position de la souris lors du clique gauche
    X = event.x
    Y = event.y
    # rajoute ou supprime les croix rouge et change la variable d'etat en 2 (en panne)
    if  80 < X < 110 and 160 < Y < 190:
        if etatP11 == 2:
            Fond.delete(croix11[0])
            Fond.delete(croix11[1])
            etatP11 = 0
        else:
            croix11 = panne(80, 160)
            etatP11 = 2
    elif 120 < X < 150 and 160 < Y < 190:
        if etatP12 == 2:
            Fond.delete(croix12[0])
            Fond.delete(croix12[1])
            etatP12 = 1
            Fond.itemconfigure(pompe_12, outline = 'gray')
        else:
            croix12 = panne(120, 160)
            etatP12 = 2
    elif 270 < X < 300 and 160 < Y < 190:
        if etatP21 == 2:
            Fond.delete(croix21[0])
            Fond.delete(croix21[1])
            etatP21 = 0
        else:
            croix21 = panne(270, 160)
            etatP21 = 2
    elif 310 < X < 340 and 160 < Y < 190:
        if etatP22 == 2:
            Fond.delete(croix22[0])
            Fond.delete(croix22[1])
            etatP22 = 1
            Fond.itemconfigure(pompe_22, outline = 'gray')
        else:
            croix22 = panne(310, 160)
            etatP22 = 2
    elif 480 < X < 510 and 160 < Y < 190:
        if etatP31 == 2:
            Fond.delete(croix31[0])
            Fond.delete(croix31[1])
            etatP31 = 0
        else:
            croix31 = panne(480, 160)
            etatP31 = 2
    elif 520 < X < 550 and 160 < Y < 190:
        if etatP32 == 2:
            Fond.delete(croix32[0])
            Fond.delete(croix32[1])
            etatP32 = 1
            Fond.itemconfigure(pompe_32, outline = 'gray')
        else:
            croix32 = panne(520, 160)
            etatP32 = 2
    # change la couleur des reservoir qui se vide et change la variable d'etat de plein à vide ,ou de vide à plein
    elif  50 < X < 180 and 50 < Y < 200:
        if etat_tank1 == 'plein':
            Fond.itemconfigure(Tank1, fill = 'gray', outline = "orange", width = 5)
            etat_tank1 = 'vide'
        elif etat_tank1 == 'vide':
            Fond.itemconfigure(Tank1, fill = "orange", outline = 'white')
            etat_tank1 = 'plein'
    elif  250 < X < 350 and 50 < Y < 200:
        if etat_tank2 == 'plein':
            Fond.itemconfigure(Tank2, fill = 'gray', outline = "green", width = 5)
            etat_tank2 = 'vide'
        elif etat_tank2 == 'vide':
            Fond.itemconfigure(Tank2, fill = "green", outline = 'white')
            etat_tank2 = 'plein'
    elif  450 < X < 580 and 50 < Y < 200:
        if etat_tank3 == 'plein':
            Fond.itemconfigure(Tank3, fill = 'gray', outline = "yellow", width = 5)
            etat_tank3 = 'vide'
        elif etat_tank3 == 'vide':
            Fond.itemconfigure(Tank3, fill = "yellow", outline = 'white')
            etat_tank3 = 'plein'
    # appelle de fontions pour mettre a jour les tuyaux et les reservoirs (les fonctions sont creer plus bas)
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()

# creation des evenements clique gauche/ droit sur la canvas pour les fonction(event)

Fond.bind("<Button-1>", clique_gauche)
Fond.bind("<Button-3>", clique_droit)

#le cuseur de la souris devient une main sur le canvas
Fond.configure(cursor ='hand2')

# mise a jour des tuyaux en fonction de toute les variables d'etat, cette contion est appeler a la fin des fonction event (clique gauche/droit) et des fonctions des boutons
def tuyaux_carburant():
    global fils_tank1, fils_tank2, fils_tank3, etat_M1, etat_M2, etat_M3
    #gestion des tuyaux entre les reservoirs et leur moteur rajout d'une variable (liste) qui liste les moteurs que chaque reservoir alimente (fils)
    if etat_tank1 == 'plein' and  (etatP11 == 0 or etatP12 ==0):
        Fond.itemconfigure(tuyau1_MT1, fill = "orange")
        Fond.itemconfigure(tuyau2_MT1, fill = "orange")
        Fond.itemconfigure(tuyau3_MT1, fill = "orange")
        etat_M1 = 0
        fils_tank1 = ['M1']
    else:
        Fond.itemconfigure(tuyau1_MT1, fill = "black")
        Fond.itemconfigure(tuyau2_MT1, fill = "black")
        Fond.itemconfigure(tuyau3_MT1, fill = "black")
        etat_M1 = 1
        fils_tank1 = []
    if etat_tank2 == 'plein' and  (etatP21 == 0 or etatP22 == 0):
        Fond.itemconfigure(tuyau1_MT2, fill = "green")
        Fond.itemconfigure(tuyau2_MT2, fill = "green")
        Fond.itemconfigure(tuyau3_MT2, fill = "green")
        etat_M2 = 0
        fils_tank2 = ['M2']
    else:
        Fond.itemconfigure(tuyau1_MT2, fill = "black")
        Fond.itemconfigure(tuyau2_MT2, fill = "black")
        Fond.itemconfigure(tuyau3_MT2, fill = "black")  
        etat_M2 = 1       
        fils_tank2 = []
    if etat_tank3 == 'plein' and  (etatP31 == 0 or etatP32 == 0):
        Fond.itemconfigure(tuyau1_MT3, fill = "yellow")
        Fond.itemconfigure(tuyau2_MT3, fill = "yellow")
        Fond.itemconfigure(tuyau3_MT3, fill = "yellow")
        etat_M3 = 0 
        fils_tank3 = ['M3']
    else:
        Fond.itemconfigure(tuyau1_MT3, fill = "black")
        Fond.itemconfigure(tuyau2_MT3, fill = "black")
        Fond.itemconfigure(tuyau3_MT3, fill = "black")
        etat_M3 = 1  
        fils_tank3 = []
    # verification de l'existance des ftres utiliser pour recuper les resultats du derniere appel de la fonction tuyaux
    try:
        if len(ftres1) == 2:
            repere1 = ftres1
    except:
        repere1 = fils_tank1
    try:
        if len(ftres2) == 2:
            repere2 = ftres2
    except:
        repere2 = fils_tank2
    try:
        if len(ftres3) == 2:
            repere3 = ftres3
    except:
        repere3 = fils_tank3
    try:
        repere1
    except:
        repere1 = fils_tank1 
    try:
        repere2
    except:
        repere2 = fils_tank2
    try:
        repere3
    except:
        repere3 = fils_tank3
    #mise a jours des tuyaux entre les reservoirs et les autres moteurs
    if repere1 != ['M1', 'M3'] and etat_tank1 == 'plein' and (etat_tank2 == 'vide' or (etatP21 != 0 and etatP22 != 0))and  etatP11 == 0 and etatP12 == 0 and etat_V12 == 1 and etat_M2 == 1:
            Fond.itemconfigure(tuyau_inter3, fill = "orange")
            Fond.itemconfigure(tuyau2_MT2, fill = "orange")
            Fond.itemconfigure(tuyau3_MT2, fill = "orange")
            etat_M2 = 0
            if 'M2' not in fils_tank1 and 'M3' not in fils_tank1 :
                fils_tank1.append('M2') 
    elif repere2 != ['M2', 'M3'] and etat_tank2 == 'plein' and (etat_tank1 == 'vide' or (etatP11 != 0 and etatP12 != 0)) and  etatP21 == 0 and etatP22 == 0 and etat_V12 == 1 and etat_M1 == 1:
            Fond.itemconfigure(tuyau_inter3, fill = "green")
            Fond.itemconfigure(tuyau2_MT1, fill = "green")
            Fond.itemconfigure(tuyau3_MT1, fill = "green")
            etat_M1 = 0
            if 'M1' not in fils_tank2 and 'M3' not in fils_tank2 :
                fils_tank2.append('M1') 
    else:
            Fond.itemconfigure(tuyau_inter3, fill = "black")

    if repere1 != ['M1', 'M2'] and etat_tank1 == 'plein' and (etat_tank3 == 'vide' or (etatP31 != 0 and etatP32 != 0))and  etatP11 == 0 and etatP12 == 0 and etat_V13 == 1 and etat_M3 == 1:
            Fond.itemconfigure(tuyau_inter1, fill = "orange")
            Fond.itemconfigure(tuyau_inter12, fill = "orange")
            Fond.itemconfigure(tuyau_inter2, fill = "orange")
            Fond.itemconfigure(tuyau3_MT3, fill = "orange")
            etat_M3 = 0
            if 'M3' not in fils_tank1 and 'M2' not in fils_tank1 :
                fils_tank1.append('M3') 
    elif repere3 != ['M3', 'M2'] and etat_tank3 == 'plein' and (etat_tank1 == 'vide' or (etatP11 != 0 and etatP12 != 0)) and  etatP31 == 0 and etatP32 == 0 and etat_V13 == 1 and etat_M1 == 1:
            Fond.itemconfigure(tuyau_inter1, fill = "yellow")
            Fond.itemconfigure(tuyau_inter122, fill = "yellow")
            Fond.itemconfigure(tuyau_inter123, fill = "yellow")
            Fond.itemconfigure(tuyau2_MT1, fill = "yellow")
            etat_M1 = 0
            if 'M1' not in fils_tank3 and 'M2' not in fils_tank3 :
                fils_tank3.append('M1') 
    else:
            Fond.itemconfigure(tuyau_inter1, fill = "black")
            Fond.itemconfigure(tuyau_inter12, fill = "black")
            Fond.itemconfigure(tuyau_inter2, fill = "black")
            Fond.itemconfigure(tuyau_inter122, fill = "black")
            Fond.itemconfigure(tuyau_inter123, fill = "black")
    
    if repere2 != ['M2', 'M1'] and  etat_tank2 == 'plein'  and (etat_tank3 == 'vide' or (etatP31 != 0 and etatP32 != 0))and  etatP21 == 0 and etatP22 == 0 and etat_V23 == 1 and etat_M3 == 1:
            Fond.itemconfigure(tuyau_inter4, fill = "green")
            Fond.itemconfigure(tuyau_inter42, fill = "green")
            Fond.itemconfigure(tuyau_inter422, fill = "green")
            Fond.itemconfigure(tuyau_inter423, fill = "green")
            Fond.itemconfigure(tuyau2_MT3, fill = "green")
            Fond.itemconfigure(tuyau3_MT3, fill = "green")
            etat_M3 = 0
            if 'M3' not in fils_tank2 and 'M1' not in fils_tank2 :
                fils_tank2.append('M3') 
    elif repere3 != ['M3', 'M1'] and  etat_tank3 == 'plein' and (etat_tank2 == 'vide' or (etatP21 != 0 and etatP22 != 0)) and  etatP31 == 0 and etatP32 == 0 and etat_V23 == 1 and etat_M2 == 1:
            Fond.itemconfigure(tuyau_inter4, fill = "yellow")
            Fond.itemconfigure(tuyau_inter42, fill = "yellow")
            Fond.itemconfigure(tuyau_inter422, fill = "yellow")
            Fond.itemconfigure(tuyau_inter423, fill = "yellow")
            Fond.itemconfigure(tuyau3_MT2, fill = "yellow")
            etat_M2 = 0
            if 'M2' not in fils_tank3 and 'M1' not in fils_tank3:
                fils_tank3.append('M2')
    else:
            Fond.itemconfigure(tuyau_inter4, fill = "black")
            Fond.itemconfigure(tuyau_inter42, fill = "black")
            Fond.itemconfigure(tuyau_inter422, fill = "black")
            Fond.itemconfigure(tuyau_inter423, fill = "black")
    return fils_tank1, fils_tank2, fils_tank3
    
def remplir_reservoirs():
    global etat_tank1, etat_tank2, etat_tank3, ftres1, ftres2, ftres3
    # si la vanne est ouverte et un reservoir plein et l'autre vide le reservoir se remplis 
    if etat_VT12 == 1 and etat_tank2 == 'plein' and etat_tank1 == 'vide':
        Fond.itemconfigure(Tank1, fill = "orange", outline = 'white')
        etat_tank1 = 'plein'
    if etat_VT23 == 1 and etat_tank2 == 'plein' and etat_tank3 == 'vide':
        Fond.itemconfigure(Tank3, fill = "yellow", outline = 'white')
        etat_tank3 = 'plein'
    if etat_VT12 == 1 and etat_tank1 == 'plein' and etat_tank2 == 'vide':
        Fond.itemconfigure(Tank2, fill = "green", outline = 'white')
        etat_tank2 = 'plein'
        if etat_VT23 == 1 and etat_tank2 == 'plein' and etat_tank3 == 'vide':
            Fond.itemconfigure(Tank3, fill = "yellow", outline = 'white')
            etat_tank3 = 'plein'
    if etat_VT23 == 1 and etat_tank3 == 'plein' and etat_tank2 == 'vide':
        Fond.itemconfigure(Tank2, fill = "green", outline = 'white')
        etat_tank2 = 'plein'
        if etat_VT12 == 1 and etat_tank2 == 'plein' and etat_tank1 == 'vide':
            Fond.itemconfigure(Tank1, fill = "orange", outline = 'white')
            etat_tank1 = 'plein'

        
# ouverture fermeture des vannes sur le tableau de bord avec les bouttons
def vanne_VT12_bouton():
    global etat_VT12,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etat_VT12 == 0:
        vannes_fermer(200,107.5)
        etat_VT12 = 1
    elif etat_VT12 == 1:
        vannes_ouverte(200,107.5)
        etat_VT12 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    try:
        Fond.delete(finir)
    except:
        None
def vanne_VT23_bouton():
    global etat_VT23,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etat_VT23 == 0:
        vannes_fermer(385,107.5)
        etat_VT23 = 1
    elif etat_VT23 == 1:
        vannes_ouverte(385,107.5)
        etat_VT23 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()   
    try:
        Fond.delete(finir)
    except:
        None
def vanne_V13_bouton():
    global etat_V13,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etat_V13 == 0:
        vannes_fermer(370,232.5)
        etat_V13 = 1
    elif etat_V13 == 1:
        vannes_ouverte(370,232.5)
        etat_V13 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()  
    try:
        Fond.delete(finir)
    except:
        None
def vanne_V12_bouton():
    global etat_V12,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etat_V12 == 0:
            vannes_fermer(200,282.5)
            etat_V12 = 1
    elif etat_V12 == 1:
            vannes_ouverte(200,282.5)
            etat_V12 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    try:
        Fond.delete(finir)
    except:
        None
def vanne_V23_bouton():
    global etat_V23,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etat_V23 == 0:
        vannes_fermer(385,302.5)
        etat_V23 = 1
    elif etat_V23 == 1:
        vannes_ouverte(385,302.5)
        etat_V23 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    try:
        Fond.delete(finir)
    except:
        None

def pompe_12_bouton():
    global etatP12,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etatP12 == 0:
            Fond.itemconfigure(pompe_12, outline = 'gray')
            etatP12 = 1
    elif etatP12 == 1:
            Fond.itemconfigure(pompe_12, outline = '#000fff000')
            etatP12 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    try:
        Fond.delete(finir)
    except:
        None
def pompe_22_bouton():
    global etatP22,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etatP22 == 0:
            Fond.itemconfigure(pompe_22, outline = 'gray')
            etatP22 = 1
    elif etatP22 == 1:
            Fond.itemconfigure(pompe_22, outline = '#000fff000')
            etatP22 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    try:
        Fond.delete(finir)
    except:
        None
def pompe_32_bouton():
    global etatP32,ftres1, ftres2, ftres3, nombre_de_coup
    nombre_de_coup += 1
    if etatP32 == 0:
            Fond.itemconfigure(pompe_32, outline = 'gray')
            etatP32 = 1
    elif etatP32 == 1:
            Fond.itemconfigure(pompe_32, outline = '#000fff000')
            etatP32 = 0
    # appelle des fontions pour mettre a jour a chaque clique de boutons
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    remplir_reservoirs()
    ftres1, ftres2, ftres3 = tuyaux_carburant()
    try:
        Fond.delete(finir)
    except:
        None
# mise a jour des clique gauche et droit en mode exercice c'est interdit
def new_clique_gauche(event):
    # fait apparaitre la moyenne des notes et toutes les notes du pilote
    global X, Y, histo, pseudo
    # renvoie la position de la souris lors du clique gauche
    X = event.x
    Y = event.y
    if 500 < X < 580  and  5< Y < 50 :
        try:
            for idx,n in enumerate(histo[pseudo]):
                print('Exercice{}: {}/10'.format(idx,n))
                moyenne = sum(histo[pseudo])/len(histo[pseudo])
            print('Moyenne: {}'.format(moyenne))
            if moyenne <= 5:
                print("Il faut encore s'entrainer {}".format(pseudo))
            else:
                print(" Trés bon résultat {}".format(pseudo))
        except:
            None
    else:
        print("ceci est interdit en mode exercice: n'utiliser que le tableau de bord")
# mise a jour des clique gauche et droit en mode exercice c'est interdit
def new_clique_droit(event):
    print("ceci est interdit en mode exercice: n'utiliser que le tableau de bord")
#mode exercice
def mode_exercice():
    global croix11, croix12, croix21, croix22, croix31, croix32, etatP11, etatP12, etatP21, etatP22, etatP31, etatP32, etat_tank1, etat_tank2, etat_tank3, etat_M1, etat_M2, etat_M3, les_croix, etat_V12, etat_V13, etat_V23, etat_VT23, etat_VT12, finir, nombre_de_coup, point_negatif, nombre_de_coup_optimale, note_et_moyenne, histo, pseudo
    # conditions pour verifier que l'exercice est finis donc tout les moteur en marche
    if etat_M1 == etat_M2 == etat_M3 == 0:
        Fond.bind("<Button-1>", new_clique_gauche)
        Fond.bind("<Button-3>", new_clique_droit)
        # demande du pseudo si le pilote ne la pas rentrer
        try:
            pseudo
        except:
            pseudo = input("saisissez votre nom d'utilisateur: ")
        # creation d'un boutons pour affiche les notes
        note_et_moyenne =Fond.create_rectangle(500 ,5, 580, 50, fill = "black", outline= 'cyan')
        Fond.create_text(545, 25, fill = "white", text = "Notes", font= ('bold', 20))
        # calcule de la note du pilote
        try:
            if nombre_de_coup_optimale == nombre_de_coup:
                note = [10,10]
            elif nombre_de_coup_optimale +1 == nombre_de_coup:
                note = [9,10]
            elif nombre_de_coup_optimale +2 == nombre_de_coup:
                note = [7,10]
            elif nombre_de_coup_optimale +3 == nombre_de_coup:
                note = [6,10]
            elif nombre_de_coup_optimale +4 == nombre_de_coup:
                note = [4,10]
            elif nombre_de_coup_optimale +5 == nombre_de_coup:
                note = [2,10]
            elif nombre_de_coup_optimale +6 == nombre_de_coup:
                note = [1,10]
            else:
                note = [0,10]
            note[0] -= point_negatif #les points negatif sont si le pilote clique sur suivant sans voir qu'un moteur n'est pas alimenter
            if note[0]<0:
                note[0] = 0
        except:
            note = []
        # ajout de la note dans la base de donné en fonction du pseudo
        histo = BD_Historique(pseudo, note)

        #remise a zero de toute les variable pour le prochaine exercice
        point_negatif = 0
        nombre_de_coup= 0
        button_mode_exercice.configure(text = 'Exercice\nsuivant')   
        Fond.itemconfigure(Tank1, fill = "orange", outline = 'white')
        etat_tank1 = 'plein'
        Fond.itemconfigure(Tank2, fill = "green", outline = 'white')
        etat_tank2 = 'plein'
        Fond.itemconfigure(Tank3, fill = "yellow", outline = 'white')
        etat_tank3 = 'plein'
        vannes_ouverte(200,107.5)
        etat_VT12 = 0
        vannes_ouverte(385,107.5)
        etat_VT23 = 0
        vannes_ouverte(370,232.5)
        etat_V13 = 0
        vannes_ouverte(200,282.5)
        etat_V12 = 0
        vannes_ouverte(385,302.5)
        etat_V23 = 0
        etatP11 = 0
        etatP12 = 1
        Fond.itemconfigure(pompe_12, outline = 'gray')
        etatP21 = 0
        etatP22 = 1
        Fond.itemconfigure(pompe_22, outline = 'gray')
        etatP31 = 0
        etatP32 = 1
        Fond.itemconfigure(pompe_32, outline = 'gray')
        #supression de toute les croix
        try:
            for i in les_croix:
                Fond.delete(i[0])
                Fond.delete(i[1])
        except:
            les_croix = []

        # partie qui choisie des pannes aleatoire pendant l'exercice (tout les exercice doive etre faisable)
        pannesecour, pannesecour2, pannesecour3 = 0, 0, 0
        typedepanne = random.randint(1,3)
        if typedepanne == 1 or typedepanne == 3:
            pannepompe = random.randint(1,6)
            if pannepompe == 1 or pannepompe == 4 or pannepompe == 6:
                pannesecour = random.randint(1,2)
                croix11 = panne(80, 160)
                etatP11 = 2
                les_croix.append(croix11)
                if pannesecour == 1:
                    croix12 = panne(120, 160)
                    etatP12 = 2
                    les_croix.append(croix12)
            if pannepompe == 2 or pannepompe == 4 or pannepompe == 5:
                pannesecour2 = random.randint(1,2)
                croix21 = panne(270, 160)
                etatP21 = 2
                les_croix.append(croix21)
                if pannesecour2 == 1 and pannesecour == 2:
                    croix22 = panne(310, 160)
                    etatP22 = 2
                    les_croix.append(croix22)
            if pannepompe == 3 or pannepompe == 5 or pannepompe == 6:
                pannesecour3 = random.randint(1,2)
                croix31 = panne(480, 160)
                etatP31 = 2
                les_croix.append(croix31)
                if pannesecour3 == 1 and pannesecour == 2 and pannesecour2 == 2:
                    croix32 = panne(520, 160)
                    etatP32 = 2
                    les_croix.append(croix32)
        if typedepanne == 2 or typedepanne == 3:
            queltankvide = random.randint(1,6)
            if queltankvide == 1 or queltankvide == 4 or queltankvide == 6:
                Fond.itemconfigure(Tank1, fill = 'gray', outline = "orange", width = 5)
                etat_tank1 = 'vide'
            if queltankvide == 3 or queltankvide == 4 or queltankvide == 5:
                Fond.itemconfigure(Tank3, fill = 'gray', outline = "yellow", width = 5)
                etat_tank3 = 'vide'
            if queltankvide == 2 or queltankvide == 5 or queltankvide == 6:
                Fond.itemconfigure(Tank2, fill = 'gray', outline = "green", width = 5)
                etat_tank2 = 'vide'
        #mise a jour des tuyaux en fonction des pannes aleatoire
        tuyaux_carburant()
        # calcule du nombre de coup qu'il faut pour resoudre l'exercice en fonction des variable choisi par random
        # par exemple si un seule reservoir se vide la meilleur chose a faire c'est ouvrir VT12 ou VT23 (énoncé du projet)
        # donc la note est calculer en fonction a la fin de l'exercice
        if typedepanne == 2: 
            if queltankvide == 1 or queltankvide ==2 or queltankvide ==3:
                nombre_de_coup_optimale = 1
            elif queltankvide == 4 or queltankvide ==5 or queltankvide ==6:
                nombre_de_coup_optimale = 2
        if typedepanne == 1: 
            if pannepompe == 1 or pannepompe == 2 or pannepompe ==3 :
                nombre_de_coup_optimale = 1
                if  pannesecour == 1 or  (pannesecour2 == 1 and pannesecour == 2) or  (pannesecour3 == 1 and pannesecour2 ==2 and pannesecour == 2):
                    nombre_de_coup_optimale = 2
            elif pannepompe == 4 or pannepompe == 5 or pannepompe ==6 :
                nombre_de_coup_optimale = 2
                if  pannesecour == 1 or  (pannesecour2 == 1 and pannesecour == 2) or  (pannesecour3 == 1 and pannesecour2 ==2 and pannesecour == 2):
                    nombre_de_coup_optimale = 3
        if typedepanne == 3:
            if queltankvide == 1 or queltankvide ==2 or queltankvide ==3:
                nombre_de_coup_optimale = 1
                if pannepompe == 1 or pannepompe == 2 or pannepompe ==3 :
                    nombre_de_coup_optimale += 1
                    if  pannesecour == 1 or  (pannesecour2 == 1 and pannesecour == 2) or  (pannesecour3 == 1 and pannesecour2 ==2 and pannesecour == 2):
                        nombre_de_coup_optimale = 2
                elif pannepompe == 4 or pannepompe == 5 or pannepompe ==6 :
                    nombre_de_coup_optimale = 3
                    if  pannesecour == 1 or  (pannesecour2 == 1 and pannesecour == 2) or  (pannesecour3 == 1 and pannesecour2 ==2 and pannesecour == 2):
                        nombre_de_coup_optimale = 3
            elif queltankvide == 4 or queltankvide ==5 or queltankvide ==6:
                nombre_de_coup_optimale = 2
                if pannepompe == 1 or pannepompe == 2 or pannepompe ==3 :
                    nombre_de_coup_optimale = 3
                    if  pannesecour == 1 or  (pannesecour2 == 1 and pannesecour == 2) or  (pannesecour3 == 1 and pannesecour2 ==2 and pannesecour == 2):
                        nombre_de_coup_optimale = 4
                elif pannepompe == 4 or pannepompe == 5 or pannepompe ==6 :
                    nombre_de_coup_optimale = 4
                    if  pannesecour == 1 or  (pannesecour2 == 1 and pannesecour == 2) or  (pannesecour3 == 1 and pannesecour2 ==2 and pannesecour == 2):
                        nombre_de_coup_optimale = 4
    else:
        #creer un texte d'erreur si l'exercice n'est pas finis
        finir = Fond.create_text(300, 20, fill = "black", text = "Finissez l'exercice s'il vous plait", font= ('bold', 15))
        point_negatif += 1


repere_annonce = 1
def BD_Historique(pseudo ,liste_de_note):
    global repere_annonce
    # grace a la libraire json et un fichier.json sauvegarde d'un dictionnaire qui sert de base de donner {pseudo:[notes]}
    with open('historique.json', 'r') as file1:
        historique = json.load(file1)
    if pseudo in historique:
        if repere_annonce == 1:
            print('Vous avez deja une session')
            repere_annonce = 2
        for n in liste_de_note:
            historique[pseudo].append(n)
    else:
        if repere_annonce == 1:
            print('Vous ete un nouveau pilote')
            repere_annonce = 2
        historique[pseudo] = liste_de_note

    with open('historique.json', 'w') as file2:
        json.dump(historique, file2)
    return historique


###Tableau de bord
# creation de la fenetre tableau de bord
tableau_de_bord = tk.Tk()
tableau_de_bord.title("Tableau de bord")
tableau_de_bord.resizable(width=False, height=False)
tableau_de_bord.geometry("600x300+800+150")
tableau_de_bord.config(background= 'black')

# creation des 9 boutons sur la fenetre tableau de bord
button_VT12 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "VT12", fg = 'white', borderwidth = 8, relief = 'groove', command= vanne_VT12_bouton) 
button_VT12.grid(column= 1, row = 0)
button_VT12.configure(cursor ='hand2')
button_VT23 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "VT23", fg = 'white', borderwidth = 8, relief = 'groove', command= vanne_VT23_bouton) 
button_VT23.grid(column= 6, row = 0)
button_VT23.configure(cursor ='hand2')
button_P12 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "P12", fg = 'white', borderwidth = 8, relief = 'groove', command= pompe_12_bouton) 
button_P12.grid(column= 1, row = 1)
button_P12.configure(cursor ='hand2')
button_P22 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "P22", fg = 'white', borderwidth = 8, relief = 'groove', command= pompe_22_bouton) 
button_P22.grid(column= 3, row = 1)
button_P22.configure(cursor ='hand2')
button_P32 = tk.Button(tableau_de_bord,font = 30, bg = "black", width = 12, height = 3, text = "P32", fg = 'white', borderwidth = 8, relief = 'groove', command= pompe_32_bouton)
button_P32.grid(column= 6, row = 1)
button_P32.configure(cursor ='hand2')
button_V12 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "V12", fg = 'white', borderwidth = 8, relief = 'groove', command= vanne_V12_bouton) 
button_V12.grid(column= 1, row = 2)
button_V12.configure(cursor ='hand2')
button_V13 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "V13", fg = 'white', borderwidth = 8, relief = 'groove', command= vanne_V13_bouton) 
button_V13.grid(column= 3, row = 2)
button_V13.configure(cursor ='hand2')
button_V23 = tk.Button(tableau_de_bord, font = 30, bg = "black", width = 12, height = 3, text = "V23", fg = 'white', borderwidth = 8, relief = 'groove', command= vanne_V23_bouton) 
button_V23.grid(column= 6, row = 2)
button_V23.configure(cursor ='hand2')
button_mode_exercice = tk.Button(tableau_de_bord, font = 30, bg = "green", width = 12, height = 3, text = "Exercice\npratique", fg = 'black', borderwidth = 8, relief = 'groove', command= mode_exercice) 
button_mode_exercice.grid(column= 3, row = 0)
button_mode_exercice.configure(cursor ='hand2')

# carre noir seulement pour espacer les boutons
carre = tk.Canvas(tableau_de_bord, width=70, height=300, bg = "black", highlightthickness =0) 
carre.grid(column=0)
carre1 = tk.Canvas(tableau_de_bord, width=30, height=300, bg = "black", highlightthickness =0) 
carre1.grid(column=2)
carre2 = tk.Canvas(tableau_de_bord, width=30, height=300, bg = "black", highlightthickness =0) 
carre2.grid(column=4)

# methode de tkinter afficher les fenetres en continue
tableau_de_bord.mainloop()
systeme_carburant.mainloop()