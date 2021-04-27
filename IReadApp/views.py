from django.shortcuts import render, redirect
#from django.http import HttpResponse
from IReadApp.models import Item, Borrower

'''LogPage = None'''

def LogPage(request):

	'''pass'''
	#return HttpResponse('<html><title> I-Read Log Book </title><body><h1>I-Read Log Book</h1><form action="" id="form-fields"><input type="text" name="Author" id="Author1" required placeholder="Who is the author?"><input type="text" name="Book" id="Book1" placeholder="What is the title?" required><button type="submit" class="btn-list" id="btnSave"></button></form></body></html>')

	#if request.method == 'POST':
	#	return HttpResponse(request.POST['AuthorEntry'])
	#return render(request,"logpage.html")
	#return render(request,'logpage.html',{'NewAuthor': request.POST.get('AuthorEntry'), 'NewBook': request.POST.get('BookEntry'), 'NewGenre': request.POST.get('GenreEntry'), 'NewRemarks': request.POST.get('RemarksEntry',''),})
	
	#item1 = Item()
	#item1.binfo = request.POST.get('AuthorEntry', '')
	#item1.save()
	#return render(request,'logpage.html', {'NewAuthor':request.POST.get('AuthorEntry',''),})

	#return render (request,'logpage.html',{'NewAuthor': item1.text,})

	#if request.method == 'POST':
	#	newItem = request.POST['AuthorEntry']
	#	Item.objects.create(binfo=newItem)		#dito yung last na gumana
	#else:
	#	newItem = ''
	#return render (request, 'logpage.html',{'NewAuthor':newItem,})

	# if request.method == 'POST':
	# 	Item.objects.create(binfo=request.POST['CodeEntry']) #bauth=request.POST['AuthorEntry'], btitle=request.POST['BookEntry'], bgenre=request.POST['GenreEntry']) #eto yung refactored pero di na nagrun
	# 	#return redirect('/')
	# 	return redirect('/IReadApp/viewlist_url/') #nung tinanggalko to nagerror sila mitch # ihave regresion si sir wala
	#infos = Item.objects.all()
	return render (request, 'logpage.html') #, {'NewCode': infos})
	#return render (request, 'logpage.html')

def ViewList (request, MainID):
	mId = Borrower.objects.get(id=MainID)
	#infos = Item.objects.all()
	#infos = Item.objects.filter(MainID = mId)
	return render (request, 'loglistpage.html', {'mId': mId,'FriendEntry':'NewFriend', 'AuthorEntry':'NewAuthor', 'BookEntry':'NewTitle', 'NewReadID':'Location', 'NewReader':'Reader'})

def NewList(request):
	NewBorrower = Borrower.objects.create()
	Item.objects.create(MainID=NewBorrower, name=request.POST['FriendEntry'], binfo=request.POST['CodeEntry'], author=request.POST['AuthorEntry'], title=request.POST['BookEntry'])
	#return redirect('/IReadApp/viewlist_url/')
	return redirect(f'/IReadApp/{NewBorrower.id}/')

def AddItemLog(request, MainID):
	mId =Borrower.objects.get(id=MainID)
	Item.objects.create(MainID=mId, name=request.POST['FriendEntry'], binfo=request.POST['CodeEntry'], author=request.POST['AuthorEntry'], title=request.POST['BookEntry'])
	return redirect (f'/IReadApp/{mId.id}/')
	#pass
