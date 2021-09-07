# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:07:02 2021

@author: Viral
"""

# import web grabbing client and
# HTML parser
from urllib.request import urlopen 
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io


filename = ("V:\SEM 7\Personal Intern\Docsup Intern\Technology_Books.csv")
f = io.open(filename, "w",encoding="utf-8")

headers = "Book title, Pages, Year, Size, Cover URL, Download URL\n"
f.write(headers)
page=1
while page != 12:
      myurl = f'https://www.pdfdrive.com/category/5/p{page}'
      
# grab website and store in variable uclient
      uClient = urlopen(myurl)

# read and close HTML
      page_html = uClient.read()
      uClient.close()

# call BeautifulSoup for parsing
      page_soup = soup(page_html, "html.parser")

# grabs all the products under list tag
      bookshelf = page_soup.findAll(
	  "div", {"class": "col-sm"})
# create csv file of all products
      

      for books in bookshelf:
          book_title = books.h2.text
          book_page = books.findAll("span", {"class": "fi-pagecount"})
          book_year = books.findAll("span", {"class": "fi-year"})
          book_size = books.findAll("span",{"class":"fi-size hidemobile"})
          year = book_year[0].text.strip()
          p = book_page[0].text.strip()
          size = book_size[0].text.strip()
          cv1=books.findAll("img",{"class":"img-zoom"})
          for cover in cv1:
              cu=cover.get('src')
              
          link = books.findAll('a')
          for link1 in link:
              link7=[]
              link2=link1.get('href')
              link3=link2.split('-')
              #link4=[link3[-1].replace('e','d',1) for link5 in link3]
              link4=link3[-1]
              link5=link4.replace('e','d',1)
              link6=link3.remove(link4)
              link7.append(link5)
              link8=link3+link7
              link9="-".join(link8)
              
          url = f'https://www.pdfdrive.com{link9}'
          option = Options()
          option.add_argument('--headless')
          driver = webdriver.Chrome('V:\SEM 7\Personal Intern\Docsup Intern\chromedriver(1)',options=option)
          uClient1 = driver.get(url)
              
              #print(uClient1)
# read and close HTML
              #page_html1 = uClient1.read()
              #uClient1.close()
              
# call BeautifulSoup for parsing
          page_soup1 = soup(driver.page_source, "html.parser")
              #delay(60)
# grabs all the products under list tag
              #sleep(randint(25,30))
          l1 = page_soup1.findAll("a",{"class":"btn"})
          for l2 in l1:
                  
              d = l2.get('href')
                  #download = 'https://pdfdrive.com' + d
                  #d1 = download.split('https://pdfdrive.com',1)[1]
              if d.startswith('http'):
                      d2=d
              else:
                      d2='https://pdfdrive.com' + d
          d3=d2
          print(d3)
          driver.close()
          f.write(book_title + ","+ p +"," + year+","+ size +"," + cu +","+ d3 +"\n")
      page = page + 1
f.close()
# variable to store website link as string

