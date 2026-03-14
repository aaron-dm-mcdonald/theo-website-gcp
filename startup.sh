#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y git python3 python3-pip

cd /home
sudo git clone https://github.com/aaron-dm-mcdonald/theo-website-gcp.git
cd theo-website-gcp

sudo pip3 install flask requests

nohup python3 app.py > output.log 2>&1 &
