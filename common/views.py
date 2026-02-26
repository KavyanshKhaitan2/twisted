from django.shortcuts import render
from django.views import View
from .models import FAQ, KVPair


# Create your views here.
class HomepageView(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        rsvp_link, created = KVPair.objects.get_or_create(key="rsvp_link")
        rsvp_link.note = "Link behind the RSVP button.\n\nDelete this to reset."
        rsvp_link.save()
        if created:
            rsvp_link.value = "https://forms.fillout.com/t/5H3DKNAADius"
            rsvp_link.save()
        front_text, created = KVPair.objects.get_or_create(key="front_text")
        front_text.note = "Text on first glance.\n\nDelete this to reset."
        if created:
            front_text.value = "A unique YSWS where you make Cool Projects And Complete a twisted roadmap full of challenges to get PC!"
        front_text.save()

        bgeffect, created = KVPair.objects.get_or_create(key="bgeffect")
        bgeffect.note = "available values: 1, 2, 3\n\nDelete this to reset."
        if created:
            bgeffect.value = "1"
        bgeffect.save()

        extra_bg_classes, created = KVPair.objects.get_or_create(key="extra_bg_classes")
        extra_bg_classes.note = "Extra bg classes.\nFor blur, set to blur-xs, blur-sm, blur-md, blur-lg.\nMight support any tailwindcss class lol.\n\nDelete this to reset."
        if created:
            extra_bg_classes.value = "blur-sm"
        extra_bg_classes.save()

        bg_magnifier_size, created = KVPair.objects.get_or_create(
            key="bg_magnifier_size"
        )
        bg_magnifier_size.note = "set this to [width], [zoom]\n\nDelete this to reset."
        if created:
            bg_magnifier_size.value = "40vw, 1.5"
        bg_magnifier_size.save()
        bg_magnifier_width, bg_magnifier_zoom = [
            x.strip() for x in bg_magnifier_size.value.split(",")
        ]

        return render(
            request,
            "homepage.html",
            context={
                "faqs": faqs,
                "rsvp_link": rsvp_link.value,
                "front_text": front_text.value,
                "bgeffect": bgeffect.value,
                "extra_bg_classes": extra_bg_classes.value,
                "bg_magnifier_width": bg_magnifier_width,
                "bg_magnifier_zoom": bg_magnifier_zoom,
            },
        )


class FAQView(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        return render(request, "faq.html", context={"faqs": faqs})
