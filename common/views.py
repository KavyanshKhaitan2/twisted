from django.shortcuts import render
from django.views import View
from .models import FAQ

# Create your views here.
class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage.html')

class FAQView(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        return render(request, 'faq.html', context={'faqs': faqs})