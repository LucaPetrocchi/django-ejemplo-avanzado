import requests

from django.core.cache import cache

from product.models import Product, Category

def dollar_exchange_rates(request):
    exchange_rates = cache.get('exchange_rates')
    if exchange_rates is None:
        exchange_rates = requests.get(
            'https://dolarapi.com/v1/dolares'
        ).json()
    
        cache.set(
            'exchange_rates', 
            exchange_rates, 
            1000,
        ) # NORMALMENTE NO USAR PARA ESTO ESPECIFICAMENTE
        # EL PRECIO DEL DOLAR TIENE QUE SIEMPRE ESTAR ACTUALIZADO
        # GUARDA!!!
        
    return dict(
        valores_dolar = exchange_rates
    )

def all_product_names(request):
    names = cache.get('product_names')
    if names is None:
        names = Product.objects.all().values_list('name')
        cache.set(
            'product_names',
            names,
            36000
        )
    return dict(
        nombres_productos = names
    )
    
def all_category_names(request):
    names = cache.get('category_names')
    if names is None:
        categories = Category.objects.all()
        names = [category.name for category in categories]
        cache.set(
            'category_names',
            names,
            36000
        )
    return dict(
        nombres_categorias = names
    )