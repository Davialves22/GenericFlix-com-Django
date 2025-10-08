from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario

# so existe porque a gente quier quer no admin apareça o campo personalizado filmes e series vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos', 'series_vistas',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Usuario,UserAdmin)
