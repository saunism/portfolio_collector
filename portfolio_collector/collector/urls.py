from django.urls import path
from . import views
urlpatterns=[
    path('',views.main),
    path('registration',views.registration),
    path('log_in',views.log_in),
    path('portfolio',views.create_portfolio),
    path('profile',views.show_profile),
    path('user/<int:id>',views.show_user),
    path('list',views.show_list)
]