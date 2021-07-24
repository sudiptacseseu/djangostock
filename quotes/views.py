from django.shortcuts import render, redirect
from quotes.forms import StockForm
from quotes.models import Stock
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    import json
    import requests

    if request.method == "POST":
        # pk_a9cd941501394a8facc1819c18002e51
        # https://cloud.iexapis.com/stable/stock/fb/quote?token=pk_a9cd941501394a8facc1819c18002e51
        ticker = request.POST["ticker_input"]
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +
                                   "/quote?token=pk_a9cd941501394a8facc1819c18002e51")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter Your Ticker Above to Continue!"})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock Has Been Added!")
            stocks = Stock.objects.all()
            #return render(request, 'add_stock.html', {'stocks': stocks})
            return redirect('add_stock')
        # else:
        #     stocks = Stock.objects.all()
        #     return render(request, 'add_stock.html', {'stocks': stocks})

    else:
        stocks = Stock.objects.all()
        output = []
        for stock_item in stocks:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(
                stock_item) + "/quote?token=pk_062031d20883444f9ea74e2610fe2011")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'stocks': stocks, 'output': output})


def delete(request, stock_id):
    stock = Stock.objects.get(pk=stock_id)
    stock.delete()
    messages.success(request, "Item has been deleted!")
    return redirect(delete_stock)


def delete_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'delete_stock.html', {'stocks': stocks})
