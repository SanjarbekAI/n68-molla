from django.urls import path

from apps.calculator.views import calculator_view, history_view

app_name = 'calculator'

urlpatterns = [
    path('history/', history_view, name='history'),
    path('', calculator_view, name='caculator'),
]
