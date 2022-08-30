from django import template
from app.models import *

register = template.Library()

@register.filter(name='split')
def split(str, key):
    return str.split(key)


@register.filter(name='products')
def products(key):
	ppp = Product.objects.all().first()
	return [ppp.title,ppp.product_image.url,ppp.discounted_price]
