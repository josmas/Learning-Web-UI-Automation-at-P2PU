# Assignment: http://p2pu.org/webcraft/learning-web-ui-automation/document/week-2-interacting-elements-page
from selenium import selenium
import unittest

class TestAdblocker(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "http://addons.allizom.org")
        self.selenium.start()
        self.selenium.open("/")
        self.selenium.window_maximize()

    def tearDown(self):
        self.selenium.stop()

    def test_that_searching_for_adblocker_returns_the_result(self):
        print "executing test"
	self.selenium.type_keys("id=search-q", "adblock")
	self.selenium.click("id=search-button")
	self.selenium.wait_for_page_to_load("30000")
	self.failUnless(self.selenium.get_location().find("adblock") > -1)
	self.assertEqual("Adblock Plus", self.selenium.get_text("xpath=//div/section/div/div/div[2]/h3/a"));

if __name__ == "__main__":
    unittest.main()
