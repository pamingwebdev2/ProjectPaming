from django.test import TestCase
"""from django.urls import resolve
from IReadApp.views import LogPage
from django.http import HttpRequest
"""
from IReadApp.models import Item #formodelsORM

class LogPageTest(TestCase):

	#def test_logpage_returns_correct_view(self):
		#found = resolve ('/')
		#self.assertEqual(found.func, LogPage)

	def test_uses_logpage_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'logpage.html')

	def test_saves_only_with_content(self): #def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)	

	def test_saving_POST(self): #def test_save_POST_request(self):
		#response = self.client.post('/', data={'AuthorEntry': 'NewAuthor',})
		response = self.client.post('/', data={'AuthorEntry': 'NewAuthor'})

		#self.assertIn('NewAuthor', response.content.decode())
		#self.assertTemplateUsed(response,'logpage.html')

		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.binfo, 'NewAuthor')

		#self.assertEqual(response.status_code, 302) #eto yung bagong insert
		#self.assertEqual(response['location'],'/')

	def test_if_redirecting_when_POST(self): #def test_redirects_POST_request(self):
		response = self.client.post('/', data={'AuthorEntry': 'NewAuthor',})
		self.assertEqual(response.status_code, 302) #eto yung bagong insert
		self.assertEqual(response['location'],'/')

	def test_display_input(self): #def test_template_displays_list(self):
		Item.objects.create(binfo='Book Info 1')
		Item.objects.create(binfo='Book Info 2')
		response = self.client.get('/')
		self.assertIn('Book Info 1', response.content.decode())
		self.assertIn('Book Info 2', response.content.decode())


#for ORM test

class ORMTest (TestCase):

	def test_and_retrieve(self): #def test_saving_retrieving_list(self):
		infoItem1 = Item()
		infoItem1.binfo = 'BkInfo one'
		infoItem1.save()
		
		infoItem2 = Item()
		infoItem2.binfo = 'BkInfo two'
		infoItem2.save()
		
		savedInfos = Item.objects.all()
		self.assertEqual(savedInfos.count(), 2)

		savedInfo1 = savedInfos[0]
		savedInfo2 = savedInfos[1]

		self.assertEqual(savedInfo1.binfo, 'BkInfo one')
		self.assertEqual(savedInfo2.binfo, 'BkInfo two')


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
