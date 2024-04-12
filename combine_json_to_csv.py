#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:07:14 2024

@author: michaelrozewski
"""

import os
import pandas as pd

#Put the path to the destination folder in these parantheses
path = ""

files = os.listdir(path)
df_list = []


#loop through file list, adding json files as dataframes to df_list
#ds_store hidden file was messing it up, so excepting that one
for file in files:
    try:
       print('Processing', file)
       file_path = os.path.join(path, file)
       df_list.append(pd.read_json(file_path, encoding='utf-8'))
    except:
        file.startswith('.')

#now, concatenate the list of dfs together, translate to csv
df = pd.concat(df_list)
df.to_csv(os.path.join(path, 'combined_data.csv'))


