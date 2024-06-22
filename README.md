Rapport de Stage : Développement d'une Application de Gestion des Bénéficiaires
École : École Marocaine des Sciences de l’Ingénieur (EMSI)
Département : Informatique
Option : Informatique et Réseaux
Présenté par : Firas Koutari
Encadré par : Mhammed Ben Said (Chef de Service) et Pr. Mbida Mohamed (Encadrant Pédagogique)
Année académique : 2022/2023

Table des Matières
Remerciements
Introduction Générale
Partie Théorique
Introduction
Description
Préparation des environnements
Logigramme Généralisé
Diagramme de cas d’utilisation
Diagramme de classe
Diagramme de séquence
Conclusion
Partie Pratique
Introduction
Contexte de l’application
Démonstration de l’application
Conclusion
Annexes
Extraits de Codes
Captures d’écran
Webographie
Remerciements
Je tiens à exprimer ma profonde gratitude à toutes les personnes qui ont contribué à la réussite de ce stage au sein de la Direction Provinciale de l'Habitat et de la Politique de la Ville de Settat. Un remerciement spécial à Monsieur Mhammed Ben Said pour cette opportunité unique et à Monsieur Mohamed Mbida pour ses conseils précieux tout au long de cette période. Je remercie également ma famille et mes amis pour leur soutien indéfectible.

Introduction Générale
Le stage en milieu professionnel est une étape cruciale dans le parcours académique, offrant l'opportunité de mettre en pratique les connaissances acquises. Du 3 juillet 2023 au 31 juillet 2023, j'ai effectué un stage au sein de la Direction Provinciale de l'Habitat et de la Politique de la Ville de Settat, axé sur le développement d'une application web pour la gestion des bénéficiaires.

Partie Théorique
Introduction
La gestion des bénéficiaires est essentielle pour assurer le succès des projets d'habitat et de politique de la ville. Cette gestion couvre la collecte, la mise à jour et la gestion des informations des bénéficiaires, permettant une distribution équitable des avantages.

Description
L'application développée est une plateforme intuitive pour gérer les informations des bénéficiaires, offrant des fonctionnalités telles que l'inscription des utilisateurs, une connexion sécurisée et la mise à jour des données.

Préparation des environnements
Pour garantir une expérience de développement fluide, nous avons utilisé Django, HTML, CSS et JavaScript, en créant des environnements virtuels dédiés pour gérer les dépendances. Des tests rigoureux ont été effectués pour assurer la qualité de l'application.

Logigramme Généralisé
(Figure 1 : Logigramme)

Diagramme de cas d’utilisation
(Figure 2 : Diagramme de cas d’utilisation)

Diagramme de classe
(Figure 3 : Diagramme de classe)

Diagramme de séquence
Inscription
(Figure 4 : Diagramme de séquence sur l’inscription)

Gestion des bénéficiaires
(Figure 5 : Diagramme de séquence gestion bénéficiaires)

Exporter en Excel
(Figure 6 : Diagramme de séquence Exporter en Excel)

Conclusion
La gestion efficace des bénéficiaires est cruciale pour le succès des projets d'habitat et de politique de la ville. L'application développée offre une plateforme efficace pour gérer ces informations, contribuant à l'optimisation des projets.

Partie Pratique
Introduction
Cette section se concentre sur la mise en œuvre pratique de l'application, en présentant ses fonctionnalités clés à travers des captures d'écran et des explications détaillées.

Contexte de l’application
L'application a été développée pour simplifier le suivi des bénéficiaires des projets d'habitat et de politique de la ville, en centralisant les informations et en optimisant leur gestion.

Démonstration de l’application
Page d'Accueil
L'utilisateur voit
une interface conviviale avec des options de navigation claires.

Inscription
Les nouveaux utilisateurs peuvent s'inscrire en fournissant des informations de base, qui sont ensuite vérifiées pour éviter les doublons.

Connexion
Un système de connexion sécurisé permet aux utilisateurs de se connecter à leur compte pour accéder aux fonctionnalités de l'application.

Tableau de Bord
Une vue d'ensemble des informations clés, y compris le nombre de bénéficiaires et les projets en cours.

Gestion des Bénéficiaires
Les utilisateurs peuvent ajouter, modifier, supprimer et consulter les informations des bénéficiaires. Un système de recherche et de filtres avancés est également disponible pour faciliter l'accès rapide aux informations.

Exportation des Données
Les utilisateurs peuvent exporter les données des bénéficiaires en format Excel pour une utilisation hors ligne ou pour des rapports.

Conclusion
L'application développée a permis d'optimiser la gestion des bénéficiaires au sein de la Direction Provinciale de l'Habitat et de la Politique de la Ville de Settat. Elle a facilité la centralisation des informations et amélioré l'efficacité des processus administratifs.

Annexes
Extraits de Codes
python
Copy code
# Exemple de code pour la gestion des bénéficiaires
from django.db import models

class Beneficiary(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
Captures d’écran
Page d'Accueil : (Capture 1)
Inscription : (Capture 2)
Connexion : (Capture 3)
Tableau de Bord : (Capture 4)
Gestion des Bénéficiaires : (Capture 5)
Exportation des Données : (Capture 6)
Webographie
Documentation Django : https://docs.djangoproject.com/
Tutoriels HTML et CSS : https://www.w3schools.com/
Références JavaScript : https://developer.mozilla.org/en-US/docs/Web/JavaScript
