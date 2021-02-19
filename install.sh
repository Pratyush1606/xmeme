#!/bin/bash

# Update the apt package manager

sudo apt-get update

# Assuming python3 already installed

# Intall pip3
sudo apt-get install -y python3-pip

# Change the current directory to the django project

# Install the necessary requirements

pip3 install -r requirements.txt