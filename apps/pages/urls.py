from django.urls import path

from apps.pages.views import home_page_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home')
]
