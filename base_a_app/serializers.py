'''
    O script serializers.py ira transformar todos os dados na nossa tabela e irá converte-los para o formato JSON
    para uma melhor vizualização

'''

from base_a_app.models import banco_a

from rest_framework import serializers

# A Classe banco_aSerializer, irá pegar quais campos do banco a serão transformados em JSON
class banco_aSerializer(serializers.ModelSerializer):
    class Meta():
        model = banco_a
        fields = ['id', 'cpf', 'nome', 'endereco', 'list_dividas']

