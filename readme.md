CMPE131 Email Client Project 
 - Pio Romo (Team Lead) @PioRomo
 - Barak Kaufman @barakkkaufman
 - Jin Chen @cjin1510
 - Thien Bryan Nguyen @thienbryannguyen6670


# BeeMail - CMPE 131 Email Client Group Project 
> Email client web application for CMPE 131 using Python, Flask, HTML, CSS

## Table of Contents
* [Introduction](#introduction)
* [Requirements](#requirements)
* [Responsibilities](#responsibilities)
* [Technologies Used](#technologies-used)
* [Setup](#setup)


## Introduction
Email client web application for CMPE 131. With this web app, users will be able to register, login/logout, delete their account, as well as send messages to other users. Additionally in this email client web application, the application will allow users to create to do lists and contact books, attach images to an email or message, manage their profile, and get notifications about the users' action such as the email or message being sent.

## Requirements
Our email web application will allow users to sign up to our application to send messages or emails to another user on the platform. For more details on the specific requirements, please read the requirements.md.

## Responsibilities
Pio Romo
 * Login
 * Logout
 * Registering for the website
 * Deleting account
 * Phone number verification

Barak Kaufman
 * Sending email
 * To Do List

Jin Chen
 * Profile Management
 * Chat box
 * Contact book

Thien Bryan Nguyen
 * Search Bar
 * Attaching images to emails
 * Notification after user action


## Technologies Used
- Python3 - version 3.10.0
- Flask, SQLite3, HTML, CSS 
- Complete Library: 
     | Library | Version | 
     |---------|---------|
     | click        | 8.1.3      |
     | Flask      | 2.2.3     |
     | Flask-Login        | 0.6.2        |
     | Flask-Reuploaded        | 1.3.0        |
     | Flask-SQLAlchemy        | 3.0.3        |
     | Flask-Uploads        | 0.2.1        |
     | Flask-WTF         | 1.1.1        |
     | greenlet        | 2.0.2         |
     | itsdangerous         | 2.1.2         |
     | Jinja2        | 3.1.2        |
     | MarkupSafe         | 2.1.2         |
     | phonenumbers         | 8.13.9         |
     | pip         | 23.1       |
     | pysqlite3           | 0.5.0        |
     | setuptools           | 67.2.0        |
     | SQLAlchemy            | 2.0.4       |
     | typing_extensions           | 4.5.0        |
     | Werkzeug            | 2.2.3        |
     | wheel           | 0.38.4         |
     | WTForms          | 3.0.1        |
     



## Setup

For this project, we had four main requirements. The app needed to be able to support registration, login, logout, and deleting an account. For a more detailed and comprehensive list of requirements, please see the requirements.md file, located in the repository. 

Proceed to describe how to install / setup one's local environment / get started with the project.

Want to try it out for yourself? Follow these instructions:
> Note: This tutorial requires basic knowledge of Linux and Git. Computer must also have python3/python installed. 

1) What we're going to do is open up the terminal. Use the `cd` command to navigate to the directory you want this repository to be stored in. 
2) Then, use the `git clone` command. You can go ahead and copy-paste this into the terminal: `git clone https://github.com/PioRomo/131-email-client.git`
   > Note: Ensure you're logged into GitHub before completing this step. 
3) You now have a cloned repository! Make sure your computer has all the proper libraries to run the project. You can check which python libraries are on your computer by using the `pip3 list` command for python3, or `pip list` for just python. Refer to the complete list of libraries above. 
   > Note: Missing libraries but not sure how to install them? Simply google "python" followed by the name of the library. 
4) Once you have all libraries installed, you should be ready to run the project. Make sure you are in the proper directory and type `flask run` into the terminal.
5) You know the app is running correctly if you see something like this in the terminal: 
    ```
     * Debug mode: off
       WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
     Press CTRL+C to quit
    
    ```   
6) Copy the url link and paste into your browser. You are now free to register, login, logout, delete your account, and of course, send emails! Enjoy! 






