from django.contrib import admin
from .models import Users, Conta


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'name', 'email', 'numero', 'habilita',]

    
@admin.register(Conta)
class UserAccount(admin.ModelAdmin):
    list_display = ['id','titular', 'ativa']
        
