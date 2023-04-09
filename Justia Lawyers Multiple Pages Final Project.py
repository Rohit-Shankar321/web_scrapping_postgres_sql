#!/usr/bin/env python
# coding: utf-8

# # scrapping justia for Multiple pages

# In[10]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy
import psycopg2


# In[11]:


Lnames = []
short_bio =[]
specialization_law=[]
Luniversity=[]
Paddress=[]
Pphone =[]
email_link =[]



for i in range(1,21):
    url = 'https://www.justia.com/lawyers/california/san-francisco?page= '+str(i)
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    
    for results in soup.find_all('div',{'data-vars-action':'OrganicListing'}):
    
    
    
    
        try:
            Lnames.append(results.find('strong',{'class':'lawyer-name'}).get_text().strip())
        except:
            Lnames.append('')



        try:
            short_bio.append(results.find('div',{'class':'lawyer-expl'}).get_text().strip())
        except:
            short_bio.append('')



        try:
            specialization_law.append(results.find('span',{'class':'-practices iconed-line-small'}).get_text().strip())
        except:
            specialization_law.append('')



        try:
            Luniversity.append(results.find('span',{'class':'-law-schools'}).get_text().strip())
        except:
            Luniversity.append('')



        try:
            Paddress.append(results.find('span',{'class':'-address'}).get_text().strip().replace('\t','').replace('\n',''))
        except:
            Paddress.append('')    


        try:
            Pphone.append(results.find('strong',{'class':'-phone'}).get_text().strip())
        except:
            Pphone.append('')



        try:
            email_link.append(results.find('a',{'class':'-email'}).get('href'))
        except:
            email_link.append('')

###################now creating the dataframe to put the value in it


df_lawyers_multiple = pd.DataFrame({'Lawyer_name':Lnames, 'short_bio':short_bio, 'specialization':specialization_law, 'university':Luniversity, 'address':Paddress, 'phone':Pphone, 'email':email_link})
df_lawyers_multiple

    


# In[6]:


#now converting this to csv format

df_lawyers_multiple.to_csv('Justia_Multiple_pages.csv',index = False)


# # Database connectivity postgress

# In[ ]:


#creating sqlalchemy engine
import psycopg2

engine = sqlalchemy.create_engine('postgresql://postgres:12345@localhost:5432/Justia')
#postgresql://username:password@host:port/database_name
df_lawyers_multiple.to_sql('lawyers',engine, index = False)


# In[ ]:




