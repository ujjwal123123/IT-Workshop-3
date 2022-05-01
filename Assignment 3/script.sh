#!/bin/bash

yum update -y
yum install -y httpd
service httpd start
service enable httpd

cd /var/www/html

# Download data from S3
wget https://ujjwal-bucket-boto.s3.amazonaws.com/files.zip
unzip files.zip
rm files.zip