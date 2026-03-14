#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y git python3 python3-flask python3-requests

cd /home
sudo git clone https://github.com/aaron-dm-mcdonald/theo-website-gcp.git
cd theo-website-gcp

sudo nohup python3 app.py > output.log 2>&1 &
