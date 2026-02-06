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

# -----------------------------------------------------------------------------
# PARTIE 3 — BOUCLE FOR : parcourir les données année par année
# -----------------------------------------------------------------------------
# Analogie : un for c'est comme lire un relevé bancaire ligne par ligne.
#            On prend chaque ligne, on fait quelque chose avec, on passe à la suivante.
# -----------------------------------------------------------------------------

print("\n--- Historique des taux OAT 10 ans ---")
for annee, taux in zip(années, taux_oat_historique):
    # zip() colle les deux listes ensemble comme deux colonnes d'un tableau
    if taux < 0:
        commentaire = "NEGATIF"
    elif taux < 1.0:
        commentaire = "Bas"
    elif taux < 2.0: 
        commentaire = "Modéré"
    else:
        commentaire = "Elevé"
    print(f" {annee} : {taux:>5.2f}% → {commentaire}")
    # f"..." = f-string : on insère des variables directement dans la chaine
    # {taux:>5.2f} signifie : aligner à droite (>), largeur 5, 2 décimales (.2f)
    
# -----------------------------------------------------------------------------
# PARTIE 4 — FONCTION : capitalisation avec taux variable année par année
# -----------------------------------------------------------------------------
# Analogie : une fonction c'est une recette de cuisine.
#            On écrit la recette UNE FOIS, puis on l'appelle autant de fois qu'on veut
#            avec des ingrédients différents (les arguments).
# -----------------------------------------------------------------------------

def capitalisation_taux_variable(capital_initial, liste_taux_annuels):
    """
    Calcule la valeur finale d'un capital investissement en obligataire,
    avec un taux qui change chaque année.

    Arguments :
        capital_initial      : montant investi au jour 1 (float)
        liste_taux_annuels   : liste des taux en pourcentage chaque année (list of float)

    Retourne :
        capital_final        : valeur du capital après N années (float)
        historique           : liste des valeurs du capital chaque année (list of float)
    """
    
    capital = capital_initial 
    historique = [capital]
    
    for taux in liste_taux_annuels :
        taux_decimal = taux / 100
        capital = capital * (1 + taux_decimal)  # formule : C(n+1) = C(n) * (1+r)
        historique.append(capital)
    
    return capital, historique      # on retourne DEUX valeurs (tuple)

# On appelle la fonction avec 10 000 € investis en 2014
capital_de_depart = 10000.0
capital_final, historique_capital = capitalisation_taux_variable(capital_de_depart,taux_oat_historique)

print(f"\n--- Simulation    : {capital_de_depart:,.0f}€ investis en OAT 10 ans (2014-2024) ---")
print(f"Capital de départ   : {capital_de_depart:>12,.2f} €")
print(f"Capital final       : {capital_final:>12,.2f} €")
print(f"Gain total          : {((capital_final / capital_de_depart) - 1) * 100:>11.2f} %")

# -----------------------------------------------------------------------------
# PARTIE 5 — BOUCLE WHILE : trouver l'année où le capital dépasse un seuil
# -----------------------------------------------------------------------------
# Analogie : un while c'est comme regarder sa montre en attendant le bus.
#            On répète "n'est-il pas arrivé ?" jusqu'à ce qu'il arrive.
# -----------------------------------------------------------------------------

seuil_cible = 10500.0

print(f"\n--- Quand le capital dépasse {seuil_cible:,.0f}€ ? ---")

i = 0
while i < len(historique_capital):
    if historique_capital[i] >= seuil_cible:
        annee_cible = 2014 + i
        print(f"Le capital a dépassé {seuil_cible:,.0f}€ en {annee_cible} "
              f"(valeur : {historique_capital[i]:,.2f}€")
        break
    i += 1
else:
    # Le bloc 'else' d'un while s'execute SEULEMENT si la boucle finit sans 'break'
    print(f"Le capital n'a jamais dépassé {seuil_cible:,.0f}€ sur la période.")
    
# -----------------------------------------------------------------------------
# PARTIE 6 — FONCTION AVEC ARGUMENT PAR DÉFAUT + COMPARAISON SCÉNARIOS
# -----------------------------------------------------------------------------
# Analogie : les arguments par défaut sont comme une recette avec des ingrédients
#            "standard". On peut en changer un si on veut, sinon on garde le standard.
# -----------------------------------------------------------------------------

def rendement_annuel_moyen(liste_taux):
    """
    Calcule le rendement annuel moyen à partir d'une liste de taux.
    C'est la moyenne arithmétique simple des taux.
    """
    
    return sum(liste_taux) / len(liste_taux)

def simuler_placement(capital_initial=10000.0, duree_annees=5, taux_fixe=None, liste_taux=None):
    """
    Simule un placement obligataire.

    Si liste_taux est fournie → on utilise les taux réels année par année.
    Sinon → on utilise taux_fixe comme taux constant sur duree_annees années.

    Arguments par défaut :
        capital_initial = 10000.0  (le standard)
        duree_annees    = 5
        taux_fixe       = None     (si None, on cherche liste_taux)
    """
    
    if liste_taux is not None:
        # Cas 1 : taux variables réels, on prend les N premiers
        taux_a_utiliser = liste_taux[:duree_annees]
    elif taux_fixe is not None:
        # Cas 2 : taux fixe constant, on crée une liste remplie de ce taux
        taux_a_utiliser = [taux_fixe] * duree_annees
    else:
        print("Erreur : il faut fournir taux_fixe ou liste_taux !")
        return None, None
    
    capital_final, historique = capitalisation_taux_variable(capital_initial, taux_a_utiliser)
    return capital_final, historique