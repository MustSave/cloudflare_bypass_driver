#!/usr/bin/python3

#selenium libraries
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

class Chrome(uc.Chrome):
    def __init__(self, options=None, user_data_dir=None, driver_executable_path=None, browser_executable_path=None, port=0, enable_cdp_events=False, service_args=None, service_creationflags=None, desired_capabilities=None, advanced_elements=False, service_log_path=None, keep_alive=True, log_level=0, headless=False, version_main=None, patcher_force_close=False, suppress_welcome=True, use_subprocess=True, debug=False, no_sandbox=True, max_retry=3, **kw):
        super().__init__(options, user_data_dir, driver_executable_path, browser_executable_path, port, enable_cdp_events, service_args, service_creationflags, desired_capabilities, advanced_elements, service_log_path, keep_alive, log_level, headless, version_main, patcher_force_close, suppress_welcome, use_subprocess, debug, no_sandbox, **kw)
        self.max_retry = max_retry
        
    def get(self, url, bypass:bool=True):
        super().get(url)

        if bypass:
            try:
                super().find_element(By.CLASS_NAME, "ray-id")
            except NoSuchElementException:
                return
            else:
                self.wait_until_cf_bypass()
        return

    def wait_until_cf_bypass(self):
        for _ in range(self.max_retry):
            try:
                WebDriverWait(self, 5.5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ray-id')))
            except TimeoutException:
                super().refresh()
            else:
                return

        raise TimeoutException()