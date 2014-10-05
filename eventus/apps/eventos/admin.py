from django.contrib import admin

from .models import Categoria, Evento, Tickets, Comentario

admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(Tickets)
admin.site.register(Comentario)