from django.shortcuts import render
from .models import ItemCode

# Create your views here.
def home(request):
    import json
    import requests

    # url = "https://covid-19-data.p.rapidapi.com/totals"

    # querystring = {"format":"undefined"}

    # headers = {
    #     'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    #     'x-rapidapi-key': "9287de9f8cmsh91471eb30f46b0dp1a427cjsnfb204ba1b3d5"
    #     }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    
   
    # api_covid19 = json.loads(response.content)
    
    
    all_items = ItemCode.objects.all
    

    if request.method == "POST":
        SearchCriteria = request.POST['SearchCriteria']
        
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + SearchCriteria + "&distance=25&API_KEY=E6B0BF0D-FDB4-4950-9DA2-F28DAD79D5C1")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error..."

        return render(request,'index.html',{'api' : api, 'all_items' : all_items})
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=31.5204&longitude=74.3587&distance=200&API_KEY=E6B0BF0D-FDB4-4950-9DA2-F28DAD79D5C1")
        #api_request=request.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode="+ SearchCriteria +"&distance=25&API_KEY=E6B0BF0D-FDB4-4950-9DA2-F28DAD79D5C1")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error..."

        return render(request,'index.html',{'api' : api, 'all_items' : all_items })

def about(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=31.5204&longitude=74.3587&distance=200&API_KEY=E6B0BF0D-FDB4-4950-9DA2-F28DAD79D5C1")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "error..."
    return render(request,'about.html',{'api' : api})

def coronavirus(request):
    import json
    import requests

    api_covid19_request=requests.get("https://api.covid19api.com/summary")

    try:
        api_covid19_summary = json.loads(api_covid19_request.content)
    except Exception as e:
        api = "error..."
    return render(request,'coronavirus.html',{"api_covid19_summary" : api_covid19_summary})
