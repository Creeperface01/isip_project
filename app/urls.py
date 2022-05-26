from django.urls import path
from app.views import homepage


urlpatterns = [
    path('', homepage),
]
