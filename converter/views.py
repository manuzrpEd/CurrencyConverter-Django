from django.shortcuts import render
import requests,time

url='http://api.currencylayer.com/'
# key=str(os.getenv('API_KEY'))
key='6c50234f11b23904b97cd52b2236673f'

# Create your views here.

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
