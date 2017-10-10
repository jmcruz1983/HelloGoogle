"""
Module that implements webdriver engine
"""

import os
import logging
from utils import find_file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Setting logger
log = logging.getLogger(__name__)
fmt = logging.Formatter(datefmt="%H:%M:%S",
                        fmt='%(asctime)s %(levelname)-8s: %(name)s: %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(fmt)
log.addHandler(sh)


class Driver(object):
    chrome = 0
    firefox = 1

class Engine():
    """
    Class that implements webdriver engine
    """

    def __init__(self, *args, **kwargs):
        logLevel = logging.INFO
        log.setLevel(logLevel)
        log.info("args=%s",str(args))
        _,kwargs = args
        log.info("kwargs=%s",str(kwargs))

        self.abs_p = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
        self.timeout = 5

        #logLevel
        if kwargs.has_key('logLevel'):
            logLevel = kwargs['logLevel']
            log.setLevel(logLevel)
        #driver
        if kwargs.has_key('driver'):
            self.driver = kwargs['driver']
        else:
            self.driver = Driver.chrome
        #path
        if kwargs.has_key('path'):
            self.path = kwargs['path']
        else:
            self.path = os.path.join(self.abs_p, "bins", "drivers")

        log.debug("logLevel=%d driver=%d", logLevel, self.driver)

        self.url="http://www.google.com"
        self.input_xpath = '//*[@id="lst-ib"]'
        self.button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
        self.results_xpath = '//*[@id="resultStats"]'
        self.text = "Hello Google"
        self.engine = None
        self.input = None
        self.button = None

        if self.driver == Driver.firefox:
            self.engine = webdriver.Firefox(executable_path=self._find_firefox_bin())
        else:
            self.engine = webdriver.Chrome(executable_path=self._find_chrome_bin())
        log.info("Engine running!")

    def _find_chrome_bin(self):
        return find_file(self.path, "chromedriver").pop(0)

    def _find_firefox_bin(self):
        return find_file(self.path, "geckodriver").pop(0)

    def _open_url(self):
        self.engine.get(self.url)

    def _find_input_element(self):
        self.input = self.engine.find_element_by_xpath(self.input_xpath)

    def _wait_until_page_loaded(self):
        try:
            WebDriverWait(self.engine, self.timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, self.input_xpath)))
            log.debug("_wait_until_page_loaded %s", self.input_xpath)
        except TimeoutException:
            print "Timed out waiting for page to load"
            self._close()

    def _input_text(self):
        self.input.send_keys(self.text)

    def _wait_until_text_loaded(self):
        try:
            WebDriverWait(self.engine, self.timeout).until(
                EC.text_to_be_present_in_element_value(
                    (By.XPATH, self.input_xpath), self.text))
            log.debug("_wait_until_text_loaded %s", self.input_xpath)
        except TimeoutException:
            print "Timed out waiting for text to appear"
            self._close()

    def _find_button_element(self):
        self.button = self.engine.find_element_by_xpath(self.button_xpath)

    def _wait_until_button_clickable(self):
        try:
            WebDriverWait(self.engine, self.timeout).until(
                EC.element_to_be_clickable(
                    (By.XPATH, self.button_xpath)))
            log.debug("_wait_until_button_clickable %s", self.button_xpath)
        except TimeoutException:
            print "Timed out waiting for button to be clickable"
            self._close()

    def _click_button(self):
        if self.button != None:
            self.button.click()

    def _wait_until_results(self):
        try:
            WebDriverWait(self.engine, self.timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, self.results_xpath)))
            log.debug("_wait_until_results %s", self.results_xpath)
        except TimeoutException:
            print "Timed out waiting for results to appear"
            self._close()

    def _close(self):
        log.info("Stopping engine!")
        self.engine.close()

    def run_engine(self):
        self._open_url()
        self._find_input_element()
        self._wait_until_page_loaded()
        self._input_text()
        self._wait_until_text_loaded()
        self._find_button_element()
        self._wait_until_button_clickable()
        self._click_button()
        self._wait_until_results()
        self._close()

def run_engine(*args, **kwargs):
    e = Engine(*args, **kwargs)
    e.run_engine()


if __name__ == '__main__':
    run_engine(logLevel=logging.DEBUG)