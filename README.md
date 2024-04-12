# spotify-analysis

This read me is intended for others who want to examine their spotify listening history. Mac users should be able to run the python script as is, but Windows users will probably have to install python.



You can request your data files on the spotify privacy page (https://www.spotify.com/us/account/privacy/).
The data comes in .json format, probably in several different files.

The first step is to combine these into one file, then transform it into .csv format for easier analysis in tableau, excel, etc.
Use the "combine_json_to_csv.py" file, changing the path variable to the appropriate path, where your data is located. 

This will output a csv with all of your listening data. Some of the columns have been trimmed, drop null, ms_played converted to a timedelta duration. This about halved the file size for me.

"get-genre.py" works on a small scale, but not with the whole file due to limitations of Spotify's API. Could look into batching it, need to investigate further.
