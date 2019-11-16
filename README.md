# Adventskalender
A web based advent calendar implemented in Python and using a Django backend. Upload your own 24 images and provide a nice surprise to a friend ;)

## Prerequisites
* Python Version 3.7
* Django >= 2.2.7
If Django is not on your server, install it with ```sudo pip install django```

## Installation
1. Clone this repository
2. Enter the *adventskalender* folder and execute the following commands
    * ```python manage.py createsuperuser``` to create an account with access to the administrator dashboard
    * ```python manage.py makemigrations``` to create the database files
    * ```python manage.py migrate``` to apply the migrations
    * ```python manage.py init``` to create the inital database entries

## Upload images
1. Visit the page *<your-domain>:8000/admin*
2. Log in with your credentials
3. Visit the link to the table **Windows**
4. Click on the table entry containing the window to which you want to assign an image
5. Upload an image by clicking on the upload button next to **content**
