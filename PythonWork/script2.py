#!/usr/bin/env python3
import sys
import os
import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
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
    print("Firefox start")
    username = "geonode_GJkxCcMRU0-autoReplace-True"
    password = "99879a56-fed0-467a-af48-df19046284ae"
    GEONODE_DNS = "premium-residential.geonode.com:9003"
    proxy = "premium-residential.geonode.com:9003" # IP:PORT or HOST:PORT

    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--proxy-server=http://%s' % proxy)
    
    # no picture
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #firefox_options.add_experimental_option("prefs", prefs)

    css_click_text_url = 'a[href=\"{0}\"]'.format(click_text_url)
    print( css_click_text_url)
    
    css_click_text_1 = 'a[href=\"{0}\"]'.format(click_text_1)
    print( css_click_text_1)
    
    css_click_text_2 = 'a[href=\"{0}\"]'.format(click_text_2)
    print( css_click_text_2)
    
    css_click_text_3 = 'a[href=\"{0}\"]'.format(click_text_3)
    print( css_click_text_3)
    
    css_click_text_4 = 'a[href=\"{0}\"]'.format(click_text_4)
    print( css_click_text_4)
    
    css_click_text_5 = 'a[href=\"{0}\"]'.format(click_text_5)
    print( css_click_text_5)
    
    browser = webdriver.Firefox(options=firefox_options)
    #browser = webdriver.Firefox(executable_path=r'E:\geckodriver\geckodriver.exe', options=firefox_options)

    
    try:

        browser.get("https://www.google.com/")  
        time.sleep(1)

        search = browser.find_element_by_name( 'q')
        search.send_keys(keyword)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        new_open = 0

        print("Wait start-step0")
        wait = WebDriverWait( browser, 5)
        print("Wait start-step1")
        a_href = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "a")))
        print("Wait start-step2")
        time.sleep(5)
        print("Wait start-step3")
        
		
        webs = browser.find_elements_by_tag_name('a')
        if webs:
	        for web in webs:
	        	print( web)
	        	finalurl = web.get_attribute('href')
	        	print( finalurl)
	        	if click_text_url in finalurl:
	        		print("Found Temp Ads URL")
	        		req = opener.open( finalurl)
	        		finalurl = req.geturl()
	        		print( finalurl)
	        		
	        	if click_text_1 in finalurl or click_text_2 in finalurl or click_text_3 in finalurl or click_text_4 in finalurl or click_text_5 in finalurl: 
	        		print("Found keyword on href url")
	        		web.send_keys(Keys.CONTROL,Keys.ENTER)
	        		new_open = new_open + 1
	        		time.sleep(0.5)
	                        
        if click_text_url:
	        print(css_click_text_url)
	        webs = browser.find_elements_by_css_selector(css_click_text_url)
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
                        
        if click_text_1:
        	print(css_click_text_1)
	        webs = browser.find_elements_by_css_selector(css_click_text_1)
	        print(webs)
	        if webs:
	                for web in webs:
	                        print(web.get_attribute('href'))
	                        web.send_keys(Keys.CONTROL,Keys.ENTER)
	                        new_open = new_open + 1
	                        time.sleep(0.5)

        if click_text_2:
        	print(css_click_text_2)
	        webs = browser.find_elements_by_css_selector(css_click_text_2)
	        print(webs)
	        if webs:
	                for web in webs:
	                        print(web.get_attribute('href'))
	                        web.send_keys(Keys.CONTROL,Keys.ENTER)
	                        new_open = new_open + 1
	                        time.sleep(0.5)

        if click_text_3:
        	print(css_click_text_3)
	        webs = browser.find_elements_by_css_selector(css_click_text_3)
	        print(webs)
	        if webs:
	                for web in webs:
	                        print(web.get_attribute('href'))
	                        web.send_keys(Keys.CONTROL,Keys.ENTER)
	                        new_open = new_open + 1
	                        time.sleep(0.5)

        if click_text_4:
        	print(css_click_text_4)
	        webs = browser.find_elements_by_css_selector(css_click_text_4)
	        print(webs)
	        if webs:
	                for web in webs:
	                        print(web.get_attribute('href'))
	                        web.send_keys(Keys.CONTROL,Keys.ENTER)
	                        new_open = new_open + 1
	                        time.sleep(0.5)

        if click_text_5:
        	print(css_click_text_5)
	        webs = browser.find_elements_by_css_selector(css_click_text_5)
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
        
    except Exception as ex:
        print(ex)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        pass


    time.sleep(2)
    x=x+1
    browser.quit()