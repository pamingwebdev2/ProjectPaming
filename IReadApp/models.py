from django.db import models

class Borrower(models.Model):
	Location = models.TextField(default="")
	Reader = models.TextField(default="")

class Item(models.Model):
	#pass
	MainID = models.ForeignKey(Borrower, default=None, on_delete=models.CASCADE)
	binfo = models.TextField(default="")
	author = models.TextField(default="")
	title = models.TextField(default="")
	name = models.TextField(default="")

# Create your models here.
