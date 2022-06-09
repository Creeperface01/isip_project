from django.urls import path
from app.views import homepage, login_request, rental, logout_request, signup_request, my_rentals, rental_item, return_item


urlpatterns = [
    path('', homepage),
    path('login', login_request),
    path('rental/<int:place_num>', rental),
    path('logout', logout_request),
    path('signup', signup_request),
    path('myrentals', my_rentals),
    path('rental_item', rental_item, name='rental_item'),
    path('return_item/<int:id_order>', return_item, name='return_item'),
]
