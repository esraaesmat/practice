#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime
now = datetime.now()
now


# In[6]:


now.year, now.month, now.day, now.hour


# In[387]:


import pandas as pd
import numpy as np
import datetime as datetime


# In[608]:


df1= pd.read_csv(r"C:\Users\esraa\Documents\ESRAA\archive\covid_19_clean_complete.csv")
df1.drop(['Lat', 'Long'], axis=1, inplace=True)
df1.rename(columns={'Province/State': 'Province', 'Country/Region': 'Country'}, inplace=True)
idx=df1['Province'].isnull()
df1['Province'][idx]='others'


# In[609]:


df1.head()


# In[610]:


df1['Date']=pd.to_datetime(df1['Date'],  errors='ignore')


# In[611]:


df1.dtypes


# In[612]:


df1['year']= df1['Date'].dt.year


# In[613]:


df1


# In[614]:


df1.columns.tolist()


# In[615]:


df1.reindex(columns=['Province','Country','Date','year', 'Confirmed','Deaths','Recovered','Active','WHO Region'])


# In[616]:


df1.groupby(['Country'])['Confirmed','Deaths'].sum()


# In[617]:


len(df1.Country.unique())


# In[647]:


df4= df1.groupby(['Country','Date'])['Confirmed','Deaths'].sum()


# In[648]:


df4


# In[649]:


df5= df4.loc['Afghanistan']
df5.loc['070120': '080120'].sum()


# In[650]:


(df1['Date']>'20-03-2020') & (df1['Date']<'20-04-2020')


# In[651]:


df1[(df1['Date'] > '030120') & (df1['Date'] < '031020')]


# In[652]:


df6= df1.groupby(['Country','Date'])['Confirmed','Deaths'].sum()
df6


# In[653]:


df8= df6.loc[['Egypt']]
df8


# In[681]:


df8.columns.tolist()


# In[682]:


df8.index.names


# In[683]:


df6.loc['Egypt']


# In[689]:


df6.loc[('Egypt','2020-07-23'), :]


# In[693]:


df6.loc[('Egypt', '2020-07-23'): ('Egypt','2020-07-27'), :]


# In[ ]:





# In[ ]:




