from django.db import models

class UsersManager(models.Manager):
    def get_user(self, pk):
        query = self.object.filter(cpf=pk)
        return query
    
class Conta(models.Model):
    titular = models.CharField(max_length=50)
    ativa = models.BooleanField(default=True)
    saldo = models.DecimalField(max_digits=30, decimal_places=2, default=0,)
    #agencia = agencia
    #numero = numero
    #saldo = saldo_inicial
    #ativa = False
    #num = num
  
    
class Users(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=55)
    email = models.CharField( max_length=50)
    numero = models.IntegerField()
    habilita = models.BooleanField()
    id_account = models.ManyToManyField(Conta, blank=True, default='')
    
    def __str__(self) -> str:
        return self.cpf
    
    