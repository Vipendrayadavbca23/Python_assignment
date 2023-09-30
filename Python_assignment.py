#!/usr/bin/env python
# coding: utf-8

# In[35]:


'''
Name:Vipendra yadav
class: BCA data science
Roll no.: 62
'''


# In[34]:


Scores=[35,50,20,30,55,75,90,95,66,80]
for i in Scores:
    if i>70:
        print("Distinction")
    elif 60<i<70:
        print("First Class")
    elif 50<i<60:
        print("Second Class")
    elif 35<i<50:
        print("Just Pass")
    else:
        print("Fail")


# In[2]:


Book_price= {"Python":600, "Java": 400, "Web_Tech": 550, "OS": 450, "IT": 700}
for x,y in Book_price.items():
    if y>500:
        print(x)


# In[10]:


aList = [1, 2, 3, 4, 5, 6, 7]
squared_list=[]
for i in range(0,len(aList)):
    squared_list.append(aList[i]**2)
squared_list 


# In[16]:


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in range(0,len(list2)):
    for j in range(0,len(list1)):
        print(list1[j]+list2[i])


# In[22]:


aLsit = [100, 200, 300, 400, 500]
reverse=aLsit[::-1]
reverse


# In[24]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
list1


# In[26]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h", "i", "j"])
list1


# In[29]:


list1=[5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
list1


# In[31]:


Player_game={'Sachin':'Cricket', 'Rahul': 'Cricket', 'Messi': 'Football', 'Federer': 'Tennis', 'Anand': 'Chess'}
for x,y in Player_game.items():
    if y=='Cricket':
        print(x)


# In[33]:


'''List1= [1,2,4,5,10,20,4,5,]
Write a python program to print sum of all the elements in the list
'''
List1= [1,2,4,5,10,20,4,5,]
sum=0
for i in List1:
    sum+=i
sum        

