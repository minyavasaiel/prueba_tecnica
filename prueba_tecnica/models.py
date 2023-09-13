from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
   
class Center(models.Model):
    name = models.CharField(max_length=100)
    stories = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='centers')

    def __str__(self):
        return self.name