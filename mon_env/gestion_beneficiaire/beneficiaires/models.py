from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    login = models.CharField(max_length=255, primary_key=True)
    mot_de_passe = models.CharField(max_length=255)

class Beneficiaire(models.Model):
    #les attributs
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

class Enfant(models.Model):
    id_enfant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    class Meta:
        ordering = ['nom']

class OrigineBeneficiaire(models.Model):

    #les variables
    villes = [
        ('Settat','Settat'),
    ]
    communes = [
        ('commune_Settat','commune_Settat'),
    ]
    douars = [
        ('kilaz','kilaz'),
    ]
    #les attributs
    ville = models.CharField(max_length=255,choices=villes)
    commune = models.CharField(max_length=255,choices=communes)
    douar = models.CharField(max_length=255,choices=douars)
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.ville
    class Meta:
        ordering = ['ville']

class InformationOperation(models.Model):
    #variables

    operateurs = [
        ('Alomrane','Alomrane'),
    ]
    type_inter = [
        ('type1','type1'),
        ('type2','type2'),
    ]
    #les attributs

    num_pv = models.CharField(max_length=255)
    operateur = models.CharField(max_length=255,choices=operateurs)
    nom_operation = models.CharField(max_length=255)
    num_ressencement = models.CharField(max_length=255)
    date_ressencement = models.DateField(null=True,default=None)
    date_affectation = models.DateField(null=True,default=None)
    type_intervention = models.CharField(max_length=255, choices=type_inter)
    prix_produit = models.DecimalField(max_digits=10, decimal_places=2)
    subvention_fshiu = models.DecimalField(max_digits=10, decimal_places=2)
    date_demolition = models.DateField(null=True,default=None)
    num_lot = models.CharField(max_length=255)
    fichier_joint = models.FileField(upload_to='uploads/')
    observation = models.TextField()
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_operation
    class Meta:
        ordering = ['nom_operation']
