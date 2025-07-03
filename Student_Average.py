#!/usr/bin/env python
# coding: utf-8

# In[23]:


def getdatafromuser():
    D = {}
    while True:
        studentid = input("Enter a student ID :")
        studentmarks = input("Enter a student Marks :")
        morestudent = input('Enter "no" to quit insertion ')
        if studentid in D:
            print(studentid, "is already inserted")
        else:
            D[studentid] = studentmarks.split(",")
        if morestudent.lower() == "no":
            return D   


# In[24]:


studentdata = getdatafromuser()


# In[25]:


def getaverage(D):
    avgmarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
            avgmarks[x] = s/len(L)
    return avgmarks


# In[26]:


avgM = getaverage(studentdata)


# In[27]:


for x in avgM:
    print("Student",x,"got average marks",avgM[x])


# In[ ]:




