from django.urls import path
from . import view

urlpatterns = [
    path('login', view.login_user, name='login'),
    path('logout', view.logout_user, name='logout'),
    path('dealer/<int:dealer_id>/reviews', view.get_dealer_reviews, name='get_dealer_reviews'),
    path('get_dealers/', view.get_dealerships, name='get_dealers'),
    path('dealer/<int:dealer_id>', view.get_dealer_details, name='get_dealer_details'),
    path('get_dealers/<str:state>', view.get_dealers_by_state, name='get_dealers_by_state'),
    path('get_cars/', view.get_car_makes, name='get_car_makes'),
    path('analyzer/review/<str:text>', view.analyze_review, name='analyze_review'),
]