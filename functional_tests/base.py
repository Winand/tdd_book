import sys
import os
from contextlib import contextmanager
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def set_text(self, el, text):
        """
        Clear field and set text until success.
        `send_keys` fails in Chrome if called too early.
        """
        while True:
            el.clear()
            el.send_keys(text)
            if el.get_attribute("value") == text:
                break
            time.sleep(0.5)


@contextmanager
def suppress_stderr():
    "Temporarly suppress writes to stderr"
    class Null:
        write = lambda *args: None
    err, sys.stderr = sys.stderr, Null
    try:
        yield
    finally:
        sys.stderr = err


import shutil
chrome_based_drivers = {
    "chromedriver": webdriver.Chrome, "chromedriver.exe": webdriver.Chrome,
    "msedgedriver": webdriver.Edge, "msedgedriver.exe": webdriver.Edge,
}
driver_name = next((i for i in chrome_based_drivers if shutil.which(i)), "")
if not driver_name:
    raise EnvironmentError("Chrome or Edge driver not found")
driver_type = chrome_based_drivers[driver_name]


class Chrome(driver_type):
    def __init__(self, *args, **kwargs):
        if driver_type == webdriver.Chrome:
            if "options" not in kwargs:
                kwargs["options"] = webdriver.ChromeOptions()
            # Suppress DevTools message on start
            kwargs["options"].add_experimental_option('excludeSwitches',
                                                    ['enable-logging'])
        if not (args or 'executable_path' in kwargs):
            args = (driver_name,)  # if .exe WSL needs extension
        super().__init__(*args, **kwargs)

    def get(self, url):
        super().get(url)
        self.raise_browser_errors()

    def raise_browser_errors(self):
        """
        Check webpage for browser errors.
        See Firefox driver errors in chapter 9.2
        """
        err_status = (
            'ERR_CONNECTION_REFUSED', 'ERR_NAME_NOT_RESOLVED',
            'DNS_PROBE_FINISHED_NXDOMAIN'
        )
        for err in err_status:
            if err in self.page_source:
                msg = "Reached error page: %s (%s)" % (err, self.current_url)
                raise WebDriverException(msg)

    def quit(self):
        "Suppress connection reset errors on quit"
        with suppress_stderr():
            super().quit()
