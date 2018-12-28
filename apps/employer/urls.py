from django.urls import path

from . import views
urlpatterns = [
    path('',views.employer, name='employer' ),

]