''' 
    Utilizando as próprias caracteristca do Django para cria uma base de dados, por Default o Django utiliza
    o sqlite

'''

from django.db import models

# Banco Base A
class banco_a(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=50)
    list_dividas = models.TextField()

    def __str__(self):
        return self.nome


created_at = models.DateTimeField(auto_now_add=True)
uptade_at = models.DateTimeField(auto_now=True)

    


    

