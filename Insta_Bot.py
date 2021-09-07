# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:54:48 2021

@author: Viral
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from random import randint
import time

while(True):

#for firefoxdriver
# i = __file__.rfind('/')
# webdriver = webdriver.Firefox(executable_path=__file__[:i + 1] + 'geckodriver.exe')
#for chromedriver
     chromedriver_path ='V:/chromedriver(1)' # Change this to your own chromedriver path!
     driver = webdriver.Chrome(executable_path=chromedriver_path)
     sleep(1)
     driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
     sleep(2)

     username = driver.find_element_by_name('username')
     username.send_keys('Your Username') # Change this to your own Instagram username
     password = driver.find_element_by_name('password')
     password.send_keys('Your Password') # Change this to your own Instagram password

     button_login = driver.find_element_by_xpath('//html//body//div[1]//section//main//div//div//div[1]//div//form//div//div[3]//button//div')
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
         driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
         sleep(5)
         first_thumbnail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

         first_thumbnail.click()
         sleep(randint(1,2))
    
         for x in range(1,2):
            
            username = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a')
            #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').click()
            actions = ActionChains(driver)
            actions.move_to_element(username).perform()
            sleep(randint(15,20))
            u=driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
            if u not in prev_user_list:
                 try:
                 #follower=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
                 #follower = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div/div[2]/span/span')
                      follower = driver.find_elements_by_class_name("g47SY.lOXF2")[1]
                      f=follower.get_attribute('title')
                      f1=f.replace(',','',2)
                      follow = int(f1)
                      if follow < 20000:
                # If we already follow, do not unfollow
                           if driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow' :
                               driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                               new_followed.append(username)
                               followed += 1
                               sleep(randint(5,10))
                
                               like1=driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[2]/div/div/a/span').text
                               l1=like1.replace(',','',2)
                               l2=int(l1)
                               print(l2)
                               #sleep(10)
                               if l2 < 300:
                                    #button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
                                    #button_like = driver.find_element_by_class_name('_8-yf5 ')
                                    #like = button_like.get_attribute('aria-label')
                                    #if like == 'Like':
                                        driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                                        likes += 1
                                        sleep(randint(5,10))
                
                                       
                                #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                               comment_box = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[3]/div/form/textarea').click
                               sleep(randint(25,35))
                               driver.find_element_by_link_text('Next').click()
                               sleep(randint(5,10))
                           else:
                               like1=driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[2]/div/div/a/span').text
                               l1=like1.replace(',','',2)
                               l2=int(l1)
                               if l2 < 300:
                                 #button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
                                    #button_like = driver.find_element_by_class_name('_8-yf5 ')
                                    #like = button_like.get_attribute('aria-label')
                                    #if like == 'Like':
                                        driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                                        likes += 1
                                        sleep(randint(5,10))
                
                                       
                                #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                               comment_box = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[3]/div/form/textarea').click
                               sleep(randint(25,35))
                               driver.find_element_by_link_text('Next').click()
                               sleep(randint(5,10))
                 except:
                        like1=driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[2]/div/div/a/span').text
                        l1=like1.replace(',','',2)
                        l2=int(l1)
                        if l2 < 300:
                                 #button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
                                    #button_like = driver.find_element_by_class_name('_8-yf5 ')
                                    #like = button_like.get_attribute('aria-label')
                                    #if like == 'Like':
                                        driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                                        likes += 1
                                        sleep(randint(5,10))
                
                                       
                                #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                        comment_box = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[3]/div/form/textarea').click
                        sleep(randint(25,35))
                        driver.find_element_by_link_text('Next').click()
                        sleep(randint(5,10))
    
            else:
                driver.find_element_by_link_text('Next').click()
                sleep(randint(5,10))
    # Some hashtag stops refreshing photos (it may happen sometimes), it continues to the next

     for n in range(0,len(new_followed)):
         prev_user_list.append(new_followed[n])
     print('Liked {} photos.'.format(likes))
     print('Commented {} photos.'.format(comments))
     print('Followed {} new people.'.format(followed))
     driver.close()
     time.sleep(60)