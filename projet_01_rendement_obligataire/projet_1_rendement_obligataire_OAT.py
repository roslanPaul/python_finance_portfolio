# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 06:19:33 2026

@author: roslanPaul
"""

# =============================================================================
# PROJET 1 — CALCULATEUR DE RENDEMENT OBLIGATAIRE (OAT françaises)
# =============================================================================
# Source libro : Python for Finance — Hilpisch, Chapitres 2-4
# Données réelles : Taux OAT historiques (Banque de France)
# Objectif : Apprendre la syntaxe Python de base en contexte financier réel
# Compétences : int, float, str, list, dict, for, while, if/elif/else, fonctions
# =============================================================================


# -----------------------------------------------------------------------------
# PARTIE 1 — TYPES DE BASE : int, float, str
# -----------------------------------------------------------------------------
# Analogie : ces 3 types sont comme les 3 sortes de briques d'une maison.
#   int    = brique entière (un nombre de jours, un nombre d'années)
#   float  = brique découpée (un taux à virgule : 0.035)
#   str    = étiquette colle sur la brique (le nom "OAT 10 ans")
# Python devient automatiquement le type — on n'a jamais besoin de le déclarer.
# -----------------------------------------------------------------------------

# Un entier : nombre d'années de l'obligation
n_annees = 10
print("Type de n_annees :", type(n_annees)) # <class 'int'>

# Un nombre à virgule : taux annuel en décimal
taux_annuel = 0.035
print("Type de taux_annuel :", type(taux_annuel))  # <class 'float'>

# Une chaîne de caractères : nom de l'obligation
nom_obligation = "OAT 10 ans"
print("Type de nom_obligation :", type(nom_obligation)) # <class 'str'>

# On peut mêler str et float avec une conversion explicite
# Attention : str(O.035 * 100) donne "3.5000000000000004" erreur d'arrondi float !
# On utilise une f-string avec format .2f pour nettoyer l'affichage
print(f"Le taux de {nom_obligation} est de {taux_annuel * 100:.2f}%")

# -----------------------------------------------------------------------------
# PARTIE 2 — LISTE ET DICTIONNAIRE : stocker plusieurs valeurs
# -----------------------------------------------------------------------------
# Analogie : une liste c'est un tiroir où les objets sont rangés par position
#            (le 1er, le 2ème, le 3ème…).
#            Un dictionnaire c'est un tiroir avec des étiquettes :
#            on cherche par NOM, pas par position.
# -----------------------------------------------------------------------------


# Liste des taux OAT 10 ans par an (données réelles approximées, source BdF)
# Format : taux annuel en pourcentage
taux_oat_historique = [
    1.50,   # 2014
    0.90,   # 2015
    0.50,   # 2016
    0.80,   # 2017
    0.70,   # 2018
    0.20,   # 2019
    -0.10,  # 2020 ← taux négatif : réalité post-BCE !
    0.05,   # 2021
    1.20,   # 2022 ← remontée rapide
    3.00,   # 2023
    2.80,   # 2024
    ]

# Les années correspondantes (même liste, même longueur)
années = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Accès par index : la liste commence à 0 en Python (pas à 1)
print("\nPremier taux de la liste :", taux_oat_historique[0]) # 1.50 (année 2014)
print("Dernier taux de la liste :", taux_oat_historique[-1]) # 2.80 (année 2024)
# le [-1] est un raccourci pour "le dernier élément" - très pratique en finance

# Dictionnaire : on associe chaque année à son taux
taux_par_annee = {}
for i in range(len(années)):
    taux_par_annee[années[i]] = taux_oat_historique[i]

print("\nTaux en 2020 : ", taux_par_annee[2020], "%")
print("Taux en 2023 :", taux_par_annee[2023], "%")
