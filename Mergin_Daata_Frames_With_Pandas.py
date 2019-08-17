# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 08:31:54 2019

@author: Julio
"""

import pandas as pd
bronze = pd.read_csv('Bronze.csv')
silver = pd.read_csv('Silver.csv')
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())
