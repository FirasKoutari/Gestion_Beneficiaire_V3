# Gestion des Bénéficiaires

## Introduction Générale

L'agent de saisie est chargé de la gestion des bénéficiaires d'une province dont l'ajout des nouveaux bénéficiaires, la recherche et le contrôle des  bénéficiaires.

---

## Partie Théorique

### Logigramme généralisé

![image](https://github.com/user-attachments/assets/dde3b0cb-142e-4507-8ef9-413eac5c7c43)


### Diagramme de cas d’utilisation

![image](https://github.com/user-attachments/assets/deea49e4-d960-4129-b385-0640985b6171)


### Diagramme de classe

![image](https://github.com/user-attachments/assets/eab82d98-873f-4d50-ac40-3985d010ab73)


### Diagramme de séquence
#### 1.	L’inscription
![image](https://github.com/user-attachments/assets/3d07d21d-1671-4bf9-939e-48ed0073e7b4)

#### 2.	Gestion du bénéficiaires
![image](https://github.com/user-attachments/assets/189b9847-70af-4304-88b4-c70fb8513488)

#### 3.	Exporter en excel
![image](https://github.com/user-attachments/assets/1c64c2c3-d4dd-4f06-944a-d47a15452a2e)



## Partie Pratique

### Authentification
Pour vous connecter, rendez-vous sur le site localhost/gb , Ci-dessous une 
capture d’écran représentant la page d’authentification de l'application:

![image](https://github.com/user-attachments/assets/e5ccbbb0-5dd6-4c5b-88f9-f96261e037fa)
![image](https://github.com/user-attachments/assets/3ec4bec6-0f91-43ef-ac7d-ac9f4a84a930)

Il ne vous reste plus qu'à saisir les codes de connexion (Identifiant et mot de passe). Ces derniers vous sont délivrés par votre administrateur. Une fois identifié, vous arriverez sur la page gestion des bénéficiaires.

### Création d'un nouveau bénéficiaire
La création d’un bénéficiaire passe par trois étapes successives :

1- Informations sur le bénéficiaires

2- L'origine du bénéficiaire

3- Informations sur l'opération

Pour créer un bénéficiaire, Cliquez sur le bouton: ajouter un bénéficiaire.
Dans le menu, cliquez sur "Gestion de bénéficiaire", une liste des bénéficiaires 
ajoutées sous forme d'une table s'affichera. Afin de modifier un bénéficiaire 
cliquez sur le bouton action, un menu déroulant s'affichera, puis cliquez sur 
modifier.
Pour supprimer un bénéficiaire, Cliquez sur le bouton action, puis sur 
supprimer. 
Pour consulter le détail d'un bénéficiaire, cliquez sur le bouton action puis sur 
détail. Une nouvelle fenêtre apparaît sur laquelle s'affiche le détail complet du
bénéficiaire.

![image](https://github.com/user-attachments/assets/005a141c-6e85-47bc-af91-ef7c80b579d6)

### Contrôle des bénéficiaires
Cette page a comme but de rechercher et détecter si une personne a déjà été 
bénéficier ou non. Cette fonctionnalité donne la possibilité de rechercher par 
un groupe des personnes.

![image](https://github.com/user-attachments/assets/6883d3ab-83d0-48dd-8e00-811de1c3922d)

### Exportation en Excel

L'application offre la possibilité d'exporter les données des bénéficiaires et des opérations au format Excel. Cette fonctionnalité permet aux utilisateurs d'analyser les données hors ligne et de générer des rapports pour des besoins spécifiques.

![image](https://github.com/user-attachments/assets/7be92d3c-80cd-447f-9de3-73459ac070e2)

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
