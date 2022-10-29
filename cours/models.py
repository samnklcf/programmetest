
from email.policy import default
from random import choices, random
from turtle import position
from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="imageCat", null=False, blank=True)
    slug = models.SlugField(null=True, blank=True)
    
    class Meta:
        verbose_name = ("Catégorie")
        verbose_name_plural = ("Catégories")
    
        
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)        

class Niveau(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Niveaux')
    
    class Meta:
        verbose_name = ("Niveau")
        verbose_name_plural = ("Niveaux")
    
    
    def __str__(self):
        return self.nom
    


    



        
class Theme(models.Model):
    title = models.CharField(max_length=50)
    mini_description = models.TextField(verbose_name="Minie description", null=False)
    description = RichTextField()
    miniature = models.ImageField(upload_to="miniatures")
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to="videos", verbose_name="Vidéo")
    prix = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE)
    auteur = models.CharField(max_length=50)
    identifiant = models.CharField(null=True, max_length=100, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.identifiant = (uuid.uuid4())
        super().save(*args, **kwargs)
        
 

class Commentaire(models.Model):
    userame = models.CharField(max_length=50)
    message = RichTextField(null=False)
    date = models.DateTimeField(auto_now=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Commentaire")
        verbose_name_plural = ("commentaires")

    def __str__(self):
        return self.userame


class Lesson(models.Model):
    chapitre = models.ForeignKey(Theme, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(null=True, blank=True)
    miniature = models.ImageField(upload_to="miniature")
    video = models.FileField(upload_to="videos")
    document = models.FileField(upload_to="document")
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

class profil(models.Model):
    choix = [
        ("Homme", "Homme"),
        ("Femme", "Femme"),
    ]
    
    choix_prof =  [
        ("Etudiant", "Etudiant"),
        ("Professionnel", "Professionnel"),
        ("Eleve", "Eleve"),
        ("Autodidacte", "Autodidacte"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=80, choices=choix)

    image = models.ImageField(
        blank=True, upload_to="img", null= False, default="default.jpg")
    statut = models.CharField(max_length=80, choices=choix_prof)
    
    date = models.DateTimeField(auto_now=True)
    
   
    
    

class etudiant(profil):
    bio = models.TextField(null = False)
    def __str__(self):
        return self.user.username


class professeur(profil):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="samuel@gmail.com", null=False)
    bio = models.TextField(null = False)
    def __str__(self):
        return self.user.username
    
    
    

