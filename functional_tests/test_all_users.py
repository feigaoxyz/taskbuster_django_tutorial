# -*- coding: utf-8 -*-

from datetime import date

from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.utils import formats

FIREFOX_URI = '/opt/homebrew-cask/Caskroom/firefox/37.0.2/Firefox.app/Contents/MacOS/firefox-bin'


class HomeNewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        firefox_binary = FirefoxBinary(FIREFOX_URI)
        self.browser = webdriver.WebDriver(firefox_binary=firefox_binary)
        self.browser.implicitly_wait(3)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn('TaskBuster', self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),
                         "rgba(200, 50, 255, 1)")

    def test_home_files(self):
        self.browser.get(self.live_server_url + '/robots.txt')
        self.assertNotIn("Not Found", self.browser.title)

        self.browser.get(self.live_server_url + '/humans.txt')
        self.assertNotIn("Not Found", self.browser.title)

    def test_i18n(self):
        for lang, h1_text in [('en', 'Welcome to TaskBuster!'),
                              ('zh-hans', '欢迎使用 TaskBuster!'),
                              ('ca', "Benvingut a TaskBuster!")
                              ]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name('h1')
            self.assertEqual(h1.text, h1_text)

    def test_l10n(self):
        today = date.today()
        for lang in ['en', 'ca', 'zh-hans']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id('non-local-date')
            self.assertEqual(formats.date_format(today, use_l10n=True), local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

    def test_time_zone(self):
        self.browser.get(self.get_full_url('home'))
        tz = self.browser.find_element_by_id('time-tz').text
        utc = self.browser.find_element_by_id('time-utc').text
        ny = self.browser.find_element_by_id('time-ny').text
        self.assertNotEqual(tz, utc)
        self.assertNotIn(ny, [tz, utc])


class TestGoogleLogin(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.WebDriver(firefox_binary=FirefoxBinary(FIREFOX_URI))
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(expected_conditions.presence_of_element_located(By.ID, element_id))

    def get_button_by_id(self, element_id):
        return self.browser.wait.unitil(expected_conditions.element_to_be_clickable(By.ID, element_id))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_google_login(self):
        self.browser.get(self.get_full_url('home'))
        google_login = self.get_element_by_id('google_login')
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('logout')

        self.assertEqual(google_login.get_attribute('href'), self.live_server_url + '/account/google/login')
        google_login.click()
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('google_login')
        google_logout = self.get_element_by_id('logout')
        google_logout.click()
        google_login = self.get_element_by_id('google_login')


def main():
    # unittest.main(warnings='ignore')  # avoid a ResourceWarning message
    pass


if __name__ == '__main__':
    main()
