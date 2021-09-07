# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:48:06 2021

@author: Viral
"""

val='105'
v=val.replace(",",'',2)
va=int(v)
print(va)
if va < 300:
    print('hii')
    
    
"""
            if like1 < 300:
                       button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button')
                       button_like.click()
                       likes += 1
                       sleep(randint(5,10))
            
            
            
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from random import randint    
            #driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a').click()
            #username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/h2/div/div/div/div/span/span').text
            #driver.find_element_by_class_name('css-1dbjc4n r-xoduu5')
            #like1=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[1]').click
            #sleep(randint(5,10))
                #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                 #username=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[2]/div/span').text
            #if username not in prev_user_list:
chromedriver_path ='V:/chromedriver(1)' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)     
driver.get('https://www.instagram.com/abinnoushad/')                
sleep(5)
#username = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a')
            #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').click()
#actions = ActionChains(driver)
#actions.move_to_element(username).perform()
#sleep(randint(15,20))
#u=driver.find_element_by_xpath('/html/body/div/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
follower=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
                 #follower = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div/div[2]/span/span')
#follower = driver.find_element_by_class_name('g47SY').text
f=follower.get_attribute('title')
f1=f.replace(',','',2)
follow = int(f1)
print(follow)
"""
""""" 
                 else:
                       like1=int(driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[2]/div/div/a/span').text)
                       if like1 < 300:
                                 #button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
                         button_like = driver.find_element_by_class_name('_8-yf5 ')
                         like = button_like.get_attribute('aria-label')
                         if like == 'Like':
                               driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                               likes += 1
                               sleep(randint(5,10))

                       
                #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                    comment_box = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[3]/div/form/textarea').click
                    sleep(randint(25,35))
                    driver.find_element_by_link_text('Next').click()
                    sleep(randint(5,10))
        
             

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
                               sleep(randint(15,20))
                               like1=int(driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[2]/div/div/a/span').text)
                               if like1 < 300:
                                 #button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
                                    button_like = driver.find_element_by_class_name('_8-yf5 ')
                                    like = button_like.get_attribute('aria-label')
                                    if like == 'Like':
                                        driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                                        likes += 1
                                        sleep(randint(5,10))
                
                                       
                                #driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                               comment_box = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[3]/div/form/textarea').click
                               sleep(randint(25,35))
                               driver.find_element_by_link_text('Next').click()
                               sleep(randint(5,10))
   
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from random import randint    
chromedriver_path ='V:/chromedriver(1)' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)     
driver.get('https://www.instagram.com/p/CS-DFYugNyH/')                
sleep(5)
like1=driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[2]/div/div/a/span').text
l1=f.replace(',','',2)
l2=int(l1)
sleep(10)
if l2 < 300:
                                 #button_like = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg')
                                    #button_like = driver.find_element_by_class_name('_8-yf5 ')
                                    #like = button_like.get_attribute('aria-label')
                                    #if like == 'Like':
                                        driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                                        likes += 1
                                        sleep(randint(5,10))
"""""