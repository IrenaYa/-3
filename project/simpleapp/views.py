# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):
    # model = Product
    # ordering = 'name'
    #queryset = Product.objects.order_by(
    #    'name'
    # )
    template_name = 'products.html'
    context_object_name = 'products'