from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from apps.pages.forms import ContactForm
from apps.pages.models import BannerModel
from core import settings


def home_page_view(request):
    banners = BannerModel.objects.filter(is_active=True)
    context = {'banners': banners}
    return render(request, 'home.html', context)


def about_page_view(request):
    return render(request, 'pages/about.html')


def contact_page_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

            # then check permission
            if not request.user.has_perm("pages.add_contactmodel"):
                raise PermissionDenied

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
