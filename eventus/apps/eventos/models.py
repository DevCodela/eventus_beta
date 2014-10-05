#encoding:utf-8
from django.db import models
from apps.users.models import User

from django.template.defaultfilters import slugify

class AuditModel(models.Model):
    """
    Clase abstracta que provee campos en común en los modelos
    """
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Categoria(AuditModel):
    """
    Este modelo contiene informacion sobre la categoría.
    """

    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable = False)

    def save(self, *args, **kwargs):
        """
        Esta funcion nos ayuda a guardar el slug de acuerdo al nombre.
        """
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __unicode__(self):
        return self.slug


class Evento(AuditModel):
    """
    Este modelo contiene informacion sobre el evento.
    """

    GRATIS = 'gratis'
    PAGO = 'pago'
    TIPO_PAGO_CHOICE = (
        (GRATIS,'Gratis'),
        (PAGO, 'Pago')
    )

    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False, unique=True)
    resumen = models.TextField(max_length=255)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    lugar = models.TextField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    imagen = models.ImageField(upload_to = 'imagenes')
    tipo_pago = models.CharField(choices=TIPO_PAGO_CHOICE, max_length=6)
    monto = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    visitas = models.IntegerField(blank=True, null=True, default=0)
    organizador = models.ForeignKey(User, blank=True, null=True, related_name="organizador")
    inscritos = models.ManyToManyField(User, through="Tickets")
    
    def save(self, *args, **kwargs):
        """
        Esta funcion nos ayuda a guardar el slug de acuerdo al nombre.
        """
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Evento, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __unicode__(self):
        return self.slug


class Tickets(AuditModel):

    evento = models.ForeignKey(Evento, blank=True, null=True)
    asistente = models.ForeignKey(User, blank=True, null=True, related_name="asistente")

    ha_pagado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __unicode__(self):
        return "[%s] %s - %s " % (self.ha_pagado, self.asistente.username, self.evento.nombre)


class Comentario(AuditModel):

    evento = models.ForeignKey(Evento)
    usuario = models.ForeignKey(User)
    contenido = models.TextField(max_length=200)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __unicode__(self):
        return "%s - %s - %s" % (self.usuario.username, self.evento.nombre, self.contenido)

