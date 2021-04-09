from django.test import TestCase

class LogPageTest(TestCase):

#	def test_logpage_returns_correct_view(self): #dito
	def test_uses_mainpage_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'logpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data={'AuthorEntry': 'NewAuthor'})
		self.assertIn('NewAuthor', response.content.decode())
		self.assertTemplateUsed(response,'logpage.html')



# Create your tests here.
