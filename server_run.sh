#!/bin/bash

# Create new migrations based on changes to models

python3 manage.py makemigrations

# Apply or unapply migrations

python3 manage.py migrate

# Run the Django inbuilt development server

python3 manage.py runserver
