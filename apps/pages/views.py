from django.shortcuts import render, redirect

from apps.pages.forms import ContactForm
from django.utils import timezone
import pytz
from apps.products.models import ProductDeal


def home_page_view(request):
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    now = timezone.now().astimezone(tashkent_tz)

    active_deal = ProductDeal.objects.filter(
        start_time__lte=now,
        end_time__gte=now
    ).first()

    final_price = None
    deal_timestamp = None
    if active_deal:
        original_price = active_deal.product.price
        discount_percent = active_deal.discount_price
        final_price = original_price * (100 - discount_percent) / 100

    context = {
        "active_deal": active_deal,
        "final_price": final_price,
    }
    return render(request, "home.html", context)


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
