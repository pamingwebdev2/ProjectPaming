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
		inputAuthor1 = self.browser.find_element_by_id('Author1')
		inputBook1 = self.browser.find_element_by_id('Book1')
		inputGenre1 = self.browser.find_element_by_id('Genre1')
		inputRemarks1 = self.browser.find_element_by_id('Remarks1')
		btnSave = self.browser.find_element_by_id('btnSave')
		self.assertEqual(inputAuthor1.get_attribute('placeholder'),'Who is the author?')
		self.assertEqual(inputBook1.get_attribute('placeholder'),'What is the title?')
		self.assertEqual(inputGenre1.get_attribute('placeholder'),'What is the genre?')
		self.assertEqual(inputRemarks1.get_attribute('placeholder'),'Remarks')
		time.sleep(2)
		inputAuthor1.send_keys('Mitch Albom')
		time.sleep(2)
		inputBook1.send_keys('Tuesdays With Morrie')
		time.sleep(2)
		inputGenre1.send_keys('Biographical Fiction')
		time.sleep(2)
		inputRemarks1.send_keys('Done')
		time.sleep(2)
		btnSave.click()
		time.sleep(1)
		table = self.browser.find_element_by_id('booklist')
		rows = table.find_element_by_tag_name('tr') 


if __name__ == '__main__':
	unittest.main(warnings='ignore')

		
		





