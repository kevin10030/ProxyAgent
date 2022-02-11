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
from selenium.webdriver.common.action_chains import ActionChains
from var import x
from var import y
from var import keyword
from var import click_text_url
from var import click_text_1
from var import click_text_2
from var import click_text_3
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
    
    browser = webdriver.Chrome(chrome_options=chrome_options)
    #browser = webdriver.Chrome(executable_path=r'E:\chromedriver_win32\chromedriver.exe',chrome_options=chrome_options)

    try:

        browser.get("https://www.google.com/") 
        time.sleep(1)

        search = browser.find_element_by_name('q')
        search.send_keys(keyword)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        new_open = 0

        print("Found Start")
        webs = browser.find_elements_by_xpath("//a[@class='sVXRqc']")
        if webs:
                for web in webs:
                		print( "Fount Ads Item")
                		print( web)
                		finalurl = web.get_attribute("href")
                		print( finalurl)
                		
                		if click_text_url in finalurl:
                			print("Found Temp Ads URL")
                			req = opener.open( finalurl)
                			finalurl = req.geturl()
                			print( finalurl)
			        	
                		if click_text_1 in finalurl or click_text_2 in finalurl or click_text_3 in finalurl: 
                			print("Found Real Ads URL")
                			ActionChains(browser).key_down(Keys.CONTROL).click(web).key_up(Keys.CONTROL).perform()
                			new_open = new_open + 1
                			time.sleep(0.5)
                		else:
                			print("Nothing found")
                			print( finalurl)
                   

        windows = browser.window_handles
        browser.switch_to.window(windows[-1])

        WebDriverWait(browser,1).until(EC.title_contains(u"YouTube"))
        time.sleep(new_open * 0.5)

        print("ok")

    except Exception as ex:
        print(ex)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    time.sleep(2)
    x=x+1
    browser.quit()