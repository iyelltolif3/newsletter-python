from django.db import models

class newslettersUser(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class newsletters(models.Model):
    name = models.CharField(max_length=250)
    subjet = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    email = models.ManyToManyField(newslettersUser)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name