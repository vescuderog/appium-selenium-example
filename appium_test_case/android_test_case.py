import os
import time
import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AndroidTests(unittest.TestCase):

    def setUp(self):
        # Para esta configuración es necesario tener instalado Android Studio y configurado correctamente el entorno:
        # self.app = os.path.join(os.path.dirname(__file__), '../../../../Downloads/app-debug.apk')
        # print('Script path is : ' + self.apk_path)
        # desired_caps = {
        #     'deviceName': 'Google Nexus 6',
        #     'platformName': 'Android',
        #     'platformVersion': '8.1',
        #     'automationName': 'uiautomator2',
        #     'app': self.app
        # }
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # BrowserStack automate
        desired_caps = {
            'browserName': 'Chrome',
            'device': 'Google Nexus 6',
            'realMobile': 'true',
            'os_version': '6.0'
        }
        self.driver = webdriver.Remote(
            command_executor='http://' + os.getenv('BROWSERSTACK_USER') + ':' + os.getenv(
                'BROWSERSTACK_ACCESS_KEY') + '@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testPageTitle(self):
        self.driver.get('https://www.wikipedia.org/')
        self.assertIn('Wikipedia', self.driver.title)

    def testSearch(self):
        self.driver.get('https://www.wikipedia.org/')
        # search_element = WebDriverWait(self.driver, 30).until(
        #     ec.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia'))
        # )
        # search_element.click()

        search_input = WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((MobileBy.ID, 'searchInput'))
        )
        search_input.send_keys('BrowserStack')
        time.sleep(5)

        search_results = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.assertGreaterEqual(len(search_results), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
