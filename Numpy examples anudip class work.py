#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


arr = np.array([10,2,3,4,5,6,20,45])
#Extract elements greater than 5
extracted_elements = np.extract(arr > 5, arr)
print("Elements greater than 3:", extracted_elements)


# In[13]:


arr = np.array([1,2,3,4,5,6,56,23])

#Split the array into two equal sized sub_array
sub_arrays = np.split(arr,4)

print(type(sub_arrays))

#Print the sub_arrays
for i in sub_arrays:
    print(i)


# In[14]:


arr = np.array([3,1,2,4,5])
#Sort the array in the ascending order(create a new sorted array)
sorted_arr = np.sort(arr)

#Print the sorted array
print("Sorted array (ascending):", sorted_arr)

#Sorted array in the desceding order
sorted_arr_desc = np.sort(arr)[::-1]

#Print the sorted array in the descending order 
print("Sorted array (descending):", sorted_arr_desc)


# In[15]:


arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

extract_odd = arr1[arr1 % 2 != 0]
print("Odd numbers from arr1:",extract_odd)


# In[17]:


arr2 = np.array([11,12,13,14,15,16,17,18,19,20])
extract_elements = np.extract(arr2 > 10, arr2)
print("The elements which are greater than 10:", extract_elements)


# In[18]:


arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15,16,17,18,19,20])

conc_array = np.concatenate((arr1,arr2))
print("Concatenated array:", conc_array)


# In[21]:


arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15,16,17,18,19,20])

add_array = (arr1 + arr2)
print("Addition of two arrays:",add_array)


# In[22]:


arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15,16,17,18,19,20])

sub_array = arr2 - arr1
print("Subtraction of two arrays:", sub_array)


# In[23]:


arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15,16,17,18,19,20])

mult_array = arr1 * arr2
print("Multiplication of two arrays", mult_array)


# In[24]:


arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15,16,17,18,19,20])
 
div_array = arr1 % arr2
print("Divide the two arrays:",div_array)


# In[ ]:




