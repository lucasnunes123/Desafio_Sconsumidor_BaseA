from django.contrib import admin

from .models import banco_a

@admin.register(banco_a)
class banco_a_admin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "endereco", "list_dividas")


