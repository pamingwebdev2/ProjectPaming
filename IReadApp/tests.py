from django.test import TestCase
"""from django.urls import resolve
from IReadApp.views import LogPage
from django.http import HttpRequest
"""
from IReadApp.models import Item, Borrower#formodelsORM #regression na naman hayup


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

	def test_save_and_retrieve(self): #def test_saving_retrieving_list(self):
		NewBorrower = Borrower()
		NewBorrower.save()
		infoItem1 = Item()
		NewBorrower1 = Borrower ()
		infoItem1.binfo = 'Reader Code 1'
		infoItem1.author ='Author 1'
		infoItem1.title = 'Title 1'
		infoItem1.name = 'Name 1'
		NewBorrower1.Reader = 'Reader 1'
		NewBorrower1.Location = 'Location 1'
		infoItem1.MainID = NewBorrower
		infoItem1.save()
		
		infoItem2 = Item()
		NewBorrower2 = Borrower ()
		infoItem2.MainID = NewBorrower
		infoItem2.binfo = 'Reader Code 2'
		infoItem2.author ='Author 2'
		infoItem2.title = 'Title 2'
		infoItem2.name = 'Name 2'
		NewBorrower2.Reader = 'Reader 2'
		NewBorrower2.Location = 'Location 2'
		infoItem2.save()
		
		savedInfos = Item.objects.all()
		savedBorrowers = Borrower.objects.first()
		self.assertEqual(savedInfos.count(), 2)
		self.assertEqual(savedBorrowers, NewBorrower)
		savedInfo1 = savedInfos[0]
		savedInfo2 = savedInfos[1]
		self.assertEqual(savedInfo1.binfo, 'Reader Code 1')
		self.assertEqual(savedInfo2.binfo, 'Reader Code 2')
		self.assertEqual(savedInfo1.author, 'Author 1')
		self.assertEqual(savedInfo2.author, 'Author 2')
		self.assertEqual(savedInfo1.title, 'Title 1')
		self.assertEqual(savedInfo2.title, 'Title 2')
		self.assertEqual(savedInfo1.name, 'Name 1')
		self.assertEqual(savedInfo2.name, 'Name 2')
		self.assertEqual(NewBorrower1.Reader, 'Reader 1')
		self.assertEqual(NewBorrower2.Reader, 'Reader 2')
		self.assertEqual(NewBorrower1.Location, 'Location 1')
		self.assertEqual(NewBorrower2.Location, 'Location 2')
		self.assertEqual(savedInfo1.MainID, NewBorrower)
		self.assertEqual(savedInfo2.MainID, NewBorrower)


class ViewingTest(TestCase):		

	def test_display_for_each_borrower(self): #def test_template_displays_list(self):
		# Item.objects.create(Borrower='Milleth Manzanilla')
		# Item.objects.create(Borrower='JM Tuzon')
		NewBorrower = Borrower.objects.create()
		Item.objects.create(MainID= NewBorrower, binfo='Manzanilla-IRD-004')
		Item.objects.create(MainID = NewBorrower, binfo='Tuzon-IRD-007')
		response = self.client.get(f'/IReadApp/{NewBorrower.id}/')
		#response = self.client.get('/IReadApp/viewlist_url/')
		self.assertContains(response,'Manzanilla-IRD-004')
		self.assertContains(response,'Tuzon-IRD-007')
		self.assertNotContains(response, 'Dinapo-IRD-111')
		self.assertNotContains(response, 'Teves-IRD-101')

		NewBorrower_2 = Borrower.objects.create()
		Item.objects.create(MainID= NewBorrower_2, binfo='Dinapo-IRD-111')
		Item.objects.create(MainID = NewBorrower_2, binfo='Teves-IRD-101')
		response = self.client.get(f'/IReadApp/{NewBorrower_2.id}/')
		self.assertContains(response, 'Dinapo-IRD-111')
		self.assertContains(response, 'Teves-IRD-101')
		self.assertNotContains(response,'Manzanilla-IRD-004')
		self.assertNotContains(response,'Tuzon-IRD-007')


	def test_list_in_loglistpage(self):
		NewBorrower = Borrower.objects.create()
		response = self.client.get(f'/IReadApp/{NewBorrower.id}/')
		# response = self.client.get('/IReadApp/viewlist_url/')
		self.assertTemplateUsed(response, 'loglistpage.html')


	def test_pass_log_to_loglistpage(self):
		dummyLog1 = Borrower.objects.create()
		dummyLog2 = Borrower.objects.create()
		passLog = Borrower.objects.create()
		response = self.client.get(f'/IReadApp/{passLog.id}/')
		self.assertEqual(response.context['mId'],passLog) 


class CreateLogListTest(TestCase):

	def test_saving_POST(self): #def test_save_POST_request(self):
		#response = self.client.post('/', data={'AuthorEntry': 'NewAuthor',})
		response = self.client.post('/IReadApp/newlist_url', data={'CodeEntry': 'NewCode', 'FriendEntry':'NewFriend', 'AuthorEntry':'NewAuthor', 'BookEntry':'NewTitle'})

		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.binfo, 'NewCode')
		self.assertEqual(newItem.author, 'NewAuthor')
		self.assertEqual(newItem.title, 'NewTitle')
		self.assertEqual(newItem.name, 'NewFriend')


	def test_if_redirecting_when_POST(self): #def test_redirects_POST_request(self):
		response = self.client.post('/IReadApp/newlist_url', data={'CodeEntry': 'NewCode', 'FriendEntry':'NewFriend', 'AuthorEntry':'NewAuthor', 'BookEntry':'NewTitle'})
		#self.assertEqual(response.status_code, 302) #eto yung bagong insert
		#self.assertEqual(response['location'],'/')
		#self.assertEqual(response['location'],'/IReadApp/viewlist_url/')
		newLog = Borrower.objects.first()
		self.assertRedirects(response,f'/IReadApp/{newLog.id}/')

class AddlogTest(TestCase):
	def test_add_another_post_existing(self):
		DummyLog1 = Borrower.objects.create()
		DummyLog2 = Borrower.objects.create()
		existingLog = Borrower.objects.create()
		self.client.post(f'/IReadApp/{existingLog.id}/addItem', data={'CodeEntry': 'New Log for existing', 'FriendEntry': 'New Name Log','AuthorEntry':'New Author Log', 'BookEntry':'New Book Log'})
		self.assertEqual(Item.objects.count(),1)
		newItem =Item.objects.first()
		self.assertEqual(newItem.binfo,'New Log for existing')
		self.assertEqual(newItem.author,'New Author Log')
		self.assertEqual(newItem.title,'New Book Log')
		self.assertEqual(newItem.name,'New Name Log')
		self.assertEqual(newItem.MainID, existingLog)

	def test_redirects_to_log_view(self):
		DummyLog1 = Borrower.objects.create()
		DummyLog2 = Borrower.objects.create()
		DummyLog3 = Borrower.objects.create()
		existingLog = Borrower.objects.create()
		response = self.client.post(f'/IReadApp/{existingLog.id}/addItem', data={'CodeEntry': 'NewCode', 'FriendEntry':'NewFriend', 'AuthorEntry':'New Author Log', 'BookEntry': 'New Book Log'})
		self.assertRedirects(response, f'/IReadApp/{existingLog.id}/')












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
