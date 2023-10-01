from rest_framework import serializers
from .models import Users, Conta

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id','titular','ativa', 'saldo']
    

class ApiSerializer(serializers.ModelSerializer):

        
    id_account_objects = AccountSerializer(
        many=True,
        source='id_account',
        read_only=True
    )
    
    
    id_account_link = serializers.HyperlinkedRelatedField(
        queryset=Conta.objects.all().order_by('-id'),
        many=True,
        read_only=False,
        view_name='conta_api_detail',
        source='id_account'
    )
    
    class Meta:
        model = Users
        fields = ['cpf', 'name', 'email', 'numero', 'habilita', 'id_account_objects','id_account','id_account_link']
 
    

    

