# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:49:19 2021

@author: Viral
"""""

import os
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])


from instabot import Bot

bot=Bot()

bot.login(username='sinchan.014', password='Vir@l3210')

bot.like("cars", "Ferari")
bot.like_by_locations(['224442573/salton-sea/'], amount=10)
bot.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)
bot.follow_by_tags(['gujju', 'junagadh'], amount=5)
bot.follow_by_list(['hardy', 'keenu'], times=1, sleep_delay=600, interact=False)
bot.follow_user_followers(['', 'follower2'], amount=10, randomize=False, interact=True)
bot.follow_likers (['dhingi_patel' , 'dosto.ni.duniya'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
bot.follow_commenters(['elonrmuskk'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)
custom_list = ["darshanravaldz", "thekinjaldave", "dhvanitthakar"]
bot.unfollow_users(amount=10, customList=(True, custom_list, "all"), style="RANDOM", unfollow_after=55*60*60, sleep_delay=600)
bot.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=600)
bot.unfollow_users(amount=40, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=450)



('/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')

'/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button/div')


//html//body//div[1]//section//main//div//div//div[1]//div//form//div//div[3]//button//div