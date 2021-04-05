from django.test import TestCase

class LogPageTest(TestCase):
	def test_logpage_returns_correct_view(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'logpage.html')


# Create your tests here.
