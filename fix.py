
# coding: utf-8

# #         Tupro 1 malin
# 

# In[2]:


import csv
import pandas as pd
import numpy as np 
import collections


# In[3]:


def ReadDataTest():
    with open('TestsetTugas1ML.csv') as csv_file:
        kolom = csv.reader(csv_file, delimiter=',')
        next(kolom)
        DataTest = []
        for row in kolom:
            DataTest.append(row)
        return DataTest


# In[4]:


def ReadDataTrain():
    with open('TrainsetTugas1ML.csv') as csv_file:
        kolom = csv.reader(csv_file, delimiter=',')
        next(kolom)
        DataTrain = []
        for row in kolom:
            DataTrain.append(row[1:])
        return DataTrain


# In[5]:


DataTrain = ReadDataTrain()


# In[6]:


DataTrain


# In[7]:


len(DataTrain)


# In[8]:


def pisahdataTrain(DataTrain) :
    KelasA = []
    KelasB = []
    for row in DataTrain :
        if (row[7] == '>50K' ):
            KelasA.append(row)
        else:
            KelasB.append(row)
    return KelasA,KelasB
                


# In[9]:


KelasA,KelasB = pisahdataTrain(DataTrain)


# In[10]:


KelasB


# In[11]:


def hitungjumlah (k):
    data = np.transpose(k)
    category = []
    for i in data[0:7] :
        nilai = collections.Counter(i)
        for a in nilai:
            nilai[a] = nilai[a]/len(k)
        category.append(nilai)
    return category
        


# In[12]:


ok=hitungjumlah(KelasA)


# In[13]:


probkelasA = len(KelasA)/len(DataTrain)


# In[14]:


probkelasA


# In[15]:


probkelasB = len(KelasB)/len(DataTrain)


# In[16]:


probkelasB


# In[17]:


import matplotlib.pyplot as plt
 
labels = ['>50K', '<=50K']
sizes = [probkelasA,probkelasB]
colors = ['lightskyblue', 'lightcoral']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.title ('income')
plt.tight_layout()
plt.show()


# In[18]:


ok


# In[19]:


no = hitungjumlah(KelasB)


# In[20]:


no


# In[21]:


DataTest = ReadDataTest()


# In[22]:


import matplotlib.pyplot as plt


# In[23]:


DataTest


# In[24]:


def hasil_K(DataTest) : 
    Hasil_nilai = []
    for i in DataTest :
        kelas1 = (ok[0][i[1]]*ok[1][i[2]]*ok[2][i[3]]*ok[3][i[4]]*ok[4][i[5]]*ok[5][i[6]]*ok[6][i[7]]) * probkelasA
        kelas2 = (no[0][i[1]]*no[1][i[2]]*no[2][i[3]]*no[3][i[4]]*no[4][i[5]]*no[5][i[6]]*no[6][i[7]]) * probkelasB
        if (kelas1 > kelas2):
            Hasil_nilai.append(['>50'])
        if (kelas1 < kelas2) :
            Hasil_nilai.append(['<=50'])
    return Hasil_nilai


# In[25]:


k = hasil_K(DataTest)


# In[26]:


def SaveResult(k):
    with open('TebakanTugas1ML.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in k:
            writer.writerow(row)


# In[27]:


SaveResult(k)


# In[35]:




