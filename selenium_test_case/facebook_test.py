import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class FacebookTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.url = 'https://www.facebook.com/'

    def tearDown(self):
        self.browser.close()

    def testPageTitle(self):
        self.browser.get(self.url)
        self.assertIn('Facebook', self.browser.title)

    def testLogin(self):
        self.browser.get(self.url)
        self.browser.find_element_by_name('email').send_keys(os.getenv('FACEBOOK_EMAIL'))
        self.browser.find_element_by_name('pass').send_keys(os.getenv('FACEBOOK_PASS'))
        self.browser.find_elements_by_css_selector("input[type=submit]")[0].click()

        # Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
        wait = WebDriverWait(self.browser, 5)

        # Test that login was successful by checking if the URL in the browser changed
        try:
            wait.until_not(
                lambda browser: browser.current_url == self.url
            )
        except TimeoutException:
            self.fail('Loading timeout expired')

        # Assert that the URL is now the correct post-login page
        self.assertEqual(self.browser.current_url,
                         'https://facebook.com',
                         msg='Successful Login')


if __name__ == '__main__':
    unittest.main(verbosity=2)
