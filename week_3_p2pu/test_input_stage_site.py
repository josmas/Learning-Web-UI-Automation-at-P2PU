#Assignment: http://p2pu.org/webcraft/learning-web-ui-automation/document/week-3-working-ajax-sites
from selenium import selenium
import unittest
import time

class TestInputStageSite(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "http://input.stage.mozilla.com")
        self.selenium.start()
        self.selenium.open("/")

    def tearDown(self):
        self.selenium.stop()

    def test_that_clicking_on_a_language_checkbox_makes_other_language_choices_disappear(self):

	self.selenium.wait_for_page_to_load("30000")

	# making sure we've more than one language in the list
	self.assertTrue(self.selenium.get_xpath_count("//div[2]/div/div/form/div[4]/ul/div/li") > '1')
	self.selenium.is_element_present("id=loc_ru")
	self.selenium.click("id=loc_ru")

	# the div disappears when only one language is selected so it's perfect for a wait function
	self.wait_for_element_to_disappear("xpath=//div[2]/div/div/form/div[4]/ul/div")
	#only one language should be there now and it is Russian
	self.assertTrue(self.selenium.get_xpath_count("//div[2]/div/div/form/div[4]/ul/li") == '1')
	self.assertTrue(self.selenium.is_element_present("id=loc_ru"))

	self.selenium.click("id=loc_ru")
	# We could wait after deselecting and test again but it is not asked for in the test

    def wait_for_element_to_disappear(self, element):
	count = 0
	while self.selenium.is_element_present(element):
		time.sleep(1)
        	count += 1
        if count == 30:
        	raise Exception(element + ' has not disapeared!')

if __name__ == "__main__":
    unittest.main()
