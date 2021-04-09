from django.shortcuts import render
from django.http import HttpResponse



def LogPage(request):
	#if request.method == 'POST':
	#	return HttpResponse(request.POST['AuthorEntry'])
	#return render(request,"logpage.html")
	return render(request,'logpage.html',{'NewAuthor': request.POST.get('AuthorEntry'), 'NewBook': request.POST.get('BookEntry'), 'NewGenre': request.POST.get('GenreEntry'), 'NewRemarks': request.POST.get('RemarksEntry',''),})




# Create your views here.
