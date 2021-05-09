'''
    A função getbanco_a irá realizar a consulta da base de dados
    

'''
from base_a_app.models import banco_a
from base_a_app.serializers import banco_aSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getbanco_a(request):
    Banco_a = banco_a.objects.all()
    serializer = banco_aSerializer(Banco_a, many=True)
    return Response(serializer.data)








