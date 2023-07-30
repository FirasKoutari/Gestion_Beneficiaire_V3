from django import forms
from .models import Beneficiaire, Conjoint, Enfant, OrigineBeneficiaire, InformationOperation

class BeneficiaireForm(forms.ModelForm):
    class Meta:
        model = Beneficiaire
        fields = '__all__'

class ConjointForm(forms.ModelForm):
    class Meta:
        model = Conjoint
        fields = '__all__'

class EnfantForm(forms.ModelForm):
    class Meta:
        model = Enfant
        fields = '__all__'

class OrigineBeneficiaireForm(forms.ModelForm):
    class Meta:
        model = OrigineBeneficiaire
        fields = '__all__'

class InformationOperationForm(forms.ModelForm):
    class Meta:
        model = InformationOperation
        fields = '__all__'
