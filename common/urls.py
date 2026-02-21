from django.urls import include, path
from .views import HomepageView, FAQView

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("faqs/", FAQView.as_view(), name="faqs"),
]
