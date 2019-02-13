# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:05:59 2019

@author: User
"""

#Импортирую библиотеки необходимые для Scraping

import requests

from bs4 import BeautifulSoup

#код ниже должен мне помочь зайти непосредственно на страницу Reminders в Inbox (в идеале: .post проходит процедуру авторизации, а .get дает нам нужную страницу).
# Однако тут возникла загвоздка. Большинство tutorials показывают, как авторизоваться на сайтах, где username&password находятся на 1 странице
# Google же сначала на 1 странице просит ввести логин, далее перенаправляет на следующую страницу с паролем.
# У меня не получается попасть на страницу Reminders, ни стандартным способом, ни тем, что описан ниже

s = requests.session()
email='username'
s.post('https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https%3A%2F%2Finbox.google.com%2F&followup=https%3A%2F%2Finbox.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin', data=email)
r = s.get('https://accounts.google.com/signin/v2/sl/pwd?passive=1209600&osid=1&continue=https%3A%2F%2Finbox.google.com%2F&followup=https%3A%2F%2Finbox.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward')
#print(r.content)

l = requests.session()
password = 'password'
l.post('https://accounts.google.com/signin/v2/sl/pwd?passive=1209600&osid=1&continue=https%3A%2F%2Finbox.google.com%2F&followup=https%3A%2F%2Finbox.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward', data=password)
k = l.get('https://inbox.google.com/reminders')
#print(k.content)




#print(k.content[:100])

# Parsing web page
soup = BeautifulSoup(k.content, 'html.parser')
print(soup.prettify())

# Find reminders on the page
div = soup.find('div')
#print(div.prettify())
reminders = div.find("div", class_= "tE")

# Далее не могу написать код, так в консоли не отображается нужная мне страница


