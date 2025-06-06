from django.contrib import admin
from .models import Cliente, Consumo, Quarto, reserva

admin.site.register(Cliente)
admin.site.register(Consumo)
admin.site.register(Quarto)
admin.site.register(reserva)