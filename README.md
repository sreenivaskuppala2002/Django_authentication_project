
# User Authentication System using Django

This project is implemented Using Django server side web framework,Html,Bootstrap. It is user authentication System that deals with user login, logout and user registration using Django.


## Installation


Step-1:
 First step we have to download python https://www.python.org/downloads/ from here, if you already download please ignore. Check pip installed in your computer using the following command in command prompt.
```bash
 pip --version 
```
step-2:
To work with Django project we have to set up virtual environment to set up virtual environment please follow below below steps.

```bash
# Install virtual environment using below command
pip install virtualenv 

#Make a directory <name> as you wish here it is Project
mkdir Project

#create virtualenvironment using following command
py -m venv <name>

#Activate virtual environment by
<name>\Scripts\activate.bat
``` 
Now we are ready to install Django using following commands
```bash
# To install django
 pip install django

 #To check the version
 django-admin version 
```
Step-3: After sucessfully completing Django now we are ready to start project using following commands.
```bash
 # To create Project
 django-admin startproject <projectname> 
```
Step-4: Clone git repository
```bash
git clone "https://github.com/sreenivaskuppala2002/Django_authentication_project"
```
Step-5:Change directory to project Folder
```bash
cd <projectname>
```
Step-6:Finally make migrations and finally runserver
```bash
#
#To migrate
py manage.py migrate 

#To runserver
py manage.py runserver
```

