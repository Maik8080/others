"""
Author: Phyo Thiha
Last Modified Date: October 1, 2019
Description: This file stores all common methods used in both fb scripts
(one for creating templates and another for downloading these templates).
"""


import os
from datetime import datetime
import re
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

import account_info


# Time to wait between checking latest downloaded files in 'Download' folder
WAIT_TIME_IN_SEC = 5


def get_chrome_browser_instance():
    folder_that_has_this_code = os.getcwd()
    # Note: Make sure that "chromedrive/chromedriver.exe" shares same PARENT folder as this script
    parent_folder = os.path.dirname(os.path.normpath(folder_that_has_this_code))
    chromedriver_exe_with_path = os.path.join(parent_folder , 'chromedriver', 'chromedriver.exe')
    print("\nInvoking Chrome driver at:", chromedriver_exe_with_path, "\n")
    return webdriver.Chrome(executable_path=chromedriver_exe_with_path)


def log_in(browser):
    print("\nLogging into Business Manager.")
    browser.get(account_info.BASE_URL)
    browser.find_element_by_id('email').clear()
    browser.find_element_by_id('pass').clear()
    browser.find_element_by_id('email').send_keys(account_info.USERNAME)
    browser.find_element_by_id('pass').send_keys(account_info.PASSWORD)
    browser.find_element_by_id('loginbutton').click()


def go_to_ads_reporting(browser):
    browser.get(account_info.ADS_REPORTING_URL)


def get_urls_of_all_accounts(browser, url_prefix):
    accounts_dropdown_xpath = '//div[@role="toolbar"]/*/button'
    click_xpath(browser, accounts_dropdown_xpath)

    # Wait until Account # dropdown elments are present in the DOM
    account_elements_xpath = '//a[@data-testid="big-ad-account-selector-item"]//*//div[contains(text(),"Account #")]'
    WebDriverWait(browser, WAIT_TIME_IN_SEC)\
        .until(ec.presence_of_element_located((By.XPATH, account_elements_xpath)))

    # Generate URLs that will directly bring us to Ads Report page (otherwise, we'll have to navigate using FB's ever changing web UI)
    return [''.join([url_prefix,
                     re.search('.*(act.*)', e.get_attribute('href'), re.I)[1]])
            for e in browser.find_elements_by_xpath('//a[@data-testid="big-ad-account-selector-item"]')]


def get_account_name_and_id(browser):
    accnt_name_id = WebDriverWait(browser, WAIT_TIME_IN_SEC) \
        .until(ec.presence_of_element_located(
        (By.XPATH, '//div[@role="toolbar"]/*/button/*/div[@data-hover="tooltip"]')))
    return re.sub(r'\W', '_', accnt_name_id.text)


def click_xpath(browser, xpath):
    ele = WebDriverWait(browser, WAIT_TIME_IN_SEC)\
        .until(ec.element_to_be_clickable((By.XPATH, xpath)))
    try:
        ele.click()
    except ElementClickInterceptedException:
        # We occasionally and erratically get ElementClickInterceptedException
        # REF: https://stackoverflow.com/a/48667924
        browser.execute_script('arguments[0].click();', ele)
    # We added 5 second break because empirically, we found that it is good
    # to give this much break before taking the next action in FB web UI
    time.sleep(WAIT_TIME_IN_SEC)


def get_report_date_range(browser):
    date_range_xpath = '//span[@data-testid="date_picker"]'
    date_range_dropdown = WebDriverWait(browser, WAIT_TIME_IN_SEC)\
        .until(ec.presence_of_element_located((By.XPATH, date_range_xpath)))
    raw_date_str = [d.strip(',') for d in date_range_dropdown.text.split()]
    to_date = ''.join([raw_date_str[-1],
                       datetime.strptime(raw_date_str[-3], '%b').strftime('%m'),
                       datetime.strptime(raw_date_str[-2], '%d').strftime('%d')])
    from_date = ''.join([raw_date_str[-5],
                         datetime.strptime(raw_date_str[-7], '%b').strftime('%m'),
                         datetime.strptime(raw_date_str[-6], '%d').strftime('%d')])
    return from_date, to_date


def create_output_folder(folder_that_has_this_code, folder_name):
    output_folder = os.path.join(folder_that_has_this_code, folder_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


def enter_str_to_input_field(browser, xpath_to_input_field, str_to_enter):
    # REF: https://stackoverflow.com/a/56875177
    # REF: Selenium expected conditions https://selenium-python.readthedocs.io/waits.html
    input_field = WebDriverWait(browser, WAIT_TIME_IN_SEC)\
        .until(ec.element_to_be_clickable((By.XPATH, xpath_to_input_field)))
    # We can do 'input_field.clear()' but that sometimes doesn't work
    input_field.send_keys(Keys.CONTROL + 'a')
    input_field.send_keys(Keys.DELETE)
    input_field.send_keys(str_to_enter)


def scroll_to_element(browser, element_xpath, scrollbar_xpath):
    element = WebDriverWait(browser, WAIT_TIME_IN_SEC) \
        .until(ec.presence_of_element_located((By.XPATH, element_xpath)))
    scrollbar = WebDriverWait(browser, WAIT_TIME_IN_SEC) \
        .until(ec.presence_of_element_located((By.XPATH, scrollbar_xpath)))

    # Scroll to checkbox element first
    i = 0
    while not element.is_displayed():
        checkbox_location = browser.find_element_by_xpath(element_xpath).location['y'] + i
        js_scroll = ''.join(['arguments[0].scrollTop=', str(checkbox_location), ';'])
        browser.execute_script(js_scroll, scrollbar)
        # We will scroll 200 pixel every time until the checkbox appears in the visible DOM
        i += 200


def scroll_all_the_way_up(browser, scrollbar_xpath):
    # REF: https://stackoverflow.com/q/39471163
    print("Scrolling all the way up the window pane.")
    scrollbar = WebDriverWait(browser, WAIT_TIME_IN_SEC)\
        .until(ec.element_to_be_clickable((By.XPATH, scrollbar_xpath)))
    scrollbar.click()
    ActionChains(browser).send_keys(Keys.HOME).perform()

