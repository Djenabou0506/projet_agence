from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categorie, Tags, Auteur, Article, Commentaire
from .forms import AuteurForm, CategorieForm, TagsForm, ArticleForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
   categories = Categorie.objects.all()
   article_liste = Article.objects.all().order_by('-date_publication')
   article_en_avant = Article.objects.filter(en_avant=True).first()
   print(categories)
   context = {
      'categories': categories,
      'articles': article_liste,
      'article_en_avant' : article_en_avant
    }
   return render(request, 'blog/frontoffice/index.html', context)

# trie les articles par date de publication, 5 article par page , recuperer le numero depuis le parametre demande
def blog_list(request):
   articles = Article.objects.all().order_by('date_publication')
   paginator = Paginator(articles, 5)
   page_number = request.GET.get('page')
   page_objets = paginator.get_page(page_number)
   return render(request, 'blog/frontoffice/blog_list.html', {'page_objets': page_objets}) 



def article_detail(request, article_id):
   article = Article.objects.get(id=article_id)
   context = {
      'article':article
   }
   return render(request, 'blog/frontoffice/article_detail.html', context)

def article_by_categorie(request, categorie_id):
    categories = Categorie.objects.all()
    categorie = Categorie.objects.get(id=categorie_id)
    article_en_avant = Article.objects.filter(en_avant=True).first()

    articles = Article.objects.filter(categorie=categorie)
    context = {
        "categories":categories,
        "articles": articles,
        "article_en_avant" : article_en_avant

    }

    return render(request, "blog/article_by_categorie.html", context)

def dashboard(request):
   nombre_article= Article.objects.all().count()
   nombre_auteur= Auteur.objects.all().count()
   context = {
      'nbre_article': nombre_article,
      'nbre_auteur': nombre_auteur
   }
   return render(request, 'blog/backoffice/dashboard.html', context)
  

def auteur_liste(request):
   auteurs = Auteur.objects.all()

   context = {
      'auteurs': auteurs
   }
   return render(request, 'blog/backoffice/auteurs/auteur_liste.html', context)


def auteur_create(request):
   form = AuteurForm
   if request.method=='POST':
      form = AuteurForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('auteur_liste')
   context = {
      "form": form
   }
   return render(request,'blog/backoffice/auteurs/auteur_create.html',context)


def auteur_update(request, auteur_id):
   auteur = Auteur.objects.get(pk=auteur_id)
   form = AuteurForm(instance=auteur)
   if request.method=='POST':
      form = AuteurForm(instance=auteur, data=request.POST)
      if form.is_valid():
         form.save()
         return redirect('auteur_liste')
   context = {
      'form': form
   }
   return render(request,'blog/backoffice/auteurs/auteur_update.html',context)


def auteur_delete(request, auteur_id):
   auteur = Auteur.objects.get(pk=auteur_id)
   auteur.delete()
   return redirect('auteur_liste')


def categorie_liste(request):
   categorie = Categorie.objects.all()

   context = {
      'categorie' : categorie
   }
   return render(request, 'blog/backoffice/categories/categorie_liste.html', context)  


def categorie_create(request):
   form = CategorieForm
   if request.method=='POST':
      form = CategorieForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('categorie_liste')
   context = {
      'form': form
   }
   return render(request, 'blog/backoffice/categories/categorie_create.html', context)


def categorie_update(request, categorie_id):
   categorie = Categorie.objects.get(pk=categorie_id)
   form = CategorieForm(instance = categorie)
   if request.method=='POST':
      form = CategorieForm(instance=categorie, data=request.POST)
      if form.is_valid():
         form.save()
         return redirect('categorie_liste')
   context = {
      'form': form
   }
   return render(request, 'blog/backoffice/categories/categorie_update.html', context)



def categorie_delete(request, categorie_id):
   categorie = Categorie.objects.get(pk= categorie_id)
   categorie.delete()
   return redirect('categorie_liste')


def tags_liste(request):
   tags = Tags.objects.all()
   context = {
      'tags':tags
   }
   return render(request, 'blog/backoffice/tags/tags_liste.html', context)


def tags_create(request):
   form = TagsForm
   if request.method=='POST':
      form = TagsForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('tags_liste')
   context = {
      'form': form
   }
   return render(request, 'blog/backoffice/tags/tags_create.html', context)



def tags_update(request, tag_id):
   tags = Tags.objects.get(pk=tag_id)
   form = TagsForm(instance=tags)
   if request.method=='POST':
      form = TagsForm(instance=tags, data=request.POST)
      if form.is_valid():
         form.save()
         return redirect('tags_liste')
   context = {
      'form': form
   }
   return render(request,'blog/backoffice/tags/tags_update.html', context)


def tags_delete(request, tag_id):
   tags = Tags.objects.get(pk= tag_id)
   tags.delete()
   return redirect('tags_liste')


def article_liste(request):
   article = Article.objects.all()
   context = {
      'article': article
   }
   return render(request, 'blog/backoffice/articles/article_liste.html', context)


def article_create(request):
   form = ArticleForm
   if request.method=='POST':
      form = ArticleForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('article_liste')
   context = {
      'form': form
   }
   return render(request, 'blog/backoffice/articles/article_create.html', context)


def article_update(request, article_id):
   article = Article.objects.get(pk=article_id)
   form = ArticleForm(instance=article)
   if request.method=='POST':
      form = ArticleForm(instance=article, data=request.POST, files=request.FILES)
      if form.is_valid():
         form.save()
         return redirect('article_liste')
   context = {
      'form': form
   }
   return render(request,'blog/backoffice/articles/article_update.html', context)


def article_delete(request, article_id):
   article = Article.objects.get(pk= article_id)
   article.delete()
   return redirect('article_liste')

