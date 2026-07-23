#!/usr/bin/env bash 
# PART 1: CHECK IF "archive" DIRECTORY EXISTS
if [ ! -d "archive" ]; then # ! means 'not', -d checks if 'archive' directory already exists and if it is a directory not a file.
    mkdir archive #Making the directory
    echo " 'archive' directory is created."
else
    echo " 'archive' directory already exists."
fi 

