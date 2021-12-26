from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("Hello, world. You're at the home page.")
    return render(request, "home.html", {})
    
def channels_view(request, *args, **kwargs):
    return render(request, "channels.html", {})
    