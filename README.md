\# 🏠 Finance Python Curriculum

> \*\*12 projets Python — données réelles — de zéro à pipeline production\*\*



On construit une \*\*maison de finance\*\*. Chaque acte pose une couche indispensable. Chaque brique est faite avec du bois réel — pas du contreplaqué simulé.



---



\## 📦 Environnement



| Outil | Rôle |

|---|---|

| `Python 3.10+` | Language principal |

| `yfinance` | Téléchargement cours boursiers |

| `pandas` / `numpy` | Manipulation \& calcul |

| `statsmodels` | Régression classique |

| `scikit-learn` | ML classique (LogReg, RF, CV) |

| `xgboost` | Gradient Boosting |

| `shap` | Interprétabilité ML |

| `plotly` | Dashboard interactif |

| `openpyxl` | Génération Excel |

| `matplotlib` / `seaborn` | Visualisation |



---



\## 🗺️ Structure du curriculum



```

curriculum/

├── acte1\_fondations/

│   ├── projet01\_obligataire/

│   ├── projet02\_cac40\_numpy/

│   └── projet03\_lending\_club\_eda/

├── acte2\_les\_murs/

│   ├── projet04\_regression\_bnp/

│   ├── projet05\_scoring\_credit/

│   ├── projet06\_var\_cac40/

│   └── projet07\_cross\_validation/

├── acte3\_ameublement/

│   ├── projet08\_ridge\_lasso\_insee/

│   ├── projet09\_rf\_xgboost\_lending/

│   └── projet10\_shap\_dashboard/

├── acte4\_electricite/

│   ├── projet11\_option\_pricing/

│   └── projet12\_pipeline\_end\_to\_end/

└── README.md

```



---



\## 🏗️ Acte 1 — Fondations



> Syntaxe, structures de données, exploration. Les briques de base.



\### Projet 1 — Calculateur de rendement obligataire OAT



\*\*Dataset :\*\* Taux OAT historiques — CSV gratuit Banque de France  

\*\*Livre :\*\* \*Python for Finance\*  

\*\*Compétences :\*\* Syntaxe Python, boucles, fonctions, types



Tu calcules la valeur d'un portefeuille obligataire sur 10 ans avec les taux réels, année par année.



> 💡 \*\*Analogie :\*\* C'est comme suivre ton compte bancaire avec les vrais taux que t'as eu chaque année — pas des taux inventés.



---



\### Projet 2 — Analyse de cours boursiers CAC40 avec NumPy



\*\*Dataset :\*\* Cours historiques des 10 + grandes actions CAC40 sur 3 ans — `yfinance` (TotalEnergies, LVMH, Sanofi, BNP Paribas…)  

\*\*Livre :\*\* \*Python for Finance\*  

\*\*Compétences :\*\* Vectorisation NumPy, manipulation de matrices



Tu construis la matrice des rendements quotidiens, calcules la matrice de corrélation, les écarts-types annualisés, et tu identifies les actions les plus / moins corrélées.



> 💡 \*\*Analogie :\*\* T'as 10 actionnaires dans une salle. NumPy te permet de mesurer en une seconde comment ils votent ensemble — c'est la corrélation.



---



\### Projet 3 — Nettoyage et exploration des données Lending Club



\*\*Dataset :\*\* Lending Club — Kaggle (150 000+ prêts personnels réels)  

\*\*Livre :\*\* \*Python for Finance\*  

\*\*Compétences :\*\* Pandas intensif, nettoyage de données, EDA



Tu charges le CSV, tu nettoyes les colonnes problématiques (pourcentages en string, valeurs manquantes, outliers), tu fais l'EDA complète : distributions, corrélations, taux de défaut par catégorie.



> 💡 \*\*Analogie :\*\* Lending Club, c'est comme un fichier client réel d'une banque — il est sale, incomplet, et c'est exactement comme ça qu'on travaille dans la vraie vie.



---



\## 🧱 Acte 2 — Les Murs



> Régression, classification, évaluation rigoureuse. On monte les murs.



\### Projet 4 — Régression linéaire sur cours boursiers réels



\*\*Dataset :\*\* Même données `yfinance` du Projet 2  

\*\*Livre :\*\* \*ISLP — Ch.3\*  

\*\*Compétences :\*\* Régression simple \& multiple, statsmodels, interprétation



Tu prédit le cours de BNP Paribas à J+1 à partir du cours à J, du volume, du cours de Société Générale, et du CAC40. Tu interprètes R², p-values, et tu montres pourquoi les features décalées (lagged) sont cruciales.



> 💡 \*\*Analogie :\*\* T'essaies de prédire demain la pluie en regardant aujourd'hui le baromètre, la température et le ciel. La régression te dit quelle variable compte le plus.



---



\### Projet 5 — Scoring crédit avec Logistic Regression



