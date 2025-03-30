from django.urls import path, re_path
from . import views

app_name = 'HomeApp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # keep the name as home
    path('about/', views.AboutView.as_view(), name='about'),
    # path('portfolio-item/', views.PortfolioItemView.as_view(), name='portfolio-item'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    # path('case-studies/', views.CaseStudiesView.as_view(), name='case-studies'),
]

