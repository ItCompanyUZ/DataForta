from django.urls import URLPattern, path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]