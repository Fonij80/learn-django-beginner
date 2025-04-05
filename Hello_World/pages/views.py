from django.http import HttpResponse
from django.views.generic import TemplateView


# function-based view
def home_page_view(request):
    return HttpResponse("Hello World!")

# class-based view
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"