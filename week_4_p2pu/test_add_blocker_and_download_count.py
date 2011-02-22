# Assingment: Pattern Matching http://p2pu.org/webcraft/learning-web-ui-automation/document/week-4-pattern-matching
from selenium import selenium
import unittest
import re

class TestAdblocker(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "http://addons.allizom.org")
        self.selenium.start()
        self.selenium.open("/")
        self.selenium.window_maximize()

    def tearDown(self):
        self.selenium.stop()

    def test_that_searching_for_adblocker_is_first_result_and_shows_download_number(self):
        print "executing test"
	self.check_first_result_is_adblock()

	self.check_show_downloads_number()

    def check_first_result_is_adblock(self):
	self.selenium.type_keys("id=search-q", "adblock")
	self.selenium.click("id=search-button")
	self.selenium.wait_for_page_to_load("30000")
	self.failUnless(self.selenium.get_location().find("adblock") > -1)
	self.assertEqual("Adblock Plus", self.selenium.get_text("xpath=//div/section/div/div/div[2]/h3/a"));

    def check_show_downloads_number(self):
	# It would be cool to use assertIsNotNone but it's only available in 2.7: bummer!
	self.assertTrue(re.search("^Adblock", self.selenium.get_text("xpath=//div/section/div/div/div[2]")) != None)
	self.assertTrue(re.search("weekly downloads", self.selenium.get_text("xpath=//div/section/div/div/div[2]/div/p[2]")) != None)

if __name__ == "__main__":
    unittest.main()
