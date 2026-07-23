#!/usr/bin/env bash 
# PART 1: CHECK IF "archive" DIRECTORY EXISTS
if [ ! -d "archive" ]; then # ! means 'not', -d checks if 'archive' directory already exists and if it is a directory not a file.
    mkdir archive #making the directory
    echo " 'archive' directory is created." #echo just print the message
else
    echo " 'archive' directory already exists."
fi 

#PART 2: CREATE A TIMESTAMP STRING  
# date command with the "+" FORMAT prints the current time where:
# %Y = 4-dgit year
# %h = month in words 
# %d = date
# %H = hours 
# %M = minutes
# %S = seconds
TIMESTAMP=$(date +"%Y-%h-%d  %H:%M:%S")
echo "Timestamp: $TIMESTAMP"

