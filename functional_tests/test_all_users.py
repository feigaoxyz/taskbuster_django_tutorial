# -*- coding: utf-8 -*-

from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class HomeNewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        firefox_binary = FirefoxBinary(
            '/opt/homebrew-cask/Caskroom/firefox/37.0.2/Firefox.app/Contents/MacOS/firefox-bin')
        # self.browser = webdriver.Firefox(firefox_binary=firefox_binary)
        self.browser = webdriver.WebDriver(firefox_binary=firefox_binary)
        self.browser.implicitly_wait(3)
        # self.url = 'http://localhost:8000'

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


def main():
    # unittest.main(warnings='ignore')  # avoid a ResourceWarning message
    pass


if __name__ == '__main__':
    main()
