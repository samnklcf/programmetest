from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(Niveau)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(Commentaire)
admin.site.register(etudiant)
admin.site.register(professeur)

