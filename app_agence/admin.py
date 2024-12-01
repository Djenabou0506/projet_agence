from django.contrib import admin
from .models import Categorie, Tags, Article, Auteur, Commentaire 

# Register your models here.
admin.site.register(Categorie),
admin.site.register(Tags),
admin.site.register(Auteur),
admin.site.register(Article)
admin.site.register(Commentaire)
