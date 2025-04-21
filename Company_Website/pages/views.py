from django.shortcuts import render
from django.views.generic import TemplateView


def home_page_view(request):
    context = {
        "available_jobs": ["Backend Developer", "React Developer", "Data Scientist"]
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address"] = "Theran, Kaj Street"
        context["phone_number"] = "021-624-8837"
        return context