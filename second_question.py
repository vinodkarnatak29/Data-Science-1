
# coding: utf-8

# #### Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[24]:


# @result variable should be blank, because if we run multiple time it will append and print the string.
result = ''
# @range() method include first parameter and exclude second one. so for 3200 we will use 3201.
for x in range(2000, 3201):
# check number is divisible by 7
    if(x%7)==0:
# check number is not multiple of 5
        if(x%5)!=0:
#append the number in string after converting into string, so that it will print in one line
            result += str(x)+","
#remove the last character of the string
result = result[:-1]
print(result)

