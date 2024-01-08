# Project Introduction

The project mainly uses the Echo Nest API to crawl, clean, and visualize Spotify's data. 
By climbing the top 20 genres, then climbing the top 50 songs in each genre, and then obtaining the audio characteristics of each song. 
The complete data set is obtained by data cleaning operations such as merging and de-duplication. 
Based on the data set, the problem is proposed and tried to solve.


# Environmental Dependence

Python 3.10
Pandas
Numpy
Matplotlib
scikit-learn
(The above package can be used with the latest version, pay attention to the version mapping.)


# Code Framework

|——Readme.md                // help document
|——`Crawl_Spotify_API.ipynb`  // main program
| |——Token acquisition      // get API access
| |——Genres acquisition     // get genres
| |——Tracks acquisition     // get tracks
| |——song feature acquisition     // get song feature
| |——data cleansing         // get cleaned data
| |——creat output database  // get `output.csv`
| |——Data visualization     // get visualization figure
| |——conclusion             // task summary


# Instructions

Available file in Part2 `Crawl_Spotify_API.ipynb` and `output.csv`
The API and data are constantly being updated and the results of the run are not static. 
Also pay attention to the request rate during the run.
If the rate is too high it may lead to speed limit. 
The solution is to recreate the account and application in Spotify's Developer platform to get the API license for the letter.

## Version Control

V1.0 
  V1.0.0 Implement basic token access requests.
  V1.0.1 Generate the final data set.
v2.0 
  v2.0.0 Draw histogram, heat map, complete visualization work.
  v2.0.1 Update the latest data, add the recommended song problem, and use KNN algorithm to solve the problem.
