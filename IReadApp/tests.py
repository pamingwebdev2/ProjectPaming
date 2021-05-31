from django.test import TestCase
from IReadApp.models import Item, Borrower


# class WelcPageTest(TestCase):

# 	def test_uses_welcome_template(self):
# 		response = self.client.get ('/')
# 		self.assertTemplateUsed(response,'welcomepage.html')


class LogPageTest(TestCase):

	def test_uses_logpage_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'logpage.html')

class ORMTest (TestCase):

	def test_save_and_retrieve(self): 
		NewBorrower = Borrower()
		NewBorrower.save()
		infoItem1 = Item()
		NewBorrower1 = Borrower ()
		infoItem1.author ='Author 1'
		infoItem1.title = 'Title 1'
		infoItem1.name = 'Name 1'
		infoItem1.MainID = NewBorrower
		infoItem1.save()
		
		infoItem2 = Item()
		NewBorrower2 = Borrower ()
		infoItem2.MainID = NewBorrower
		infoItem2.author ='Author 2'
		infoItem2.title = 'Title 2'
		infoItem2.name = 'Name 2'
		infoItem2.save()
		
		savedInfos = Item.objects.all()
		savedBorrowers = Borrower.objects.first()
		self.assertEqual(savedInfos.count(), 2)
		self.assertEqual(savedBorrowers, NewBorrower)
		savedInfo1 = savedInfos[0]
		savedInfo2 = savedInfos[1]
		self.assertEqual(savedInfo1.author, 'Author 1')
		self.assertEqual(savedInfo2.author, 'Author 2')
		self.assertEqual(savedInfo1.title, 'Title 1')
		self.assertEqual(savedInfo2.title, 'Title 2')
		self.assertEqual(savedInfo1.name, 'Name 1')
		self.assertEqual(savedInfo2.name, 'Name 2')
		self.assertEqual(savedInfo1.MainID, NewBorrower)
		self.assertEqual(savedInfo2.MainID, NewBorrower)


class ViewingTest(TestCase):		

	def test_display_for_each_borrower(self): 
		NewBorrower = Borrower.objects.create()
		Item.objects.create(MainID= NewBorrower, binfo='Manzanilla-IRD-004') #transaction?
		Item.objects.create(MainID = NewBorrower, binfo='Tuzon-IRD-007')
		response = self.client.get(f'/IReadApp/{NewBorrower.id}/')
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
		self.assertTemplateUsed(response, 'loglistpage.html')


	def test_pass_log_to_loglistpage(self):
		dummyLog1 = Borrower.objects.create()
		dummyLog2 = Borrower.objects.create()
		passLog = Borrower.objects.create()
		response = self.client.get(f'/IReadApp/{passLog.id}/')
		self.assertEqual(response.context['mId'],passLog) 


class CreateLogListTest(TestCase): #running

	def test_saving_POST(self): 
		response = self.client.post('/IReadApp/newlist_url', data={'NewReader':'Reader', 'Number':'Number', 'ReadLoc':'Location', 'School':'School'})

		self.assertEqual(Borrower.objects.count(), 1)
		newBorr = Borrower.objects.first()
		self.assertEqual(newBorr.Reader, 'Reader')
		self.assertEqual(newBorr.Number, 'Number')
		self.assertEqual(newBorr.Location, 'Location')
		self.assertEqual(newBorr.School, 'School')


	def test_if_redirecting_when_POST(self):
		response = self.client.post('/IReadApp/newlist_url', data={'NewReader':'Reader', 'Number':'Number', 'ReadLoc':'Location', 'School':'School'})
		newLog = Borrower.objects.first()
		self.assertRedirects(response,f'/IReadApp/{newLog.id}/')

class AddlogTest(TestCase):
	def test_add_another_post_existing(self): #dagdagborrowwing trans
		DummyLog1 = Borrower.objects.create()
		DummyLog2 = Borrower.objects.create()
		existingLog = Borrower.objects.create()
		self.client.post(f'/IReadApp/{existingLog.id}/addItem', data={'Category': 'New Name Log','AuthorEntry':'New Author Log', 'BookEntry':'New Book Log'})
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
		response = self.client.post(f'/IReadApp/{existingLog.id}/addItem', data={'Category':'NewFriend', 'AuthorEntry':'New Author Log', 'BookEntry': 'New Book Log'})
		self.assertRedirects(response, f'/IReadApp/{existingLog.id}/')











