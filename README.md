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
We start our virtual environment running `myvenv\Scripts\activate`.
