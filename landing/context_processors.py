from . import forms, models


def contact_form(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	company_info = {
		'name': 'WebStructure',
	}
	return locals()
