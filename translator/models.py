from django.db import models

# Create your models here.

class Alphabet(models.Model):
    letter = models.name = models.CharField(max_length=10)
    name = models.name = models.CharField(max_length=100)
    transliteration = models.name = models.CharField(max_length=100)
    equivalent = models.name = models.CharField(max_length=200)
    examples = models.name = models.CharField(max_length=200)

    def __str__(self):
        return self.letter

    
class Number(models.Model): 
    name = models.name = models.CharField(max_length=100)
    number = models.name = models.CharField(max_length=10000)
    transliteration = models.name = models.CharField(max_length=100)

    def __str__(self):
        return self.name