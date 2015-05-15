# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        firefox_binary = FirefoxBinary(
            '/opt/homebrew-cask/Caskroom/firefox/37.0.2/Firefox.app/Contents/MacOS/firefox-bin')
        self.browser = webdriver.Firefox(firefox_binary=firefox_binary)
        self.browser.implicitly_wait(3)
        self.url = 'http://localhost:8000'

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get(self.url)
        self.assertIn('Welcome to Django', self.browser.title)


def main():
    unittest.main(warnings='ignore')  # avoid a ResourceWarning message


if __name__ == '__main__':
    main()
