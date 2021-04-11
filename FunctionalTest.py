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
		
		inputAuthor1 = self.browser.find_element_by_id('AuthorEntry')
		inputBook1 = self.browser.find_element_by_id('BookEntry')
		inputGenre1 = self.browser.find_element_by_id('GenreEntry')
		inputRemarks1 = self.browser.find_element_by_id('RemarksEntry')
		btnSave = self.browser.find_element_by_id('btnSave')
		
		self.assertEqual(inputAuthor1.get_attribute('placeholder'),'Who is the author?')
		self.assertEqual(inputBook1.get_attribute('placeholder'),'What is the title?')
		self.assertEqual(inputGenre1.get_attribute('placeholder'),'What is the genre?')
		self.assertEqual(inputRemarks1.get_attribute('placeholder'),'Remarks')
		
		time.sleep(2)
		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		time.sleep(1)
		inAuthor.send_keys('Mitch Albom')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('Tuesdays With Morrie')
		time.sleep(1)

		inGenre = self.browser.find_element_by_id('GenreEntry')
		inGenre.click()
		time.sleep(1)
		inGenre.send_keys('Biographical Fiction')
		time.sleep(1)

		inRemarks = self.browser.find_element_by_id('RemarksEntry')
		inRemarks.click()
		time.sleep(1)
		inRemarks.send_keys('Done')
		time.sleep(1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()
		time.sleep(2)

#another input

		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		time.sleep(1)
		inAuthor.send_keys('Deb Caletti')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		time.sleep(1)
		inBook.send_keys('Stay')
		time.sleep(1)

		inGenre = self.browser.find_element_by_id('GenreEntry')
		inGenre.click()
		time.sleep(1)
		inGenre.send_keys('Adult Fiction')
		time.sleep(1)

		inRemarks = self.browser.find_element_by_id('RemarksEntry')
		inRemarks.click()
		time.sleep(1)
		inRemarks.send_keys('Borrowed')
		time.sleep(1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()
		time.sleep(2)

		'''time.sleep(2)
		inputAuthor1.send_keys('Mitch Albom')
		time.sleep(2)
		inputBook1.send_keys('Tuesdays With Morrie')
		time.sleep(2)
		inputGenre1.send_keys('Biographical Fiction')
		time.sleep(2)
		inputRemarks1.send_keys('Done')
		time.sleep(2)
		btnSave.click()
		time.sleep(1)'''

#table updates

		table = self.browser.find_element_by_id('booklist')
		rows = table.find_elements_by_tag_name('tr') 
		self.assertIn('1: Mitch Albom Tuesdays With Morrie Biographical Fiction Done X', [row.text for row in rows])
		self.assertIn('2: Deb Caletti Stay Adult Fiction Borrowed X', [row.text for row in rows])
		#self.assertIn('1: Mitch Albom Tuesdays With Morrie Biographical Fiction Done X', [row.text for row in rows])


if __name__ == '__main__':
	unittest.main(warnings='ignore')

		
		