\*\*Dataset :\*\* Default — ISLP (10 000 clients, données carte de crédit réelles)  

\*\*Livre :\*\* \*ISLP — Ch.4\*  

\*\*Compétences :\*\* Classification, odds ratios, confusion matrix, confounding



Tu prédit la probabilité de défaut via logistic regression. Tu montres le paradoxe de confounding : les étudiants ont un taux de défaut plus élevé globalement, mais plus bas pour un même niveau de balance.



> 💡 \*\*Analogie :\*\* La logistic regression, c'est une porte avec un curseur. Le balance du client pousse le curseur vers « défaut » — le modèle apprend exactement à quel point cette porte s'ouvre.



---



\### Projet 6 — VaR sur portefeuille CAC40 \*(simulation calibrée)\*



\*\*Dataset :\*\* Cours historiques des 5 actions CAC40 via `yfinance` + simulation Monte Carlo calibrée  

\*\*Livre :\*\* \*Python for Finance — Ch.10\*  

\*\*Compétences :\*\* VaR historique, Monte Carlo, comparaison de méthodes



Tu calcules d'abord le VaR historique directement sur les données réelles (méthode 1). Puis tu estimes volatilité et corrélations sur ces mêmes données pour faire une simulation Monte Carlo (méthode 2). La simulation existe uniquement pour explorer des scénarios que les données historiques ne couvrent pas — mais elle reste 100% ancrée dans la réalité.



> 💡 \*\*Analogie :\*\* Le VaR historique, c'est regarder dans le rétroviseur. Le Monte Carlo calibré, c'est regarder dans le rétroviseur pour imaginer ce qui pourrait arriver demain.



---



\### Projet 7 — Cross-validation sur le scoring crédit



\*\*Dataset :\*\* Même Default de ISLP du Projet 5  

\*\*Livre :\*\* \*ISLP — Ch.5\*  

\*\*Compétences :\*\* Validation set, LOOCV, 5-Fold CV, courbe bias-variance



Tu reprends exactement le même modèle logistique du Projet 5, mais tu l'évalues correctement cette fois. Tu traces la courbe en U bias-variance et tu montres que l'erreur d'entraînement te mentit systématiquement.



> 💡 \*\*Analogie :\*\* Dans le Projet 5, t'avais évalué ton modèle sur les mêmes données qu'il avait vues — c'est comme évaluer un élève sur les questions qu'il avait déjà pratiquées. Ici, on fait un vrai examen.



---



\## 🛋️ Acte 3 — L'Ameublement



> Régularisation, ensembles, interprétabilité. On meuble la maison.



\### Projet 8 — Ridge vs Lasso sur données macroéconomiques INSEE



\*\*Dataset :\*\* Données économiques françaises sur 20 ans trimestriels — INSEE (CSV gratuit)  

\*\*Livre :\*\* \*ISLP — Ch.6\*  

\*\*Compétences :\*\* Régularisation, sélection de variables, chemins des coefficients



Tu prédit le taux de chômage à partir des autres indicateurs (PIB, inflation, indice industriel…). Tu compares OLS, Ridge, et Lasso, et tu traces les chemins des coefficients selon lambda.



> 💡 \*\*Analogie :\*\* Ridge comprime toutes tes dépenses mensuelles de 10%. Lasso, plus brutal — il coupe complètement le Netflix, la salle de sport, et les magazines, et garde uniquement l'alimentation et le loyer.



---



\### Projet 9 — Random Forest vs XGBoost sur Lending Club



\*\*Dataset :\*\* Même Lending Club du Projet 3 — mode classification  

\*\*Livre :\*\* \*ISLP — Ch.8\*  

\*\*Compétences :\*\* Ensembles, AUC-ROC, feature importances, courbes d'apprentissage



Tu prédit le défaut (`fully\_paid` vs `charged\_off`) avec Random Forest puis Gradient Boosting. Tu compares les AUC-ROC et tu extrais les feature importances.



> 💡 \*\*Analogie :\*\* Un arbre de décision, c'est un conseiller bancaire qui dit « si le revenu est bas ET le détenu depuis moins de 2 ans, alors risque élevé ». Random Forest, c'est un jury de 500 conseillers bancaires — on prend le vote majoritaire.



---



\### Projet 10 — SHAP + Dashboard interactif sur le modèle crédit



\*\*Dataset :\*\* Même modèle du Projet 9 (Lending Club + XGBoost)  

\*\*Livre :\*\* \*ISLP — Ch.8\*  

\*\*Compétences :\*\* SHAP values, interprétabilité ML, Plotly dashboard



Tu codes un dashboard Plotly interactif qui montre, pour un emprunteur donné : sa probabilité de défaut, les 5 features qui ont poussé la décision, et un scénario « et si son revenu augmentait de 20% ».



