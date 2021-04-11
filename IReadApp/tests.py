from django.test import TestCase
from IReadApp.models import Item #formodelsORM

class LogPageTest(TestCase):

#	def test_logpage_returns_correct_view(self): #dito
	def test_uses_mainpage_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'logpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data={'AuthorEntry': 'NewAuthor'})
		self.assertIn('NewAuthor', response.content.decode())
		self.assertTemplateUsed(response,'logpage.html')

#for ORM test

class ORMTest (TestCase):

	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()

		txtItem3 = Item()
		txtItem3.text = 'Item three'
		txtItem3.save()

		txtItem4 = Item()
		txtItem4.text = 'Item four'
		txtItem4.save()
		
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 4)

		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		savedItem3 = savedItems[2]
		savedItem4 = savedItems[3]

		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')
		self.assertEqual(savedItem3.text, 'Item three')
		self.assertEqual(savedItem4.text, 'Item four')



# Create your tests here.
