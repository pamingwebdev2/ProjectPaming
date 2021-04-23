from django.db import models

class Item(models.Model):
	#pass
	binfo = models.TextField(default="")

class Author(models.Model):
	#pass
	bauth = models.TextField(default="")
	btitle = models.TextField(default="")
	bgenre = models.TextField(default="")




# Create your models here.
