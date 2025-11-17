from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('affiliations/', views.affiliations, name='affiliations'),
    path('contact/', views.contact, name='contact'),
    path('contact_data/', views.contact_data, name='contact_data'),
    path('course/', views.course, name='course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]
