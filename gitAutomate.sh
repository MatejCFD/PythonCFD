#!/bin/bash

# Add the CFD codes written in python
# Based on Lorena Barba's 12 Steps to Navier-Stokes
# Augmented by Matej Tomić
git remote add origin https://github.com/MatejCFD/PythonCFD.git

git init
git add .

echo "What is the commit name?"
read NAME

git commit -m "$NAME"

git push --set-upstream origin master
git push
