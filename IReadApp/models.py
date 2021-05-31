from django.db import models



class Borrower(models.Model):
	Reader = models.TextField(default="")
	Number = models.TextField(default="")
	Location = models.TextField(default="")
	School = models.TextField(default="")
	class meta:
		db_table="Borrower"


class Item(models.Model):
	binfo = models.TextField(default="") #isbn to
	author = models.TextField(default="")
	title = models.TextField(default="")
	name = models.TextField(default="")
	class meta:
		db_table="Books"


class BorrTrans(models.Model):
	borrId = models.ManyToManyField(Borrower, default=None) #many to many
	bookId = models.ManyToManyField(Item, default=None) #many to many
	DateBorr = models.DateTimeField(auto_now_add=True, null=True)
	DueDate = models.TextField(default="")
	DateRet = models.DateTimeField(auto_now_add=True, null=True)
	Remarks = models.TextField(default="On Process")
	class meta:
		db_table="Transaction"


# class Sponsor(models.Model):
# 	SpoName = models.TextField(default="")
# 	SpoNumber = models.TextField(default="")
# 	SpoLocation = models.TextField(default="")
# 	SpoAffil = models.TextField(default="")
# 	class meta:
# 		db_table="Sponsor"

class DonTrans(models.Model):
	borrId = models.ForeignKey(Borrower, default=None, on_delete=models.CASCADE)
	# DateCon= models.DateField(default="")#kailan nag fill up ng donation form
	Quantity = models.IntegerField(default="") #Ilangbooks
	Mode = models.TextField(default="") #delivery/meetup #1or2
	DateTrans= models.DateTimeField(auto_now_add=True, null=True) #kailanmagaabot 
	Message = models.TextField(default="")
	Categories = models.TextField(default="")
	Status = models.TextField(default="Pending")
	class meta:
		db_table="Donation"

class Penalty (models.Model):
	borrId = models.ForeignKey(Borrower, default=None, on_delete=models.CASCADE)
	Amount =models.IntegerField(default="")
	Mode = models.TextField(default="")
	DatePaid= models.DateTimeField(auto_now_add=True, null=True) #kailanmagaabot 

	class meta:
		db_table="Penalty"

