from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest (unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('I-Read Log Book', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('I-Read Log Book', headerText)
		inputAuthor = self.browser.find_element_by_id('AuthorEntry')
		inputBook = self.browser.find_element_by_id('BookEntry')
		inputGenre = self.browser.find_element_by_id('GenreEntry')
		inputRemarks = self.browser.find_element_by_id('RemarksEntry')
		btnSave = self.browser.find_element_by_id('btnSave')
		self.assertEqual(inputAuthor.get_attribute('placeholder'),'Who is the author?')
		self.assertEqual(inputBook.get_attribute('placeholder'),'What is the title?')
		self.assertEqual(inputGenre.get_attribute('placeholder'),'What is the genre?')
		self.assertEqual(inputRemarks.get_attribute('placeholder'),'Remarks')
		time.sleep(2)
		inputAuthor.send_keys('Mitch Albom')
		time.sleep(2)
		inputBook.send_keys('Tuesdays With Morrie')
		time.sleep(2)
		inputGenre.send_keys('Biographical Fiction')
		time.sleep(2)
		inputRemarks.send_keys('Done')
		time.sleep(2)
		btnSave.click()
		time.sleep(1)
		table = self.browser.find_element_by_id('booklist')
		rows = table.find_element_by_tag_name('tr') 


if __name__ == '__main__':
	unittest.main(warnings='ignore')

		
		





