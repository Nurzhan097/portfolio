from django.shortcuts import render
from . import models


# Create your views here.
def main_page(request):
	products = models.Product.objects.filter(is_active=True)
	categories = models.ProductCategory.objects.filter(is_active=True)
	print(f'EEEEEEE {categories}')
	context = {
		'products': products,
		'categories': categories,
	}
	return render(request, 'landing/main_page.html', context)


def pages(request, template):
	context = {}
	return render(request, template, context)



