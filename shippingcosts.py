#!/usr/bin/env python
# coding: utf-8

# In[1]:


weight = 4.8


# GROUND SHIPPING

flat_charge = 20.00

if weight <= 2:
  cost_1 = 1.50*weight + flat_charge
elif weight > 2 and weight <= 6:
  cost_1 = 3.00*weight + flat_charge
elif weight > 6 and weight <=10:
  cost_1 = 4.00*weight + flat_charge
elif weight > 10:
  cost_1 = 4.75*weight + flat_charge

print(cost_1)



premium_ground_shipping = 125



# DRONE SHIPPING

weight = 4.8

if weight <= 2:
  cost_2 = 4.50*weight 
elif weight > 2 and weight <= 6:
  cost_2 = 9.00*weight
elif weight > 6 and weight <= 10:
  cost_2 = 12.00*weight
elif weight > 10:
  cost_2 = 14.25*weight

print(cost_2)


# In[ ]:




