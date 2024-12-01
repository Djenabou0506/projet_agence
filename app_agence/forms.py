from django import forms 
from .models import Auteur, Categorie, Tags, Article

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields ="__all__"

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = "__all__"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"  