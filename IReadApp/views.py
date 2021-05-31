from django.shortcuts import render, redirect
from IReadApp.models import Item, Borrower, BorrTrans

	
def LogPage(request):
	BorrList = Borrower.objects.all()
	return render (request, 'logpage.html',{'Borrower': BorrList})

def ViewList (request, MainID):
	mId = Borrower.objects.get(id=MainID)
	return render (request, 'loglistpage.html', {'mId': mId}) 

def NewList(request): 
	NewBorrower = Borrower.objects.create(Reader=request.POST['NewReader'], Number=request.POST['Number'], Location=request.POST['ReadLoc'], School=request.POST['School'])
	return redirect(f'/IReadApp/{NewBorrower.id}/')

def AddItemLog(request, MainID): #dagdagbo
	mId =Borrower.objects.get(id=MainID)
	Item.objects.create(MainID=mId, binfo=request.POST['CodeEntry'], name=request.POST['Category'], author=request.POST['AuthorEntry'], title=request.POST['BookEntry'])
	return redirect (f'/IReadApp/{mId.id}/')


def DataManip(request):

	#create
	borrower= Borrower(Reader='Rica Paming', Number='09123456789', Location='Dasmarinas', School='TUPC')
	borrower.save()

	#read
	objects = Borrower.objects.all()
	result = 'Output all records in Borrower model : <br>'
	for x in objects:
		res +=x.ID + "<br>"

	#read specifics
	bID = Borrower.objects.get(id="20")
	res += 'Displays One record <br>'
	res += bID.ReadId

	#delete
	res +='<br> Deleting a record <br>'
	bID.delete()

	#update
	borrower= Borrower(Reader='Rica Paming', Number='09987654321', Location='Bacoor', School='PNU')
	borrower.save()
	res += 'Updates entry <br>'

	borrower = Borrower.objects.get(School= 'PNU')
	borrower.School = "PNU"
	borrower.save()
	res = ""

	#filter
	qs = Borrower.objects.filter(Remarks= 'Borrowed')
	res += "Found: %s results<br>" %len(qs)

	#sort
	qs = Borrower.objects.order_by("ReadId")
	for x in qs:
		res +=x.ID +'<br>'