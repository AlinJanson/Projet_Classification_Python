# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:10:41 2024

@author: paull
"""



import csv
import math

## fonction annexe
def distance(L1,L2):
    a=0
    for i in range(len(L1)):
        a=a+(L1[i]-L2[i])**2
    return math.sqrt(a)

def indice_max(L):
    a=0
    b=L[0]
    for i in range(len(L)):
        if b<=L[i]:
            a=i
            b=L[i]
    return a

# Ouvrir le fichier et lire les données
with open('train_txt.txt', 'r') as file:
    data = []
    for line in file:
        row = line.strip().split(',')
        data.append(row)
    for i in range(len(data)):
        for j in range(9):
            data[i][j]=float(data[i][j])

#ouvrir le fichier test pour tester l'algo knn

with open('test_txt.txt', 'r') as file:
    data1 = []
    for line in file:
        row = line.strip().split(',')
        data1.append(row)
    for i in range(len(data1)):
        for j in range(8):
            data1[i][j]=float(data1[i][j])


#création d'une liste qui prend que les paramètres numériques afin d'appliquer la fonction distance
data_float=[]
for i in range(len(data)):
    data_float.append(data[i][1:-1])

data1_float=[]
for i in range(len(data1)):
    data1_float.append(data1[i][1:])


##algorithme knn

def knn(k,L):
    dist_list=[[] for i in range(len(data))]
    for i in range(len(data)):
        dist_list[i].append(distance(L,data_float[i]))
        dist_list[i].append(data[i][-1])
    dist_list=sorted(dist_list, key=lambda x: x[0])
    label=set()
    for i in range(k):
        label.add(dist_list[i][1])
    label_list=list(label)
    frequence=[]
    for i in range(len(label_list)):
        b=0
        for j in range(k):
            if dist_list[j][1]==label_list[i]:
                b=b+1
        frequence.append(b)
    return label_list[indice_max(frequence)]
    
 ## tester les resultats du knn avec les données du fichier test_fleur   
A=[]
for i in range(len(data1)):
    A.append(knn(1,data1_float[i]))
  




import pandas as pd

A=[int(A[i]) for i in range(len(A))]
# Données pour les deux colonnes
data = {
    "Id": [i for i in range(1030,5030)],
    "Label": A
}

# Créer un DataFrame avec les données
df = pd.DataFrame(data)

# Écrire le DataFrame dans un fichier Excel
df.to_csv('fichier.csv', index=False)

print("Fichier Excel 'fichier.xlsx' créé avec succès.")


