#!/bin/bash

echo "Current directory:"
pwd

echo
echo "Files in scratch/:"
ls scratch

echo
echo "Lines mentioning 'Linux' in scratch/notes.txt:"
grep "Linux" scratch/notes.txt
