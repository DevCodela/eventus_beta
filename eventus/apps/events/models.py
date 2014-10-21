#encoding:utf-8
from django.db import models
from apps.users.models import User

from django.template.defaultfilters import slugify


class AuditModel(models.Model):
    """
    Clase abstracta que provee campos en común en los modelos
    """
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Category(AuditModel):
    """
    Este modelo contiene informacion sobre la categoría.
    """

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable = False)

    def save(self, *args, **kwargs):
        """
        Esta funcion nos ayuda a guardar el slug de acuerdo al nombre.
        """
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.slug


class Event(AuditModel):
    """
    Este modelo contiene informacion sobre el evento.
    """

    FREE = 'gratis'
    PAYMENT = 'pago'
    PAYMENT_TYPE_CHOICE = (
        (FREE,'Gratis'),
        (PAYMENT, 'Pago')
    )

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False, unique=True)
    extract = models.TextField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category)
    place = models.CharField(max_length=255)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    image = models.ImageField(upload_to = 'event_images')
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICE, max_length=6)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    views = models.IntegerField(blank=True, null=True, default=0)
    organizer = models.ForeignKey(User, blank=True, null=True, related_name='organizer')
    enrolled = models.ManyToManyField(User, through="AssistantEnrolled")
    
    def save(self, *args, **kwargs):
        """
        Esta funcion nos ayuda a guardar el slug de acuerdo al nombre.
        """
        if not self.id:
            self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __unicode__(self):
        return self.slug


class AssistantEnrolled(AuditModel):

    event = models.ForeignKey(Event, blank=True, null=True)
    assistant = models.ForeignKey(User, blank=True, null=True, related_name="assistant")

    attended = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Enrolled"
        verbose_name_plural = "Enrolled"

    def __unicode__(self):
        return "[%s] %s - %s " % (self.has_paid, self.assistant.username, self.event.name)


class Comments(AuditModel):

    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)

    content = models.TextField(max_length=200)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __unicode__(self):
        return "%s - %s - %s" % (self.user.username, self.event.name, self.content)

