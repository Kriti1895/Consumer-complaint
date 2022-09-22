#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# In[36]:


#- Import data into Python environment 
df=pd.read_csv('D:/simpli learn/Python/Project-3/Comcast_telecom_complaints_data.csv')
df.head()


# In[37]:


#Provide the trend chart for the number of complaints at monthly and daily granularity levels.
df['month']=pd.to_datetime(df['Date_month_year']).dt.month_name()
df['date']=pd.to_datetime(df['Date_month_year']).dt.day

display(df.head(2))

df.groupby(['date'])['Customer Complaint'].count().plot(kind='bar')
plt.show()


df.groupby(['month'])['Customer Complaint'].count().plot(kind='bar',color='green')
plt.show()


# In[38]:


#Provide a table with the frequency of complaint types.
df['Customer Complaint'].value_counts().to_frame().reset_index()


# In[39]:


#Which complaint types are maximum i.e., around internet, network issues, or across any other domains.
df['Customer Complaint'].value_counts().head(5)


# In[40]:


#Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed.
df['Status']=df['Status'].apply(lambda x: 'Open' if((x=='Open') | (x=='Pending')) else 'Closed')
df.head()


# In[41]:


op=df[df['Status']=='Open'].groupby(['State'])['Status'].count().to_frame().reset_index()
cl=df[df['Status']=='Closed'].groupby(['State'])['Status'].count().to_frame().reset_index()
display(op.head(2))
display(cl.head(2))

fig=plt.figure(figsize=(10,10))
plt.barh(cl.State,cl.Status)
plt.barh(op.State,op.Status)

plt.ylabel("State",size=10)
plt.xlabel("Status Count")
plt.legend(["closed","open"])
plt.title("state vs status count")
plt.show()


# In[42]:


op.sort_values('Status',ascending=False).head(3)


# In[43]:


cl.sort_values('Status',ascending=False).head(3)


# In[44]:


#Which state has the maximum complaints
'Georgia'


# In[45]:


#Which state has the highest percentage of unresolved complaints
'Georgia'


# In[46]:


df[df['Status']=='Closed'].value_counts(normalize=True)*100


# In[47]:


#Provide the percentage of complaints resolved till date
#Which were received through the Internet and customer care calls

df[df['Status']=='Closed'][['Received Via']].value_counts(normalize=True)*100


# In[ ]:




