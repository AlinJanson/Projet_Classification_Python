# KNN Classification Challenge

## Description

Ce projet implémente un algorithme des k plus proches voisins (**K-Nearest Neighbors, KNN**) en utilisant **NumPy** et **Pandas**. 
Il est conçu pour effectuer des classifications sur des ensembles de données fournis sous forme de fichiers CSV. 
L'algorithme prend en charge la métriques de distance :

- Distance Euclidienne

Le modèle est optimisé pour fonctionner avec K=le nobmre de voisin, après une série d’expérimentations sur la plateforme **Kaggle**.

## Auteurs

- **Lin Antoine** (Pseudo Kaggle : Antoine Lin)
- **LU-YEN-TUNG Paul-Adrien** (Pseudo Kaggle : pol-adr1)
- **MALLEM Merwane**(Pseudo Kaggle : merwane_mallem)


## Fonctionnalités

- Chargement des données depuis des fichiers CSV
- Calcul des distances entre les points
- Prédiction de la classe des points de test
- Sauvegarde des prédictions au format CSV

## Installation

1. Assurez-vous d'avoir **Python 3** installé.
2. Installez les dépendances requises avec la commande suivante :
   ```bash
   pip install numpy pandas
   ```
3. Placez vos fichiers `train.csv` et `test.csv` dans le répertoire du projet.

## Utilisation

Exécutez le script **KNN (4).py** avec la commande suivante :

```bash
python Code_python_KNN.py
```

Les prédictions seront enregistrées dans un fichier **fichier.csv**.

## Licence

Projet réalisé dans le cadre d'un challenge Kaggle.