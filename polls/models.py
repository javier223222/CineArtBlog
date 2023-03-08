from django.db import models

# Create your models here.

class Article(models.Model):
  
 nombre=models.CharField(max_length=90,help_text="nombre del articulo")

 fecha=models.DateField() 
 articulo=models.TextField()

 imagen=models.ImageField()

