#!/usr/bin/env python
# coding: utf-8

# In[1]:


# METHOD 1
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# example: blackjack(5,6,7) --> 18 
#          blackjack(9,9,9) --> 'BUST'
#          blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    if sum([a,b,c]) == 21:
        return 'WooHoo!!, it is BLACKJACK'
    elif sum([a,b,c]) < 21:
        return sum([a,b,c])
    elif sum([a,b,c]) > 21 and a == 11 or b == 11 or c == 11:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'
    


# In[2]:


blackjack(4,5,6)


# In[3]:


blackjack(9,9,9)


# In[4]:


blackjack(9,9,3)


# In[ ]:


# METHOD 2
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# example: blackjack(5,6,7) --> 18 
#          blackjack(9,9,9) --> 'BUST'
#          blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    if sum([a,b,c]) == 21:
        return 'WooHoo!!, it is BLACKJACK'
    elif sum([a,b,c]) < 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'

