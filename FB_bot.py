# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:53:22 2021

@author: Viral
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from random import randint


while(True):

#for firefoxdriver
# i = __file__.rfind('/')
# webdriver = webdriver.Firefox(executable_path=__file__[:i + 1] + 'geckodriver.exe')
#for chromedriver
     chromedriver_path ='V:\SEM 7\Personal Intern\Docsup Intern\chromedriver(1)' # Change this to your own chromedriver path!
     driver = webdriver.Chrome(executable_path=chromedriver_path)
     sleep(1)
     driver.get('https://www.facebook.com/')
     sleep(2)

     username = driver.find_element_by_name('email')
     username.send_keys('9265188289') # Change this to your own Instagram username
     password = driver.find_element_by_name('pass')
     password.send_keys('Virus3210') # Change this to your own Instagram password

     button_login = driver.find_element_by_name('login')
     button_login.click()
     sleep(15)

     hashtag_list = ['nature','toys','butterflies'] # Change this to your own tags

     prev_user_list = [] # If it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20190604-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

     new_followed = []
     tag = -1
     followed = 0
     likes = 0
     comments = 0

     for hashtag in hashtag_list:
         tag += 1
         driver.get('https://www.facebook.com/hashtag/'+ hashtag_list[tag] + '/')
         sleep(5)
    
         for x in range(1,2):
            
            #username = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div/div/div')
            uname=driver.find_element_by_class_na('.gmql0nx0.l94mrbxd.p1ri9a11.lzcic4wl.aahdfvyu.hzawbc8m[@id="jsc_c_zy"]')
            username=uname.find_element_by_tag('a')
            actions = ActionChains(driver)
            actions.move_to_element(username).perform()
            sleep(randint(15,20))
           