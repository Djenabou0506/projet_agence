from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboad'),
    path('article-by-categorie/<int:categorie_id>/', article_by_categorie, name="article_by_categorie"),
    path('article_detail/<int:article_id>/', article_detail, name='article_detail'),
    path('blog_list/', blog_list, name='blog_list'),
    path('auteur_liste/', auteur_liste, name='auteur_liste'),
    path('auteur_create/', auteur_create, name='auteur_create'),
    path('auteur_update/<int:auteur_id>/', auteur_update, name='auteur_update'),
    path('auteur_delete/<int:auteur_id>/', auteur_delete, name='auteur_delete'),
    path('categorie_liste/', categorie_liste, name='categorie_liste'),
    path('categorie_create/', categorie_create, name='categorie_create'),
    path('categorie_update/<int:categorie_id>/', categorie_update, name='categorie_update'),
    path('categorie_delete/<int:categorie_id>/', categorie_delete, name='categorie_delete'),
    path('tags_liste/', tags_liste, name='tags_liste'),
    path('tags_create/', tags_create, name='tags_create'),
    path('tags_update/<int:tag_id>', tags_update, name='tags_update'),
    path('tags_delete/<int:tag_id>', tags_delete, name='tags_delete'),
    path('article_liste/', article_liste, name='article_liste'),
    path('article_create/', article_create, name='article_create'),
    path('article_update/<int:article_id>', article_update, name='article_update'),
    path('article_delete/<int:article_id>', article_delete, name='article_delete')
]