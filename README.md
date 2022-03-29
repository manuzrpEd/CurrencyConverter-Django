# Currency Converter - Code Challenge

The following is a coding challenge. I intend to build an API that allows end-users to convert one amount from one currency to another. I will simply reference this API from my front end:

http://api.currencylayer.com/

Using [Django](https://www.djangoproject.com/)'s Python web framework, I will expose the API functionality to users. Users should be able to select a source currency, enter an amount and select a destination currency. The app should then convert the amount to the destination currency and display the converted amount.

My solution can be found in the following website: https://simplecurrency.onrender.com

# Steps of my code solution - Django framework

### Virtual environment ###

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

### Django project/app ###

Now we are in a position to start our Django project. Execute the command `django-admin.exe startproject currency_converter .` to start the Djago project. An app in Django is a subcomponent of the Django project. To start our currency app, execute `python manage.py startapp converter`. 

At this point, we have created all files and directories needed for our project/application. Using a Code editor, we can modify the files of our project/app to our particular needs. I use [Visual Studio Code](https://code.visualstudio.com/).

1. In the `settings.py` file, we need to add `converter` in the list of `INSTALLED_APPS`.
2. Add `ALLOWED_HOSTS = ['currencyconverter.onrender.com']` to `settings.py` file.
3. Create a `.env` file at the root of the project.
4. Execute `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` and add `SECRET_KEY=<YOUR DJANGO PROJECT SECRET KEY>` to the `.env` file created.
5. Add `SECRET_KEY = str(os.getenv('SECRET_KEY'))` to `settings.py` file.
6. Add `USE_THOUSAND_SEPARATOR = True` to `settings.py` file.
7. Under `Views.py`, define the function responsible for handling the currency exchange:
```
def index(request):
    # define the temlate name
    template = 'index.html'
    if request.method == 'POST':

        # first currency
        currency1 = request.POST.get('currency1', False)

        # second currency
        currency2 = request.POST.get('currency2', False)

        # amount to exchnage
        amount= request.POST.get('amount', False)
        try:
            amount=float(amount)
            result="Success"
            time.sleep(2)
        except:
            amount=0
            result="Error. Please enter numerical values only."
            time.sleep(2)

        # response = requests.get(f"{url}/convert?access_key={key}&from={currency1}&to={currency2}&amount={amount}")
        response = requests.get(f"{url}/live?access_key={key}")

        # response data convterted to json
        # data = response.json()
        # rate = data['info']['quote']
        # amt = data['result']
        # context = {"rate": rate, 'amount': amt}
        data = response.json()
        quotes = data['quotes']

        rate=1
        if currency1!=currency2:
            if currency1+currency2 in quotes.keys():
                rate=quotes[currency1+currency2]
            elif currency2+currency1 in quotes.keys():
                rate=1/quotes[currency2+currency1]
            elif ('USD'+currency1 in quotes.keys()) and ('USD'+currency2 in quotes.keys()):
                rate=quotes['USD'+currency2]/quotes['USD'+currency1]
    

        amt = amount*rate
        context = {"rate": round(rate,4), 'amount': round(amt,4), 'pair':currency1+currency2
        , 'currency1':currency1
        , 'currency2':currency2
        ,'amt_entered':amount
        ,'status':result}

        # render the template with the data passed to it
        return render(request, template, context)
    else:
        return render(request, template)
```
