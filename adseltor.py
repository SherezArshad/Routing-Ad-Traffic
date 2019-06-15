'''
Daniyal Arshad
ESOC 488
Final Project

'''

#================================================
import os
import sys
import subprocess
import unittest, time, re
from subprocess import call
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType #*
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
#================================================

#Define Both ProxyHost and ProxyPort as Strings

#ProxyHost = ""
#Proxyport = ""

#driver = webdriver.Firefox()

#browser = webdriver.Firefox() 

#browser.get(https://www.arizona.edu/)

#asset "arizona" in driver.title


#==========================================



#=========================================================#
if __name__ == "__main__":

#========== Subprocess pckg (call) to get tor to work =========#
#=========== Adding ad nauseam extentesion =============#


    options = Options()
    options.set_headless(True)



geckodriver = '/Users/MyMac/Desktop/finalprojectesoc/geckodriver'

driver = webdriver.Firefox(executable_path=geckodriver, firefox_options=options)

wait = WebDriverWait(driver, timeout=10)

addon1 = '/Users/MyMac/Library/Application Support/Firefox/Profiles/i0nhni3z.default/extensions/adnauseam@rednoise.org.xpi'
driver.install_addon(addon1, temporary=True)




driver.get('http://www.arizona.edu')
driver.get('https://www.dictionary.com')
driver.get('https://www.courant.com')
driver.get('https://www.ign.com')
driver.get('https://www.lingscars.com')
driver.get('https://www.speedtest.net')
driver.get('https://www.forbes.com')
driver.get('https://www.youtube.com')
driver.get('https://www.wikipedia.org')


print(driver.page_source)


subprocess.call(['tor', '-f', '/usr/local/etc/tor/torrc'], shell=False, stdin=None);

driver.quit()




