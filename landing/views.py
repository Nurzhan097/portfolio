from django.shortcuts import render, get_object_or_404
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


def project_page(request, slug, pk):
	product = get_object_or_404(models.Product, slug=slug, pk=pk)
	context = {
		'product': product,
	}
	return render(request, 'landing/project_page.html', context)


def pages(request, template):
	context = {}
	return render(request, template, context)



