#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def normalize(df):
    result = df.copy()
    for col in df.columns:
        if col != "target" and col != "Day of Week":
            max_value = df[col].max()
            min_value = df[col].min()
            result[col] = (df[col] - min_value) / (max_value - min_value)
    return result

