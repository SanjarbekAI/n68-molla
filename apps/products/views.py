from django.shortcuts import render

from apps.products.models import ProductCategory, ProductModel, ProductSize, ProductColor, ProductBrand


def products_list_view(request):
    categories = ProductCategory.objects.all()
    brands = ProductBrand.objects.all()
    colors = ProductColor.objects.all()
    sizes = ProductSize.objects.all()
    products = ProductModel.objects.all()

    cat_id = request.GET.get('cat')
    brand_id = request.GET.get('brand_id')
    color_id = request.GET.get('color_id')
    size_id = request.GET.get('size_id')
    q = request.GET.get('q')

    if cat_id:
        products = products.filter(categories=cat_id)

    if brand_id:
        products = products.filter(brand=brand_id)

    if color_id:
        products = products.filter(products_quantity__color=color_id)

    if size_id:
        products = products.filter(products_quantity__size=size_id)

    if q:
        products = products.filter(title__icontains=q)

    context = {
        "categories": categories,
        "brands": brands,
        "colors": colors,
        "sizes": sizes,
        "products": products,
    }
    return render(request, 'products/products.html', context)
