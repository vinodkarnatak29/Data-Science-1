
# coding: utf-8

# #### Python program to find the volume of a sphere with diameter 12 cm.

# In[3]:


# @pi value is 3.1415926535897931 
# @radius is 6.0cm, because diameter is 12cm
# @volume formula is 4/3 (pi*r**3)
pi = 3.1415926535897931
radius = 6.0
volume = 4.0/3.0*(pi* radius**3)
volume = round(volume, 2)
print('The volume of the sphere is: ',volume, 'centimetercube')

