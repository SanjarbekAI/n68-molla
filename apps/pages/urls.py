from django.urls import path

from apps.pages.views import home_page_view, ContactPageView, about_page_view

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', about_page_view, name='about'),
    path('', home_page_view, name='home'),
]
