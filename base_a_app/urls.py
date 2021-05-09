from base_a_app.views import getbanco_a

from django.urls import path

'''
    arquivo url que referencia o método getbanco_a do script views
    para uso no navegador


'''

urlpatterns = [
    path('', getbanco_a),
]