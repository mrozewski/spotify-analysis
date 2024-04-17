# spotify-analysis

This read me is intended for others who want to examine their spotify listening history. Mac users should be able to run the Python script as is, but Windows users will probably have to install Python.

You can request your data files on the Spotify privacy page (https://www.spotify.com/us/account/privacy/).
The data comes in .json format, probably in several different files.

You will receive your data in a few days, or closer to a month if you request full listening history.
The first step is to combine these into one file, then transform it into .csv format for easier analysis in Tableau, Excel, etc.
Use the "combine_json_to_csv.py" file, changing the path variable to the appropriate path, where your data is located. 

This will output a csv with all of your listening data. Some of the columns have been trimmed, drop null, ms_played converted to a timedelta duration. This about halved the file size for me.

"get-genre.py" works on a small scale, but not with the whole file due to limitations of Spotify's API. Looking into batching it, need to investigate further. Maybe there is another music data API that would provide genres. 

Currently deciding how to implement visualization. The file shouldn't be too big for Excel, but Tableau might be easier for beginners. Tableau public is free and easy to configure. I'm considering writing a python portion in plotly to make it plug and play. 

Reccommended visualizations: 
-Listening volume over time, volume by season, and volume by day of the week.
-Listening by time of day
-Top artists, top songs.
  -Make this filterable by time period.
-Average song playtime to skip
-Songs most shuffled into
