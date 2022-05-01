#!/bin/bash
yum update -y
wget https://ass4.s3.amazonaws.com/ass4-ujjwal.zip
unzip ass4-ujjwal -d website
cd website
yum install docker -y
systemctl start docker.service
docker build . -t ass6image
docker run -p 80:8080 -d --name ass6container ass6image
