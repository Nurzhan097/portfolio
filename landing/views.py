from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from . import models, forms


# Create your views here.
def main_page(request):
	products = models.Product.objects.filter(is_active=True)
	categories = models.ProductCategory.objects.filter(is_active=True)
	contact_form = forms.ContactForm()

	context = {
		'products': products,
		'categories': categories,
		'contact_form': contact_form,

	}
	return render(request, 'landing/main_page.html', context)


def project_page(request, slug, pk):
	product = get_object_or_404(models.Product, slug=slug, pk=pk)
	context = {
		'product': product,
	}
	return render(request, 'landing/project_page.html', context)


def contact_with_us(request):
	message = ''
	context = {}
	contact_form = forms.ContactForm()

	if request.method == 'POST':
		contact_form = forms.ContactForm(request.POST)
		context['contact_form'] = contact_form
		if contact_form.is_valid():
			new_contact = contact_form.save()

			session_key = request.session.session_key
			if not session_key:
				request.session.cycle_key()
			created_contact = models.Contact.objects.get(pk=new_contact.pk)
			created_contact.session_key = session_key
			created_contact.save()

			context['message'] = "ЗБС заработало"
			context['url_scheme'] = request.META['wsgi.url_scheme']  # .wsgi.url_scheme
			context['HTTP_HOST'] = request.META['HTTP_HOST']  # .wsgi.url_scheme

			# TODO: Сделать нормальные страницы для подтверждения отправки писем
			is_sended_to_client = send_mail(
				f'name - {new_contact.name}, ',
				'hello world!',
				settings.EMAIL_HOST_USER,
				[new_contact.email, ],
				fail_silently=False,
				html_message=get_template('contact_done.html',).render(context),
			)
			is_sended_to_admin = send_mail(
				f'name - {new_contact.name}, ',
				'hello world!',
				settings.EMAIL_HOST_USER,
				['atar.7@ya.ru', ],
				fail_silently=False,
				html_message=get_template('contact_done.html',).render(context),
			)
			if is_sended_to_client and is_sended_to_admin:
				return render(request, 'contact_done.html', context)
			else:
				message = "Mail did't send"

	context['contact_form'] = contact_form
	context['message'] = message
	return render(request, 'contact_form_page.html', context)


def pages(request, template):
	context = {}
	return render(request, template, context)
