from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    STATUS = [
        ('rascunho','Rascunho'),
        ('publicado', 'Publicado')
    ]

    title  = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now())
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
    choices=STATUS,
    default='rascunho')

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return f'{self.title} - {self.slug}'