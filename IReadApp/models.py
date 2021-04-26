from django.db import models

class Borrower(models.Model):
	pass

class Item(models.Model):
	#pass
	MainID = models.ForeignKey(Borrower, default=None, on_delete=models.CASCADE)
	binfo = models.TextField(default="")

# Create your models here.
