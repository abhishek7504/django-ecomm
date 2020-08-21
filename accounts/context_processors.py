from django.conf import settings
from web.models import Product, Category


def main(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        "category" : category,
        "product" : product,
    }

    return context
