#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def classify(current, future):
    if float(future) > float(current):
        return 1
    else:
        return 0

