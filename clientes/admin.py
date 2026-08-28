

from django.contrib import admin
from .models import Cliente, Projeto, Documento, Vencimento

admin.site.register(Cliente)
admin.site.register(Projeto)
admin.site.register(Documento)
admin.site.register(Vencimento)
