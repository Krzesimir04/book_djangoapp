from django.urls import path
from .views import *
urlpatterns=[
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register, name='register'),
    path('reservation', reservation, name='reservation'),
    path('reservation/<str:day>', reservation_2, name='reservation_2'),
    path('make_reservation/<int:pk>', make_reservation, name='make_reservation'),
    path('cancel/<str:day>/<str:pk>', cancel, name='cancel'),
]