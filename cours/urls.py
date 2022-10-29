from time import sleep
from django.urls import path
from .views import *
import uuid




urlpatterns = [
    path('', home, name="home"),
    path("theme/<str:slug>", ListeLesson, name="lesson"),
    
    
    # path("app/<int:id>/", applesson, name="applesson"),
    path("test/<str:slug>", seeTheme, name="cours"),
    path('liste/theme/<str:slug>', themedetail, name="themedetail"),
    path('liste/', liste, name="liste"),
    path('liste/categorie/<str:slug>', parCategorie, name="categorie"),
    path("lessonvideo/<str:slug>", lessonvideo, name="lessonvideo"),
    path("lesson/categorie", cat, name="toutcat"),
    path("enregistrement", register, name="register"),
    path("login/", connexion, name="login"),
    path("deconnexion/", deconnexion, name="deconnexion"),
    path(f'etudiant/{uuid.uuid4()}', Etudiant, name="etudiant"),
    
    # re_path(r"^/categorie/(?P<slug>[-\w])*$", voir, name="categorie"),

    
]