> 💡 \*\*Analogie :\*\* SHAP, c'est comme un avocat de la défense dans un tribunal. Le modèle a dit « coupable (défaut probable) ». SHAP montre exactement pourquoi — quelles preuves ont pesé le plus.



---



\## ⚡ Acte 4 — L'Électricité



> Pricing avancé, orchestration, pipeline reproductible. On branche tout.



\### Projet 11 — Option Pricing : BSM analytique vs Monte Carlo calibré



\*\*Dataset :\*\* Données d'options réelles sur le CAC40 via Yahoo Finance (symbole `FCE`) + simulation calibrée  

\*\*Livre :\*\* \*Python for Finance — Ch.10 / Ch.17\*  

\*\*Compétences :\*\* Black-Scholes-Merton, Monte Carlo, Greeks (Delta, Vega), volatilité implicite



Tu récupères le prix du sous-jacent, l'échéance, le strike, tu estimes la volatilité implicite sur ces données réelles. Puis tu compares le prix analytique BSM avec une simulation Monte Carlo qui utilise cette volatilité réelle. La simulation reste nécessaire ici pour pricer des options que BSM ne peut pas gérer (options américaines via LSM).



> 💡 \*\*Analogie :\*\* BSM analytique, c'est la formule exacte pour calculer la surface d'une sphère. Monte Carlo, c'est lancer des fléchettes aléatoirement sur une sphère et estimer la surface par la proportion qui touche — si on calibre la taille de la sphère sur la réalité, le résultat converge vers le même nombre.



---



\### Projet 12 — Pipeline end-to-end : données réelles → modèle → rapport Excel



\*\*Dataset :\*\* Lending Club (Kaggle) comme source connectée  

\*\*Livre :\*\* \*Curriculum Phase 4\*  

\*\*Compétences :\*\* Orchestration, openpyxl, pipeline reproductible



Le script Python télécharge les données, nettoye automatiquement, charge le modèle XGBoost du Projet 9, score tous les nouveaux emprunteurs, et génère un rapport Excel : onglet récapitulatif, onglet clients à risque élevé triés par score, onglet visualisations.



> 💡 \*\*Analogie :\*\* Les 11 projets précédents t'ont appris à construire chaque pièce de la maison séparément. Ce projet les connecte toutes — l'eau coule, l'électricité marche, la chauffage s'allume automatiquement le matin.



---



\## 📊 Résumé



| # | Projet | Acte | Dataset réel | Source |

|---|--------|------|--------------|--------|

| 1 | Rendement obligataire OAT | Fondations | Banque de France CSV | Python for Finance |

| 2 | Cours CAC40 NumPy | Fondations | yfinance (10 actions) | Python for Finance |

| 3 | EDA Lending Club | Fondations | Kaggle Lending Club | Python for Finance |

| 4 | Régression cours BNP / CAC40 | Les Murs | yfinance (même P2) | ISLP Ch.3 |

| 5 | Scoring crédit Default | Les Murs | ISLP Default dataset | ISLP Ch.4 |

| 6 | VaR portefeuille CAC40 | Les Murs | yfinance + sim. calibrée | Python for Finance Ch.10 |

| 7 | Cross-validation Default | Les Murs | ISLP Default dataset | ISLP Ch.5 |

| 8 | Ridge / Lasso macroéco INSEE | L'Ameublement | INSEE CSV gratuit | ISLP Ch.6 |

| 9 | RF vs XGBoost Lending Club | L'Ameublement | Kaggle Lending Club | ISLP Ch.8 |

| 10 | SHAP + Dashboard crédit | L'Ameublement | Même P9 (Lending Club) | ISLP Ch.8 |

| 11 | Option Pricing CAC40 réel | L'Électricité | Yahoo Finance options | Python for Finance Ch.10/17 |

| 12 | Pipeline end-to-end crédit | L'Électricité | Lending Club + Excel | Curriculum Phase 4 |



---



\## 🔗 Liens données



| Source | URL |

|--------|-----|

| Banque de France — taux OAT | \[https://www.banque-de-france.fr](https://www.banque-de-france.fr) |

| INSEE — données macroéconomiques | \[https://www.insee.fr](https://www.insee.fr) |

| Kaggle — Lending Club | \[https://www.kaggle.com/datasets/wordsworth/lending-club-loan-data](https://www.kaggle.com/datasets/wordsworth/lending-club-loan-data) |

| Yahoo Finance — cours \& options | \[https://finance.yahoo.com](https://finance.yahoo.com) |

| ISLP — Default dataset | Fourni avec le livre \*An Introduction to Statistical Learning\* |



---



\## 📚 Références livres



\- \*\*Python for Finance\*\* — Yves Hilpolt \*(base technique Python + finance)\*

\- \*\*ISLP — An Introduction to Statistical Learning\*\* — James, Witten, Hastie, Tibshirani \*(base ML \& statistiques)\*



---

