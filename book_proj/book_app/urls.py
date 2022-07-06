from django.urls import path
from .views import *
urlpatterns=[
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register, name='register'),
    path('reservation', reservation, name='reservation'),
    path('reservation/<str:date>', reservation_2, name='reservation_2'),
]