# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:29:43 2021

@author: Viral
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
from random import randint
import time

while(True):

#for firefoxdriver
# i = __file__.rfind('/')
# webdriver = webdriver.Firefox(executable_path=__file__[:i + 1] + 'geckodriver.exe')
#for chromedriver
     chromedriver_path ='V:\SEM 7\Personal Intern\Docsup Intern\chromedriver(1)' # Change this to your own chromedriver path!
     driver = webdriver.Chrome(executable_path=chromedriver_path)
     sleep(1)
     driver.get('https://twitter.com/login?redirect_after_login=https%3A%2F%2Fads.twitter.com%2Flogin&hide_message=1')
     sleep(2)

     username = driver.find_element_by_name('session[username_or_email]')
     uk=username.send_keys('Username') # Change this to your own Instagram username
     password = driver.find_element_by_name('session[password]')
     password.send_keys('Password') # Change this to your own Instagram password

     button_login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
     button_login.click()
     sleep(randint(25,30))
     driver.get('https://twitter.com/{uk}')
     #driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li[2]/a').click()
     hashtag_list = ['art','flower','rainbow'] # Change this to your own tags
     prev_user_list = []
     tag = -1
     likes = 0
     comments = 0

     for hashtag in hashtag_list:
         tag += 1
         driver.get('https://twitter.com/hashtag/'+ hashtag_list[tag] + '/')
         sleep(randint(5,10))
         latest = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[1]/a/div')

         latest.click()
         sleep(randint(15,20))
    
         for i in range(1,6):
                # reply button selector
                driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[" + str(i) + "]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div").click()
                sleep(randint(5,10))
                driver.find_element_by_css_selector('.notranslate[data-testid="tweetTextarea_0"]').send_keys('Your Text')
                sleep(randint(10,15))
                driver.find_element_by_css_selector('.css-1dbjc4n[data-testid="tweetButton"]').click()
                sleep(randint(15,20))
                # retweet button selector
                driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[" + str(i) + "]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div").click()
                sleep(randint(5,10))
                tweet=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/a').click()
                sleep(randint(15,20))
                driver.find_element_by_css_selector('.notranslate[data-testid="tweetTextarea_0"]').send_keys('Your Text')
                sleep(randint(10,15))
                driver.find_element_by_css_selector('.css-18t94o4[data-testid="tweetButton"]').click()
                sleep(randint(15,20))
                # like button selector
                driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[" + str(i) + "]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div").click()
                sleep(randint(5,10))
              
        
    # Some hashtag stops refreshing photos (it may happen sometimes), it continues to the next

     driver.close()
     time.sleep(60)
    