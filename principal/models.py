from django.db import models

#nome, email, telefone
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    categoria = models.CharField(max_length=15)
    numero = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.categoria} - {self.numero}"


class reserva(models.Model):
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nome}"


class Consumo(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    reserva =  models.ForeignKey(reserva, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao