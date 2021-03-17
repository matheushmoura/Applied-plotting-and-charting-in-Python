
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Sao Paulo, Brazil**, or **Brazil** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Sao Paulo, Brazil** to Ann Arbor, USA. In that case at least one source file must be about ** Sao Paulo, Brazil**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Sao Paulo, Brazil** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[97]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

get_ipython().magic('matplotlib notebook')
datasp = pd.DataFrame(columns=['ano', 'sp', 'pp', 'g', 'c'])
#Reading data downloaded in'seade.gov.br'
#tabelas baixadas do SEADE

for x in range(2002,2019):
    df = pd.read_csv("SeadeFiles/PIB" + str(x) + ".csv")
    datasp= datasp.append({
            'ano':str(x),
            'sp':df.loc[df['MUNICIPIO'] == "São Paulo"]['PIB CAPITA'].values *1000,
            'pp':df.loc[df['MUNICIPIO'] == "Presidente Prudente"]['PIB CAPITA'].values *1000 ,
            'g':df.loc[df['MUNICIPIO'] == "Guarulhos"]['PIB CAPITA'].values *1000,
            'c':df.loc[df['MUNICIPIO'] == "Campinas"]['PIB CAPITA'].values *1000
        }, ignore_index=True)

print(datasp)


# In[98]:

#plotting
ax= plt.gca()

ax.set_facecolor('#F6F9ED')


                        
datasp = datasp.astype(float)
datasp.plot(kind='line',x='ano',y='sp', label='São Paulo (SP)',ax=ax, color='#42124C')
datasp.plot(kind='line',x='ano',y='c', label='Campinas (SP)',ax=ax, color='#FE0472')
datasp.plot(kind='line',x='ano',y='g', label='Guarulhos (SP)',ax=ax, color='#8AFF00')
datasp.plot(kind='line',x='ano',y='pp', label='Presidente Prudente (SP)',ax=ax, color='#C3FF13')


ax.grid(False)
plt.title('Presidente Prudente: Gross Domestic Product (GDP) \n compared to the 3 largest cities in São Paulo (State)', fontsize=14, alpha=0.8)
plt.ylabel('GDP Per Capita in Real(R$)', fontsize=13, alpha=0.8)
plt.xlabel('Year', fontsize=13, alpha=0.8)

plt.tick_params(top='off', right='off',  labelbottom='on')
plt.show()



