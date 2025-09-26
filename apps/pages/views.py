from django.shortcuts import render, redirect

from apps.pages.forms import ContactForm
from apps.pages.models import TeamModel


def home_page_view(request):
    return render(request, 'home.html')


def about_page_view(request):
    teams =TeamModel.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'pages/about.html', context)


def contact_page_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.result = 1313
            form.save()
            return redirect('pages:contact')
        else:
            errors = []
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)
            context = {
                "errors": errors
            }
            return render(request, 'pages/contact.html', context)

    else:
        return render(request, 'pages/contact.html')
