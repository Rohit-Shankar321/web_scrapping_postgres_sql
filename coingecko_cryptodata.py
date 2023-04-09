#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy
import psycopg2


# In[ ]:


website = 'https://www.coingecko.com/en'


# In[ ]:


source = requests.get(website)


# In[ ]:


source


# In[ ]:


#creating object and html parsing 


# In[ ]:


source = requests.get(website).text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())


# # getting the data

# In[ ]:


table = soup.find('table',{'class':'table-scrollable'})


# # finding rows inside the table

# In[ ]:


table_elements = soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr')


# In[ ]:


len(table_elements)


# # data we have to find inside the tables are                                                #Name                                                                                                                     #Price                                                                                                                          #1h Change                                                                                                                #24h Change                                                                                                              #7day Change                                                                                                           #24h Volume                                                                                                    #Market Cap

# # Name

# In[ ]:


#with short form
table_elements[0].find('a',{'class':'tw-flex tw-flex-auto tw-items-start md:tw-flex-row tw-flex-col'}).get_text().strip().replace('\n','')


# In[ ]:


# I am taking this 
table_elements[0].find('span',{'class':'lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()


# # Price

# In[ ]:


#simple syntax - we can also use this 
table_elements[0].find('td',class_='td-price price text-right').text.strip()


# In[ ]:


table_elements[0].find('td',{'class':'td-price price text-right'}).get_text().strip()


# # 1h Change

# In[ ]:


#will show error
table_elements[0].find('td',{'class':'td-change-99h change1h stat-percent text-right col-market'}).get_text().strip()


# In[ ]:


#-- using change1h only in class
#table_elements[0].find('td',{'class':'change1h'}).get_text().strip()
table_elements[0].find('td',{'class':'td-change1h'}).get_text().strip() #this will also print the data 


# # 24h Change

# In[ ]:


table_elements[0].find('td',{'class':'td-change24h'}).get_text().strip()


# # 7day Change

# In[ ]:


table_elements[0].find('td',{'class':'td-change7d'}).get_text().strip()


# # 24h Volume

# In[ ]:


table_elements[0].find('td',{'class':'td-liquidity_score'}).get_text().strip()


# # Market Cap

# In[ ]:


table_elements[0].find('td',{'class':'td-market_cap'}).get_text().strip()


# # our data is scrapped now , so combining these data and putting into an empty list for single page using exception handling , for loop and empty list creation for each data column

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy


name = []
price= []
change_1h= []
change_24h= []
change_7d = []
volume_24h =[]
market_cap =[]

website = 'https://www.coingecko.com/en'


source = requests.get(website).text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())



for table_elements in soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr'):
    
    try:
        name.append(table_elements.find('span',{'class':'lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        name.append('')
        
        
    try:
        price.append(table_elements.find('td',{'class':'td-price price text-right'}).get_text().strip())
    except:
        price.append('')
        
        
    try:
        change_1h.append(table_elements.find('td',{'class':'td-change1h'}).get_text().strip())
    except:
        change_1h.append('')
        
        
    try:
        change_24h.append(table_elements.find('td',{'class':'td-change24h'}).get_text().strip())
    except:
        change_24h.append('')
        
        
    try:
        change_7d.append(table_elements.find('td',{'class':'td-change7d'}).get_text().strip())
    except:
        change_7d.append('')
        
    
    try:
        volume_24h.append(table_elements.find('td',{'class':'td-liquidity_score'}).get_text().strip())
    except:
        volume_24h.append('')
        
        
    try:
        market_cap.append(table_elements.find('td',{'class':'td-market_cap'}).get_text().strip())
    except:
        market_cap.append('')
        
        
df_crypto =pd.DataFrame({'Crypto Name':name, 'Price':price, '1h Change': change_1h, '24h Change': change_24h, '7d Change': change_7d, '24h Volume': volume_24h, 'Market Capital' : market_cap})
df_crypto        
    


# # now scrapping the data for multiple pages i am doing it for 100

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy


name = []
price= []
change_1h= []
change_24h= []
change_7d = []
volume_24h =[]
market_cap =[]


for i in range(1,100):
    website = 'https://www.coingecko.com/?page= '+str(i)
    source = requests.get(website).text
    soup = BeautifulSoup(source,'lxml')




    for table_elements in soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr'):

        try:
            name.append(table_elements.find('span',{'class':'lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
        except:
            name.append('')


        try:
            price.append(table_elements.find('td',{'class':'td-price price text-right'}).get_text().strip())
        except:
            price.append('')


        try:
            change_1h.append(table_elements.find('td',{'class':'td-change1h'}).get_text().strip())
        except:
            change_1h.append('')


        try:
            change_24h.append(table_elements.find('td',{'class':'td-change24h'}).get_text().strip())
        except:
            change_24h.append('')


        try:
            change_7d.append(table_elements.find('td',{'class':'td-change7d'}).get_text().strip())
        except:
            change_7d.append('')


        try:
            volume_24h.append(table_elements.find('td',{'class':'td-liquidity_score'}).get_text().strip())
        except:
            volume_24h.append('')


        try:
            market_cap.append(table_elements.find('td',{'class':'td-market_cap'}).get_text().strip())
        except:
            market_cap.append('')



#changing into a dataframe            
df_crypto =pd.DataFrame({'Crypto Name':name, 'Price':price, '1h Change': change_1h, '24h Change': change_24h, '7d Change': change_7d, '24h Volume': volume_24h, 'Market Capital' : market_cap})
df_crypto        



# # converting this to csv file

# In[ ]:


df_crypto.to_csv('crypto_data.csv',index = False)


# # Database connectivity postgress , Database name - Cryptocurrency

# In[ ]:


import sqlalchemy
import psycopg2


engine = sqlalchemy.create_engine('postgresql://postgres:12345@localhost:5432/Cryptocurrency')
#postgresql://username:password@host:port/database_name
df_crypto.to_sql('crypto',engine, index = False)


# In[ ]:




