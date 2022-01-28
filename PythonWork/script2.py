#!/usr/bin/env python3
import sys
import os
import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from var import x
from var import y
from var import keyword
from var import click_text_url
from var import click_text_1
from var import click_text_2
from var import click_text_3
from var import click_text_4
from var import click_text_5
import urllib.request as request

proxy_handler = request.ProxyHandler({})
opener = request.build_opener(proxy_handler)

while x<=y :
    print("start")
    username = "geonode_GJkxCcMRU0-autoReplace-True"
    password = "99879a56-fed0-467a-af48-df19046284ae"
    GEONODE_DNS = "premium-residential.geonode.com:9003"
    proxy = "premium-residential.geonode.com:9003" # IP:PORT or HOST:PORT

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://%s' % proxy)

    # no picture
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome(executable_path=r'E:\chromedriver_win32\chromedriver.exe', options=chrome_options)

    try:

        browser.get("https://www.google.com/") 
        time.sleep(1)

        search = browser.find_element_by_name('q')
        search.send_keys(keyword)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        new_open = 0

        webs = browser.find_elements(By.PARTIAL_LINK_TEXT, click_text_url)
        if webs:
                for web in webs:
                        print("Found Temp Ads URL")
                        print(web.get_attribute('href'))
                        req = opener.open(web.get_attribute('href'))
                        finalurl = req.geturl()
                        print("Final URL = ")
                        print(finalurl)
                        if click_text_1 in finalurl or click_text_2 in finalurl or click_text_3 in finalurl or click_text_4 in finalurl or click_text_5 in finalurl: 
                        	print("Found keyword on final url")
                        	web.send_keys(Keys.CONTROL,Keys.ENTER)
                        	new_open = new_open + 1
                        	time.sleep(0.5)
                        
        webs = browser.find_elements(By.PARTIAL_LINK_TEXT, click_text_1)
        print(webs)
        if webs:
                for web in webs:
                        print(web.get_attribute('href'))
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements(By.PARTIAL_LINK_TEXT, click_text_2)
        print(webs)
        if webs:
                for web in webs:
                        print(web.get_attribute('href'))
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements(By.PARTIAL_LINK_TEXT, click_text_3)
        print(webs)
        if webs:
                for web in webs:
                        print(web.get_attribute('href'))
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements(By.PARTIAL_LINK_TEXT, click_text_4)
        print(webs)
        if webs:
                for web in webs:
                        print(web.get_attribute('href'))
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        webs = browser.find_elements(By.PARTIAL_LINK_TEXT, click_text_5)
        print(webs)
        if webs:
                for web in webs:
                        print(web.get_attribute('href'))
                        web.send_keys(Keys.CONTROL,Keys.ENTER)
                        new_open = new_open + 1
                        time.sleep(0.5)

        windows = browser.window_handles
        browser.switch_to.window(windows[-1])

        WebDriverWait(browser,1).until(EC.title_contains(u"YouTube"))
        time.sleep(new_open * 0.5)

        print("ok")
        
    except StaleElementReferenceException as ex:
        print(ex)
        pass
    except NoSuchElementException as ex:
        print(ex)
        pass
    except Exception as ex:
        print(ex)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        pass


    time.sleep(2)
    x=x+1
    browser.quit()