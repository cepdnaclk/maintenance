#!/bin/sh

echo "Obtaining repository data"
python3 ./generate.py 

echo "Synchronizing the repositories"
cd ./backup/ && sh execute.sh 