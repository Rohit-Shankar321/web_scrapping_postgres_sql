#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import sqlalchemy


# In[2]:


Product_name =[]
Prices =[]
Description=[]
Stars=[]
Reviews=[]

for i in range(2,100):
    url = 'https://www.flipkart.com/search?q=mobiles+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(i)
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    
    
    for boxes in soup.find_all('div' , class_='_2kHMtA'):
    
        product_elem = boxes.find('div',class_='_4rR01T')
        if product_elem is not None:
            product = product_elem.text
        else:
            product = ''
        Product_name.append(product)
        
        
        
        description_elem = boxes.find('ul', class_='_1xgFaf')
        if description_elem is not None:
            description = description_elem.text
        else:
            description = ''
        Description.append(description)
        
        

        price_elem = boxes.find('div', class_='_30jeq3')
        if price_elem is not None:
            price = price_elem.text
        else:
            price = ''
        Prices.append(price)
        
        
        
        stars_elem = boxes.find('div', class_='_3LWZlK')
        if stars_elem is not None:
            stars = stars_elem.text
        else:
            stars = ''
        Stars.append(stars)
        
        
        
        rating_reviews_elem = boxes.find('span', class_='_2_R_DZ')
        if rating_reviews_elem is not None:
            rating_reviews = rating_reviews_elem.text
        else:
            rating_reviews = ''
        Reviews.append(rating_reviews)
        
        
df = pd.DataFrame({'Product_name':Product_name, 'Cost':Prices, 'Specifications':Description,'Ratings':Stars,'Review':Reviews})
print(df)    
    
#df.to_csv('ekartpostgres.csv')
#print('SuccessfullyCreated')
    


# # --------------------------------------------To csv file-----------------------------

# In[3]:


df.to_csv('ekartpostgres.csv',index = False)
print('SuccessfullyCreated')


# In[6]:


import psycopg2 
#create sqlalchemy engine

engine = sqlalchemy.create_engine('postgresql://postgres:rohit81023@localhost:5432/Ecommerce_Flipkart')
#postgresql://username:password@host:port/database_name
df.to_sql('Flipkart',engine, index = False)






