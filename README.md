mobile AAT setup
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## How to use?

### Setup Firebase

Before using this package, you need to setup a firebase project. Firebase will be used to store your experiments and study data online. If you
already have Firebase set up, skip to step 4.

1)  Open http://firebase.google.com, log in with your google account and
    create a new project.
    - The name here does not matter, you don’t need google analytics
2)  In your project create a database (this is where the data AATs be
    stored)
    - click on Realtime Database (on the left)
    - click Create Database
    - choose Belgium for Database location
    - choose start in locked mode
    - ones the database is created click on Rules (on the top) and
      change the two “false” to “true”
    - Publish
3)  Create Firebase storage (this is where you can upload experiments)
    - click on Storage (on the left)
    - click on Get started
    - Start in production mode
    - Set location to Europe west
    - click on Rules and change the “false” to “true”
4)  Add the app
    - Click on the cog, next to Project Overview (upper left)
    - Click on Project settings
    - Click on the Android logo (bottom)
    - Under Android package name, fill in com.yourname.picturegame,
      where you replace yourname with your name or your lab’s name.
5)  Download google-services.json

### Install the mobile aat setup package

This package will help you make the mobile AAT app. If you haven't installed Python yet. First, install [Python 3](https://www.python.org/downloads/)

Once Python is installed, run this from your Terminal App on a Mac or from Command Prompt on Windows:

`pip install mobile_aat_setup`

### Setup the app

[`setup_aat`](https://hgzech.github.io/mobile_aat_setup/setup.html#setup_aat)
downloads the newest version of the mobile AAT app, changes the app’s
package ID (so you can upload your own version of the app to the
Playstore) and links the app to your google Firebase account.

``` python
from mobile_aat_setup.setup import setup_aat

PATH_TO_WHERE_YOU_WANT_TO_STORE_THE_APP = '/Users/hilmarzech/Desktop/mobileaat'
PATH_TO_GOOGLE_SERVICES_JSON = '/Users/hilmarzech/Desktop/google-services.json'

setup_aat(PATH_TO_WHERE_YOU_WANT_TO_STORE_THE_APP, PATH_TO_GOOGLE_SERVICES_JSON)
```

### Download Android Studio and open the created app folder

You should now be able to run the app on your device.
