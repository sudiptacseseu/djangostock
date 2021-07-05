
from django.shortcuts import render


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
