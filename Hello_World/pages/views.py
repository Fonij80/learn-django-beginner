from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# function-based view
def homePageView(request):
    return HttpResponse("Hello World!")

# class-based view
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"