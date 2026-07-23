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
# %Y = 4-digit year
# %h = month in words and %m = month in numbers
# %d = date
# %H = hours 
# %M = minutes
# %S = seconds
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
TIMESTAMPS=$(date +"%Y-%h-%d  %H:%M:%S")
echo "Timestamp: $TIMESTAMPS"

#PART 3: REMOVE AND MOVE THE grades.csv INTO THE 'archive' FOLDER
ORIGINAL_FILE="grades.csv"
ARCHIVED_FILE="grades_${TIMESTAMP}.csv"

if [ -f "$ORIGINAL_FILE" ];then 
    mv "$ORIGINAL_FILE" archive/$ARCHIVED_FILE #move the grades.csv into the archive folder and also rename it with the timestamp
    echo "The '$ORIGINAL_FILE' was successfully moved to 'archive/$ARCHIVED_FILE'"


#PART 4: CREATE A NEW AND EMPTY FILE NAMED 'grades.csv' FOR THE NEXT BATCH OF GRADES
    #'touch' creates a new and empty file if it doesn't exists for the next fresh batch of grades 
    touch $ORIGINAL_FILE
    echo "A new and empty '$ORIGINAL_FILE' was created" 

#PART 5: LOG EVERYTHING INTO 'organizer.log'

    echo "[$TIMESTAMP] archived '$ORIGINAL_FILE' as '$ARCHIVED_FILE'" >> organizer.log #'>>' appends to the end of the file then,
    #creates it if it doesn't exist yet. Instead of overwriting it, so eveytimr it runs a new line is added to the history. 
    echo "Logged this action to organizer.log"

else
    # This would run if the grades.csv file did not exist when the script was started.
    echo "There was no $ORIGINAL_FILE found in the current folder. There's nothing to archive" 
    echo "[$TIMESTAMP] attempted to archive '$ORIGINAL_FILE' but it was missing." >> organizer.log
fi 

echo "DONE"





