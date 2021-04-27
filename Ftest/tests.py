"""browser = webdriver.Firefox()"""
"""browser.get('http://127.0.0.1:8000')"""
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException


cWait = 3
class PageTest (LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# def tearDown(self):
	#  	self.browser.quit()

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
		self.browser.get('http://localhost:8000')
		#self.browser.get(self.live_server_url)
		self.assertIn('I-Read Log Book', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BORROW a BOOK', headerText)
		
		inputAuthor1 = self.browser.find_element_by_id('AuthorEntry')
		inputBook1 = self.browser.find_element_by_id('BookEntry')
		inputFriend1 = self.browser.find_element_by_id('FriendEntry')
		inputCode1 = self.browser.find_element_by_id ('CodeEntry')
		btnSave = self.browser.find_element_by_id('btnSave')
		
		inputName1 =self.browser.find_element_by_id('NewReader')
		# inputNumber1 = self.browser.find_element_by_id('NumberEntry')
		inputUserID1 = self.browser.find_element_by_id('NewReadID')
		# inputSchool = self.browser.find_element_by_id('SchoolEntry')

		self.assertEqual(inputFriend1.get_attribute('placeholder'),'Name')
		self.assertEqual(inputAuthor1.get_attribute('placeholder'),'Who is the author?')
		self.assertEqual(inputBook1.get_attribute('placeholder'),'What is the title?')
		#self.assertEqual(inputUserID1.get_attribute('placeholder'),'User-IRD-ID')
		self.assertEqual(inputCode1.get_attribute('placeholder'),'User-IRD-ID')
		

		# inNumber = self.browser.find_element_by_id('NumberEntry')
		# inNumber.click()
		# inNumber.send_keys('09066809206')
		
		# time.sleep(.1)
		# inDate = self.browser.find_element_by_id('DateEntry')
		# inDate.click()
		# inputDate1.send_keys('01/25/21')
		# time.sleep(.1)

		time.sleep(.1)
		inBorrower = self.browser.find_element_by_id('NewReadID')
		inBorrower.click()
		inBorrower.send_keys('Dasmarinas')


		time.sleep(.1)
		inName = self.browser.find_element_by_id('NewReader')
		inName.click()
		inName.send_keys('Rica Marie Paming')
		time.sleep(.1)
		
		# time.sleep(.1)
		# inSchool = self.browser.find_element_by_id('SchoolEntry')
		# inSchool.click()
		# inSchool.send_keys('TUPC')
		
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('Tesla-IRD-002')
		time.sleep(.1)

		time.sleep(.1)
		inName = self.browser.find_element_by_id('FriendEntry')
		inName.click()
		inName.send_keys('Nikola Tesla')
		time.sleep(.1)

		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Mitch Albom')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('Tuesdays With Morrie')
		time.sleep(.1)
		
		# inGenre = self.browser.find_element_by_id('GenreEntry')
		# inGenre.click()
		# inGenre.send_keys('Biographical Fiction')
		# time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()

		#self.check_rows_in_booklist('1. Mitch Albom') #(Tuesdays With Morrie Biographical Fiction Done X')
		self.wait_rows_in_booklist('1. Tesla-IRD-002 Nikola Tesla Mitch Albom Tuesdays With Morrie View Return X')
		#self.wait_rows_in_booklist('1. IRD-Book-1 Mitch Albom Tuesdays With Morrie Biographical Fiction View Return X')
#another input

		time.sleep(.1)
		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('Einstein-IRD-009')

		time.sleep(.1)
		inName = self.browser.find_element_by_id('FriendEntry')
		inName.click()
		inName.send_keys('Albert Einstein')
		time.sleep(.1)

		time.sleep(.1)
		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Deb Caletti')
		
		time.sleep(.1)
		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('Stay')
		time.sleep(.1)

		# inGenre = self.browser.find_element_by_id('GenreEntry')
		# inGenre.click()
		# inGenre.send_keys('Adult Fiction')
		# time.sleep(.1)
		

		# inBorrower= self.browser.find_element_by_id('BIDEntry')
		# inBorrower.click()
		# inBorrower.send_keys('Paming-IRD-002')
		# time.sleep(.1)

		

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()

		self.wait_rows_in_booklist("2. Einstein-IRD-009 Albert Einstein Deb Caletti Stay View Return X") #Stay Adult Fiction Borrowed X
		#self.wait_rows_in_booklist("2. IRD-Book-9 Deb Caletti Stay Adult Fiction View Return X")
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
	
	def test_different_url_for_diff_user(self):
		self.browser.get('http://localhost:8000')
		#self.browser.get(self.live_server_url)


		time.sleep(.1)
		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('Currie-IRD-003')
		time.sleep(.1)

		
		inName = self.browser.find_element_by_id('FriendEntry')
		inName.click()
		inName.send_keys('Marie Currie')
		time.sleep(.1)

		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Colleen Hoover')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('November 9')
		time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()
		self.wait_rows_in_booklist("1. Currie-IRD-003 Marie Currie Colleen Hoover November 9 View Return X")
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/IReadApp/.+')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get('http://localhost:8000')
		#self.browser.get(self.live_server_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn("1. Currie-IRD-003 Marie Currie Colleen Hoover November 9 View Return X", pageBody)

		time.sleep(.1)
		inCode = self.browser.find_element_by_id('CodeEntry')
		inCode.click()
		inCode.send_keys('Newton-IRD-005')
		time.sleep(.1)

		inName = self.browser.find_element_by_id('FriendEntry')
		inName.click()
		inName.send_keys('Isaac Newton')
		time.sleep(.1)

		inAuthor = self.browser.find_element_by_id('AuthorEntry')
		inAuthor.click()
		inAuthor.send_keys('Tarryn Fisher')
		time.sleep(1)

		inBook = self.browser.find_element_by_id('BookEntry')
		inBook.click()
		inBook.send_keys('The Opportunist')
		time.sleep(.1)

		btnSave = self.browser.find_element_by_id('btnSave')
		btnSave.click()
		self.wait_rows_in_booklist("1. Newton-IRD-005 Isaac Newton Tarryn Fisher The Opportunist View Return X")

		user2_url =self.browser.current_url
		self.assertRegex(user2_url, '/IReadApp/.+')
		self.assertNotEqual(viewlist_url, user2_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn(" Currie-IRD-003 Marie Currie Colleen Hoover November 9 View Return X", pageBody)
		self.assertIn(" Newton-IRD-005 Isaac Newton Tarryn Fisher The Opportunist View Return X", pageBody)









		"""self.fail('Finish the test')"""
'''if __name__ == '__main__':
	unittest.main(warnings='ignore')'''

		
		





