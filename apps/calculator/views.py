from django.shortcuts import render

from apps.calculator.forms import CalculatorForm
from apps.calculator.models import ResultModel


def calculator_view(request):
    if request.method == "GET":

        return render(request, 'calculator/calculator.html')
    else:
        form = CalculatorForm(request.POST)
        if form.is_valid():
            data = form.save()
            context = {
                "result": data.result
            }
            return render(request, 'calculator/calculator.html', context)

        return None


def history_view(request):
    if request.method == "GET":
        results = ResultModel.objects.all()
        context = {
            "results": results
        }
        return render(
            request, 'calculator/history.html',
            context)
    return None
