"""browser = webdriver.Firefox()"""
"""browser.get('http://127.0.0.1:8000')"""
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


cWait = 3
class PageTest (LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	#def tearDown(self):
		#self.browser.quit()

	'''def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('I-Read Log Book', self.browser.title)'''

	def wait_rows_in_booklist(self, row_text):
		#table = self.browser.find_element_by_id('booklist')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn(row_text, [row.text for row in rows])
		
		start_time = time.time ()
		while time.time() - start_time<cWait:
			time.sleep(0.2)
		try:
			table = self.browser.find_element_by_id('booklist')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except (AssertionError, WebDriverException) as f:
			if time.time () - start_time>cWait:
				raise f


	def test_start_a_list_for_one_user(self): #start_list_one_user
		#self.browser.get('http://localhost:8000')
		self.browser.get(self.live_server_url)
		self.assertIn('I-Read Log Book', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BORROW a BOOK', headerText)
		
		inputAuthor1 = self.browser.find_element_by_id('AuthorEntry')
		inputBook1 = self.browser.find_element_by_id('BookEntry')
		inputGenre1 = self.browser.find_element_by_id('GenreEntry')
		inputCode1 = self.browser.find_element_by_id ('CodeEntry')
		btnSave = self.browser.find_element_by_id('btnSave')
		
		inputName1 =self.browser.find_element_by_id('NameEntry')
		inputNumber1 = self.browser.find_element_by_id('NumberEntry')
		# inputDate1 = self.browser.find_element_by_id ('DateEntry')
		inputUserID1 = self.browser.find_element_by_id('BIDEntry')
		inputSchool = self.browser.find_element_by_id('SchoolEntry')

		#self.assertEqual(inputDate1.get_attribute('placeholder'),'month/day/year')
		self.assertEqual(inputAuthor1.get_attribute('placeholder'),'Who is the author?')
		self.assertEqual(inputBook1.get_attribute('placeholder'),'What is the title?')
		self.assertEqual(inputGenre1.get_attribute('placeholder'),'What is the genre?')
		self.assertEqual(inputUserID1.get_attribute('placeholder'),'User-IRD-ID')
		self.assertEqual(inputCode1.get_attribute('placeholder'),'IRD-Book-#')
		
		time.sleep(.1)
		inName = self.browser.find_element_by_id('NameEntry')
		inName.click()
		inName.send_keys('Rica Marie Paming')
		time.sleep(.1)

		inNumber = self.browser.find_element_by_id('NumberEntry')
		inNumber.click()
		inNumber.send_keys('09066809206')
		
		# time.sleep(.1)
		# inDate = self.browser.find_element_by_id('DateEntry')
		# inDate.click()
		# inputDate1.send_keys('01/25/21')
		# time.sleep(.1)

		time.sleep(.1)
		inBorrower = self.browser.find_element_by_id('BIDEntry')
		inBorrower.click()
		inBorrower.send_keys('Paming-IRD-001')
		
		time.sleep(.1)
		inSchool = self.browser.find_element_by_id('SchoolEntry')
		inSchool.click()
		inSchool.send_keys('TUPC')
		
		time.sleep(.1)
		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Mitch Albom')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('Tuesdays With Morrie')
		time.sleep(.1)
		
		inGenre = self.browser.find_element_by_id('GenreEntry')
		inGenre.click()
		inGenre.send_keys('Biographical Fiction')
		time.sleep(.1)

		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('IRD-Book-1')
		time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()

		#self.check_rows_in_booklist('1. Mitch Albom') #(Tuesdays With Morrie Biographical Fiction Done X')
		self.wait_rows_in_booklist('1. IRD-Book-1 View Return X')
#another input

		'''time.sleep(1)
		inName = self.browser.find_element_by_id('NameEntry')
		inName.click()
		inputName1.send_keys('Jasmine May Tuzon')
		time.sleep(1)

		inNumber = self.browser.find_element_by_id('NumberEntry')
		inNumber.click()
		inputNumber1.send_keys('09771439087')
		
		time.sleep(.1)
		inUser = self.browser.find_element_by_id('UserNEntry')
		inUser.click()
		inputUserN1.send_keys('jmtuzon.25@gmail.com')
		time.sleep(.1)

		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inputCode1.send_keys('IRD-Book-7')'''

		time.sleep(.1)
		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Deb Caletti')
		
		time.sleep(.1)
		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('Stay')
		time.sleep(.1)

		inGenre = self.browser.find_element_by_id('GenreEntry')
		inGenre.click()
		inGenre.send_keys('Adult Fiction')
		time.sleep(.1)

		# inBorrower= self.browser.find_element_by_id('BIDEntry')
		# inBorrower.click()
		# inBorrower.send_keys('Paming-IRD-002')
		# time.sleep(.1)

		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('IRD-Book-9')
		time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()

		#self.check_rows_in_booklist("2. Deb Caletti") #Stay Adult Fiction Borrowed X
		self.wait_rows_in_booklist("2. IRD-Book-9 View Return X")
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

		#table = self.browser.find_element_by_id('booklist')
		#rows = table.find_elements_by_tag_name('tr') 
		#self.assertIn('1: Mitch Albom Tuesdays With Morrie Biographical Fiction Done X', [row.text for row in rows])
		#self.assertIn('2: Deb Caletti Stay Adult Fiction Borrowed X', [row.text for row in rows])
		#self.assertIn('1: Mitch Albom Tuesdays With Morrie Biographical Fiction Done X', [row.text for row in rows])
	
	def test_another_user_with_different_url(self): #otheruserdiffurl 
		self.browser.get(self.live_server_url)
		
		time.sleep(.1)
		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Tarryn Fisher')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('The Opportunist')
		time.sleep(.1)
		
		inGenre = self.browser.find_element_by_id('GenreEntry')
		inGenre.click()
		inGenre.send_keys('Contemporary Fiction')
		time.sleep(.1)

		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('IRD-Book-2')
		time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()
		
		self.wait_rows_in_booklist ('1. IRD-Book-2 View Return X')
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/IReadApp/.+')


		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)
		logpagebody = self.browser.find_element_by_tag_name('body').text
		#self.assertNotIn('1. IRD-Book-2 View Return X', logpagebody) #dito ako nagerror kaya di napasok si book 2

		time.sleep(.1)
		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Nicholas Sparks')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('The NoteBook')
		time.sleep(.1)
		
		inGenre = self.browser.find_element_by_id('GenreEntry')
		inGenre.click()
		inGenre.send_keys('Adult Fiction')
		time.sleep(.1)

		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('IRD-Book-10 ')
		time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()

		self.wait_rows_in_booklist ('1. IRD-Book-10 View Return X')
		userbook2_url = self.browser.current_url
		self.assertRegex(userbook2_url, '/IReadApp/.+')
		self.assertNotEqual(viewlist_url, userbook2_url)
		logpagebody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('1. IRD-Book-2 View Return X', logpagebody) #eto kinomment ni sir
		self.assertIn('1. IRD-Book-10 View Return X', logpagebody)














		"""self.fail('Finish the test')"""
'''if __name__ == '__main__':
	unittest.main(warnings='ignore')'''

		
		





