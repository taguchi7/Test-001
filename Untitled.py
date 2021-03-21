#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas_datareader')


# In[2]:


from pandas datareader import data
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from pandas datareader import data
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


start = '2019-06-01'
end = '2020-06-01'
df = data.datareader('^N225','yahoo',start,end)


# In[6]:


start = '2019-06-01'
end = '2020-06-01'

df = data.datareader('^N225','yahoo',start,end)


# In[7]:


start = '2019-06-01'
end = '2020-06-01'
df = data.Datareader('^N225','yahoo',start,end)


# In[8]:


start = '2019-06-01'
end = '2020-06-01'
df = data.dataReader('^N225','yahoo',start,end)


# In[9]:


start = '2019-06-01'
end = '2020-06-01'
df = data.DataReader('^N225','yahoo',start,end)


# In[10]:


df.head(10)


# In[11]:


df.index


# In[12]:


date=df.index
price=df['Adj Close']


# In[13]:


plt.plot(date.price)


# In[14]:


plt.plot(date,price)


# In[15]:


plt.figure(figsize=(30,10))
plt.plot(date,price)


# In[16]:


plt.plot(date,price,label='Nikkei225')
plt.legend()


# In[17]:


pl.title('N225',color='blue',background='white',size=40,loc='center')
plt.legend()


# In[18]:


plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.legend()


# In[19]:


plt.title('N225',color='blue',backgroundcolor='white',size=40,loc='center')
plt.legend()


# In[20]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.legend()


# In[21]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
plt.title('N225',color='blue',backgroundcolor='white',size=40,loc='center')
plt.legend()


# In[22]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.xlabel('date',color='black',size=30)
plt.ylabel('price',color='black',size=30)
plt.legend()


# In[23]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.xlabel('date',color='black',size=30)
plt.ylabel('price',color='black',size=30)
plt.legend()


# In[24]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.xlabel('date',color='black',size=30)
plt.ylabel('price',color='black',size=30)
plt.legend()


# In[25]:


span01=5
span02=25
span03=50

df['sma01'] = price.rolling(window=span01).mean()
df['sma02'] = price.rolling(window=span02).mean()
df['sma03'] = price.rolling(window=span03).mean()


# In[26]:


df.head(100)


# In[27]:


pd.set_option('display.max_rows',None)
df.head(100)


# In[28]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
df['sma01'] = price.rolling(window=span01).mean()
df['sma02'] = price.rolling(window=span02).mean()
df['sma03'] = price.rolling(window=span03).mean()

plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.xlabel('date',color='black',size=30)
plt.ylabel('price',color='black',size=30)

plt.legend()


# In[29]:


plt.figure(figsize=(30,10))
plt.plot(date,price,label='Nikkei225')
plt.plot(date,df['sma01'],label='sma01')
plt.plot(date,df['sma02'],label='sma02')
plt.plot(date,df['sma03'],label='sma03')

plt.title('N225',color='blue',background='white',size=40,loc='center')
plt.xlabel('date',color='black',size=30)
plt.ylabel('price',color='black',size=30)

plt.legend()


# In[30]:


plt figure{figsize=30,15}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[31]:


plt.figure{figsize=30,15}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[32]:


plt.figure{figsize=30,15}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[34]:


plt.figure{figsize=(30,15)}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[35]:


plt.figure{figsize=(30,15)}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[36]:


plt.figure{figsize=(30,15)}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[37]:


plt.figure[figsize=(30,15)]
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[38]:


plt.figure(figsize=(30,15))
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[39]:


plt.figure(figsize=(30,15))
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt legend()


# In[40]:


plt.figure{figsize=(30,15)}
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt.legend()


# In[41]:


plt.figure(figsize=(30,15))
plt.bar(date.df['Volume'],label='Volume',color='grey')

plt.legend()


# In[42]:


plt.figure(figsize=(30,15))
plt.bar(date,df['Volume'],label='Volume',color='grey')

plt legend()


# In[43]:


plt.figure(figsize=(30,15))
plt.bar(date,df['Volume'],label='Volume',color='grey')

plt.legend()


# In[44]:


df = data.DataReader('6098.JP')


# In[45]:


df = data.DataReader('6098.JP','stooq')


# In[46]:


df.head()


# In[47]:


df = data.DataReader('7269.JP','stooq')


# In[49]:


de.head()


# In[50]:


ff.head()


# In[51]:


df,head()


# In[52]:


df.head()


# In[ ]:




