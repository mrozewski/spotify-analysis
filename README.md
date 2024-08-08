# spotify-analysis

This read me is intended for others who want to examine their spotify listening history. 
Mac users should be able to run the Python script as is, but Windows users will probably have to install Python. 

You can request your data files on the Spotify privacy page (https://www.spotify.com/us/account/privacy/).
The data comes in .json format, probably in several different files.

You will receive your data in a few days, or closer to a month if you request full listening history.
The first step is to combine these into one file, then transform it into .csv format for easier analysis in Tableau, Excel, etc.

"python_project_plot.py" is the script that combines your data and outputs top 25 songs and artists, also plotting listening volume over time. All you need to do
is input the path to your folder where the data files are.


"get-genre.py" works on a small scale, but not with the whole file due to limitations of Spotify's API. Looking into batching it, need to investigate further. Maybe there is another music data API that would provide genres. 

Currently deciding how to implement visualization. The file shouldn't be too big for Excel, but Tableau might be easier for beginners. Tableau public is free and easy to configure. I'm considering writing a python portion in plotly to make it plug and play. 

Reccommended visualizations: 
-Listening volume over time, volume by season, and volume by day of the week.
-Listening by time of day
-Top artists, top songs.
  -Make this filterable by time period.
-Average song playtime to skip
-Songs most shuffled into
