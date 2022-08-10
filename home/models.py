from django.db import models

# Create your models here.

class ArtRequestFormMessage(models.Model):
    '''
    custom art requests messages
    '''
    message_text = models.TextField(null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)


