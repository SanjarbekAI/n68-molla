from django.shortcuts import render, redirect

from apps.blogs.models import BlogModel
from apps.pages.forms import ContactForm
from apps.products.models import ProductModel


def home_page_view(request):
    last_products = ProductModel.objects.all().order_by('-created_at')[:5]
    last_blogs = BlogModel.objects.filter(
        status=BlogModel.BlogStatus.PUBLISHED
    ).order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'last_products': last_products,
        'last_blogs': last_blogs,
    })



def about_page_view(request):
    return render(request, 'pages/about.html')


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
