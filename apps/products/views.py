from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.products.models import ProductCategory, ProductModel, ProductSize, ProductColor, ProductBrand


class ProductsListView(ListView):
    model = ProductModel
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = ProductModel.objects.all()

        # Get filter parameters from GET request
        cat_id = self.request.GET.get('cat')
        brand_id = self.request.GET.get('brand_id')
        color_id = self.request.GET.get('color_id')
        size_id = self.request.GET.get('size_id')
        q = self.request.GET.get('q')

        # Apply filters
        if cat_id:
            queryset = queryset.filter(categories=cat_id)

        if brand_id:
            queryset = queryset.filter(brand=brand_id)

        if color_id:
            queryset = queryset.filter(products_quantity__color=color_id)

        if size_id:
            queryset = queryset.filter(products_quantity__size=size_id)

        if q:
            queryset = queryset.filter(title__icontains=q)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add filter options to context
        context['categories'] = ProductCategory.objects.all()
        context['brands'] = ProductBrand.objects.all()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()

        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'product'

