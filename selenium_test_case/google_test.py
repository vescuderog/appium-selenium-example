import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def testSearch(self):
        self.browser.get('http://www.google.com')
        elem = self.browser.find_element_by_name('q')  # Find the search box
        elem.send_keys('selenium', Keys.RETURN)
        self.assertNotIn('No results found', self.browser.page_source)

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
