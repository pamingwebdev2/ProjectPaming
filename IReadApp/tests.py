from django.test import TestCase
"""from django.urls import resolve
from IReadApp.views import LogPage
from django.http import HttpRequest
"""
from IReadApp.models import Item #formodelsORM #regression na naman hayup


class LogPageTest(TestCase):

	#def test_logpage_returns_correct_view(self):
		#found = resolve ('/')
		#self.assertEqual(found.func, LogPage)

	def test_uses_logpage_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'logpage.html')

	# def test_saves_only_with_content(self): #def test_only_saves_items_if_necessary(self):
	# 	self.client.get('/')
	# 	self.assertEqual(Item.objects.count(), 0)	

	# def test_saving_POST(self): #def test_save_POST_request(self):
	# 	#response = self.client.post('/', data={'AuthorEntry': 'NewAuthor',})
	# 	response = self.client.post('/', data={'CodeEntry': 'NewCode'})

	# 	#self.assertIn('NewAuthor', response.content.decode())
	# 	#self.assertTemplateUsed(response,'logpage.html')

	# 	self.assertEqual(Item.objects.count(), 1)
	# 	newItem = Item.objects.first()
	# 	self.assertEqual(newItem.binfo, 'NewCode')

		#self.assertEqual(response.status_code, 302) #eto yung bagong insert
		#self.assertEqual(response['location'],'/')

	# def test_if_redirecting_when_POST(self): #def test_redirects_POST_request(self):
	# 	response = self.client.post('/', data={'CodeEntry': 'NewCode',})
	# 	self.assertEqual(response.status_code, 302) #eto yung bagong insert
	# 	#self.assertEqual(response['location'],'/')
	# 	self.assertEqual(response['location'],'/IReadApp/viewlist_url/')

	# def test_display_input(self): #def test_template_displays_list(self):
	# 	Item.objects.create(binfo='Book Code 1')
	# 	Item.objects.create(binfo='Book Code 2')
	# 	response = self.client.get('/')
	# 	self.assertIn('Book Code 1', response.content.decode())
	# 	self.assertIn('Book Code 2', response.content.decode())


	# # 	Item.objects.create(bauth='Author 1')
	# # 	Item.objects.create(bauth='Author 2')

	# # 	Item.objects.create(btitle='Title 1')
	# # 	Item.objects.create(btitle='Title 2')

	# # 	Item.objects.create(bgenre='Genre 1')
	# # 	Item.objects.create(bgenre='Genre 2')

	# 	self.assertIn('Author 1', response.content.decode())
	# 	self.assertIn('Author 2', response.content.decode())

	# 	self.assertIn('Title 1', response.content.decode())
	# 	self.assertIn('Title 2', response.content.decode())

	# 	self.assertIn('Genre 1', response.content.decode())
	# 	self.assertIn('Genre 2', response.content.decode())

#for ORM test

class ORMTest (TestCase):

	def test_and_retrieve(self): #def test_saving_retrieving_list(self):
		infoItem1 = Item()
		#infoAuthor1 = Author()
		infoItem1.binfo = 'Book Code 1'
		# infoItem1.bauth = 'Author 1'
		# infoItem1.btitle = 'Title 1'
		# infoItem1.bgenre = 'Genre 1'
		infoItem1.save()
	#	infoAuthor1.save()
		
		infoItem2 = Item()
		#infoAuthor2 = Author()
		infoItem2.binfo = 'Book Code 2'
		# infoItem2.bauth = 'Author 2'
		# infoItem2.btitle = 'Title 2'
		# infoItem2.bgenre = 'Genre 2'
		infoItem2.save()
		# infoAuthor2.save()
		# infoAuthor2.save()
		
		
		savedInfos = Item.objects.all()
		#savedAuthors = Author.objects.all()
		self.assertEqual(savedInfos.count(), 2)
		#self.assertEqual(savedAuthors.count(), 2)

		savedInfo1 = savedInfos[0]
		savedInfo2 = savedInfos[1]

		# savedAuthor1= savedAuthors[0]
		# savedAuthor2= savedAuthors[1]

		self.assertEqual(savedInfo1.binfo, 'Book Code 1')
		# self.assertEqual(savedInfo1.bauth, 'Author 1')
		# self.assertEqual(savedInfo1.btitle, 'Title 1')
		# self.assertEqual(savedInfo1.bgenre, 'Genre 1')

		self.assertEqual(savedInfo2.binfo, 'Book Code 2')
		# self.assertEqual(savedInfo2.bauth, 'Author 2')	
		# # self.assertEqual(savedInfo2.btitle, 'Title 2')
		# self.assertEqual(savedInfo2.bgenre, 'Genre 2')

class ViewingTest(TestCase):		

	def test_display_all(self): #def test_template_displays_list(self):
		# Item.objects.create(Borrower='Milleth Manzanilla')
		# Item.objects.create(Borrower='JM Tuzon')
		Item.objects.create(binfo='Milleth Manzanilla')
		Item.objects.create(binfo='JM Tuzon')
		response = self.client.get('/IReadApp/viewlist_url/')
		self.assertContains(response,'Milleth Manzanilla')
		self.assertContains(response,'JM Tuzon')

	def test_list_in_loglistpage(self):
		response = self.client.get('/IReadApp/viewlist_url/')
		self.assertTemplateUsed(response, 'loglistpage.html')

class CreateLogListTest(TestCase):

	def test_saving_POST(self): #def test_save_POST_request(self):
		#response = self.client.post('/', data={'AuthorEntry': 'NewAuthor',})
		response = self.client.post('/IReadApp/newlist_url', data={'CodeEntry': 'NewCode'})

		#self.assertIn('NewAuthor', response.content.decode())
		#self.assertTemplateUsed(response,'logpage.html')

		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.binfo, 'NewCode')


	def test_if_redirecting_when_POST(self): #def test_redirects_POST_request(self):
		response = self.client.post('/IReadApp/newlist_url', data={'CodeEntry': 'NewCode',})
		#self.assertEqual(response.status_code, 302) #eto yung bagong insert
		#self.assertEqual(response['location'],'/')
		#self.assertEqual(response['location'],'/IReadApp/viewlist_url/')
		self.assertRedirects(response,'/IReadApp/viewlist_url/')








	'''	
	def test_logpage_returns_correct_view(self):
		response = self.client.get ('/')
		html = response.content.decode('utf8')
		string_html = render_to_string('logpage.html')
		self.assertEqual(html, string_html)
		self.assertTemplateUsed(response,'logpage.html')

	'''

	'''
	def test_logpage_returns_correct_view(self):
		request = HttpRequest()
		response = LogPage(request)
		html = response.content.decode('utf8')
		string_html = render_to_string('logpage.html')
		self.assertEqual(html, string_html)


	def test_logpage_returns_correct_view(self):
		request = HttpRequest()
		response = LogPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title> I-Read Log Book </title>', html)
		self.assertTrue(html.endswith('</html>'))'''


# Create your tests here.
