from django.shortcuts import render
from django.views import View
from .models import FAQ, KVPair

# Create your views here.
class HomepageView(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        rsvp_link, created = KVPair.objects.get_or_create(key='rsvp_link')
        if created:
            rsvp_link.value = "https://forms.fillout.com/t/5H3DKNAADius"
            rsvp_link.save()
        front_text, created = KVPair.objects.get_or_create(key='front_text')
        if created:
            front_text.value = "A unique YSWS where you make Cool Projects And Complete a twisted roadmap full of challenges to get PC!"
            front_text.save()
        return render(request, 'homepage.html', context={'faqs': faqs, "rsvp_link": rsvp_link.value, "front_text": front_text.value})

class FAQView(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        return render(request, 'faq.html', context={'faqs': faqs})