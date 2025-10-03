from django.core.management import BaseCommand

from apps.products.models import ProductModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = ProductModel.objects.all()
        for product in products:
            print(product.title)
