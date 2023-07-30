from django.contrib import admin
from .models import Utilisateur,Beneficiaire,Conjoint,Enfant,OrigineBeneficiaire,InformationOperation
# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Beneficiaire)
admin.site.register(Conjoint)
admin.site.register(Enfant)
admin.site.register(OrigineBeneficiaire)
admin.site.register(InformationOperation)
