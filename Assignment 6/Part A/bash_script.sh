#!/bin/bash

sudo docker container stop ass6
sudo docker container rm ass6

mkdir testfolder

pwd

sudo docker run -dit --name=ass6 \
    -v ./testfolder:/myfolder \
    python:3.8-slim

sudo docker exec -it ass6 /bin/bash

done
