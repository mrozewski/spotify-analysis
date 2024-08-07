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

#Let's trim some fields so the file isn't quite so big
#We can take the columns we want, drop any rows with missing values
df.dropna()
df_final = df[['ts', 'ms_played', 'master_metadata_track_name', 'master_metadata_album_artist_name',
'master_metadata_album_album_name','shuffle', 'skipped', 'offline' ]]

#Let's convert 'ms_played' to timestamp, with a separate field to make it easy for summing later on

df_final['duration'] = pd.to_timedelta(df_final['ms_played'] // 1000, unit='s')
df_final['duration_seconds'] = df_final['duration'].dt.total_seconds()


df.to_csv(os.path.join(path, 'combined_data.csv'))


