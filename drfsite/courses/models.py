from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Contact(models.Model):
    CHOICES = [
        (1,'Phone'),
        (2,'Facebook'),
        (3,'Email'),
    ]
    name = models.IntegerField(choices = CHOICES)
    value = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    logo = models.CharField(max_length=100)
    contacts = models.ForeignKey(Contact, related_name='contact', on_delete=models.CASCADE)
    branches = models.ForeignKey(Branch, related_name='branch', on_delete=models.CASCADE)