from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def indexPageView(request) :
#     sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
#     return HttpResponse(sOutput)

def indexPageView(request) :
    return render(request, 'travelpages/index.html')


# def aboutPageView(request, trip_name, trip_length) :
#     trip_length = trip_length + 2
#     sOutput = '<html><head><title>My Title</title></head><body><p>The trip to ' + trip_name + ' will be ' + str(trip_length) + ' days with airfare.' + '</p></body></html>'
#     return HttpResponse(sOutput)

def aboutPageView(request, trip_name, trip_length) :

    context = {
    "trip_name" : trip_name,
    "trip_length" : trip_length + 2,
    "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]
    } 

    return render(request, 'travelpages/about.html', context)  