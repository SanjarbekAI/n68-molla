from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.pages.forms import ContactForm
from apps.pages.models import ContactModel, StoreModel


def home_page_view(request):
    return render(request, 'home.html')


def about_page_view(request):
    return render(request, 'pages/about.html')


class ContactPageView(ListView):
    model =  StoreModel
    template_name = 'pages/contact.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['store'] = StoreModel.objects.filter(is_active=True)
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.result = 1313  # Sizning custom field
            contact.save()
            return redirect('pages:contact')
        else:
            # Form xatolari bilan sahifani qayta ko'rsatish
            errors = []
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)

            # ListView context bilan birga xatoliklarni yuborish
            context = self.get_context_data()
            context['errors'] = errors
            context['form'] = form  # Xatolikli formni qaytarish
            return self.render_to_response(context)

# def contact_page_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             form.result = 1313
#             form.save()
#             return redirect('pages:contact')
#         else:
#             errors = []
#             for key, value in form.errors.items():
#                 for error in value:
#                     errors.append(error)
#             context = {
#                 "errors": errors
#             }
#             return render(request, 'pages/contact.html', context)
#
#     else:
#
#         return render(request, 'pages/contact.html')