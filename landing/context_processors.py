from . import forms, models


def contact_form(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	contact_form_in_all_page = forms.ContactForm()
	company_info = {
		'name': 'WebStructure',
	}
	return locals()
