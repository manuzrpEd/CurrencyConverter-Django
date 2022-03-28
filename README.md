# Currency Converter - Code Challenge

The following is a coding challenge. I intend to build an API that allows end-users to convert one amount from one currency to another. I will simply reference this API from my front end:

http://api.currencylayer.com/

Using [Django](https://www.djangoproject.com/)'s Python web framework, I will expose the API functionality to users. Users should be able to select a source currency, enter an amount and select a destination currency. The app should then convert the amount to the destination currency and display the converted amount.

My solution can be found in the following website: https://simplecurrency.onrender.com

# Steps of my code solution

On Windows 11, open the command prompt and move to a directory where we will create our virtual environment. A virtual environment is a tool that helps to keep the dependencies required by this project separate from other. We create a folder for our project, navigate into the folder and create the virtual environment in the following way:
```
mkdir currency
cd currency
python3 -m venv myvenv
```

We start our virtual environment running `myvenv\Scripts\activate`. Then, it is good practice to have a requirements file to list all the dependencies to be installed. The file will store information about all the libraries, modules, and packages that are used while developing our project.

Create `requirements.txt` file and add `Django~=3.2.10` in the file. Then, the commands:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
will make sure that we have the latest software `pip` to install libraries and we will have Django installed.

Now we are in a position to start our Django project. Execute the command `django-admin.exe startproject currency_converter .` to start the Djago project. An app in Django is a subcomponent of the Django project. To start our currency app, execute `python manage.py startapp converter`. 

At this point, we have created all files and directories needed for our project/application. Using a Code editor, we can modify the files to addapt our project/app to our needs.
