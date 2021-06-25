from django.shortcuts import render, redirect
from IReadApp.models import Item, Borrower, BorrTrans, DonTrans, Penalty

#---------------------------------------------------- borrow
	
def LogPage(request): #OK
	BorrList = Borrower.objects.all()
	return render (request, 'logpage.html',{'Borrower': BorrList})

def ViewList (request, MainID): #OK
	Books = Item.objects.all()
	Transact = BorrTrans.objects.all()
	mId = Borrower.objects.get(id=MainID)
	return render (request, 'loglistpage.html', {'mId': mId, 'Item':Books, 'BorrTrans':Transact}) #same with donate page iba lang render html

def NewList(request):  #OK
	NewBorrower = Borrower.objects.create(Reader=request.POST['NewReader'], Number=request.POST['Number'], Location=request.POST['ReadLoc'], School=request.POST['School'])
	return redirect(f'/IReadApp/{NewBorrower.id}/')

def AddItemLog(request, borrId): #for the many to many NOT OK
	mId= Borrower.objects.get(id=borrId)
	btransact = BorrTrans(DateBorr=request.POST['BorrDate'], DueDate=request.POST['DueDate'], DateRet=request.POST['DateRet'], Remarks=request.POST['DateRem'], PenEstimate=request.POST['Penalty'])
	btransact.save()
	return redirect (f'/IReadApp/{mId.id}/')

#--------------------------------------------------------donation

def DonatePage(request, MainID):#OK
	mId = Borrower.objects.get(id=MainID)
	return render (request, 'donationpage.html', {'mId':mId}) #view and additemlog and self #old urls

def AddDonate(request, borrId): #OK
	#pass
	mId =Borrower.objects.get(id=borrId)
	DonTrans.objects.create(borrId=mId, Quantity=request.POST['Quantity'], Categories=request.POST['Categories'] ,Mode=request.POST['key'], Channel=request.POST['cour'], DateTrans=request.POST['DateTrans'], Message=request.POST['Message'], Status=request.POST['DonSts'])
	return redirect (f'/IReadApp/{mId.id}/donatepage/')

def UpdateDon(request, id):
	dontrans= DonTrans.objects.get(id=id) #OK
	content = {'dontrans':dontrans}
	return render (request, 'donatepagedit.html', content) 

def StatusChange (request,id):
	dontrans= DonTrans.objects.get(id=id)
	dontrans.Quantity=request.POST['Quantity']
	dontrans.Categories=request.POST['Categories'] 
	dontrans.Mode=request.POST['key']
	dontrans.Channel=request.POST['cour']
	dontrans.DateTrans=request.POST['DateTrans']
	dontrans.Message=request.POST['Message']
	dontrans.Status=request.POST['DonSts']
	dontrans.save()
	return redirect('logpage') #sira anf redirection idk y pero nasesave

def DeleteDon (request, id): #OK
	dontrans = DonTrans.objects.get(id=id)
	dontrans.delete()
	return redirect('logpage') #sira anf redirection idk y pero nasesave

#---------------------------------------------------------- booklist

def BookList(request): #OK
	BookList= Item.objects.all()
	return render (request, 'booklist.html', {'Item':BookList}) 

def AddBookList(request): #OK
	#pass
	Item.objects.create(binfo=request.POST['CodeEntry'], name=request.POST['Category'], author=request.POST['AuthorEntry'], title=request.POST['BookEntry'])
	return redirect (f'/IReadApp/booklistpage/')

def UpdateBook(request, id):
	item= Item.objects.get(id=id) #OK
	content = {'item':item}
	return render (request, 'booklistedit.html', content)

def BookChange (request, id): #OK
	item= Item.objects.get(id=id)
	item.binfo= request.POST['CodeEntry']
	item.name = request.POST['Category']
	item.author = request.POST['AuthorEntry']
	item.title = request.POST['BookEntry']
	item.save()
	return redirect(f'/IReadApp/booklistpage/')

def DeleteBook (request, id): #OK
	item = Item.objects.get(id=id)
	item.delete()
	return redirect(f'/IReadApp/booklistpage/')

#-------------------------------------------------------- status

def BookingPage(request,MainID): #OK
	Transact = BorrTrans.objects.all()
	mId = Borrower.objects.get(id=MainID)
	return render (request, 'penalty-page.html',{'mId':mId, 'BorrTrans':Transact},) #view and add itemlog and self #old urls

def AddBooking(request, borrId): #OK
	#pass
	mId = Borrower.objects.get(id=borrId)
	Penalty.objects.create(borrId=mId, Amount=request.POST['Amount'], Mode=request.POST['PMode'], Details=request.POST['details'], DatePaid=request.POST['DPaid'], Checking=request.POST['PaySts'])
	return redirect (f'/IReadApp/{mId.id}/bookingpage/')

def BorrPage(request): #for task 6
 	return render (request, 'loglistpage.html') 

#--------------------------------------------------------

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