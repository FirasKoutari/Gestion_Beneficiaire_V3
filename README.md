# Gestion des Bénéficiaires

## Introduction Générale

L'agent de saisie est chargé de la gestion des bénéficiaires d'une province dont 
l'ajout des nouveaux bénéficiaires, la recherche et le contrôle des 
bénéficiaires.

---

## Partie Théorique

### Introduction

L'introduction à la gestion des bénéficiaires revêt une importance significative dans le contexte des projets liés à l'habitat et à la politique de la ville. [...]

### Description

Cette application a été soigneusement conçue dans le but de fournir une plateforme à la fois intuitive et exhaustive, avec pour objectif de rationaliser et d'optimiser la gestion des informations associées aux bénéficiaires. [...]

### Préparation des environnements

La phase de préparation des environnements a revêtu une importance capitale dans le processus de développement de l'application web destinée à la gestion des bénéficiaires. [...]

### Logigramme généralisé

*Insérer Figure 1 ici*

### Diagramme de cas d’utilisation

*Insérer Figure 2 ici*

### Diagramme de classe

*Insérer Figure 3 ici*

### Diagramme de séquence

*Insérer Figures 4 à 6 ici*

### Conclusion

En conclusion de la partie théorique, nous avons plongé profondément dans les principes fondamentaux de la gestion des bénéficiaires. [...]

---

## Partie Pratique

### Introduction

Cette section de la présentation se concentre sur la mise en œuvre pratique de l'application développée pour répondre aux besoins spécifiques de la Direction Provinciale de l'Habitat et de la Politique de la Ville à Settat. [...]

### Contexte de l’application

Le contexte de l'application est étroitement lié à une institution qui s'investit activement dans la réalisation de projets ayant pour objectif d'améliorer les conditions de vie. [...]

### Démonstration de l’application

- Page d'accueil
- Inscription d'un utilisateur
- Connexion à l'application
- Gestion des bénéficiaires
- Exportation en Excel

*Insérer Figures 7 à 11 ici*

### Conclusion

Le contexte de l'application est étroitement lié à une institution qui s'investit activement dans la réalisation de projets visant à améliorer les conditions de vie. [...]

---

## Conclusion Générale

Mon stage au sein de la Direction Provinciale de l'Habitat et de la Politique de la Ville de Settat a été une expérience exceptionnelle qui a enrichi ma formation académique et élargi ma perspective professionnelle. [...]

---

## Annexes

### Extraits du Code

```python
from django.db import models

class Beneficiaire(models.Model):
    cin = models.CharField(max_length=255, primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['nom']

class Conjoint(models.Model):
    cin = models.CharField(max_length=255, primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['nom']
