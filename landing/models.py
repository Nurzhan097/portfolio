from django.db import models


# Название доступных продуктов
class ProductCategory(models.Model):
	name = models.CharField(max_length=40, verbose_name='Название')
	slug = models.SlugField(verbose_name='Краткое название', help_text="Ссылка")

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name = 'Категория продуктов'
		verbose_name_plural = 'категорий продуктов'
		ordering = ('name',)

	def __str__(self):
		return f'{self.name}'


# Статус заявки
class ContactStatus(models.Model):
	name = models.CharField(max_length=150, verbose_name='Статус')
	color_bootstrap = models.CharField(max_length=40, verbose_name="Цвет в bootstrap")

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name = 'Статус заявки'
		verbose_name_plural = 'Статусы заявок'
		ordering = ('name',)

	def __str__(self):
		return f'{self.name}'


# Предпочитаемый метод связи
class DesiredContactMethod(models.Model):
	name = models.CharField(max_length=80, verbose_name='Предпочитаемый метод Предпочитаемый метод связи')

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name = 'Предпочитаемы метод связи'
		verbose_name_plural = 'Предпочитаемые методы связи'
		ordering = ('name',)

	def __str__(self):
		return f'{self.name}'


# Заявка
class Contact(models.Model):
	DESIRED_CONTACT_METHOD = [
		('email', 'E-mail',),
		('phone', 'Телефон',),
		# ('fb', 'Facebook',),
		('wapp', 'WhatsApp',),
		('teleg', 'Telegram',),
		# ('phone', 'Телефон',),
	]

	name = models.CharField(max_length=30, verbose_name='Имя')
	email = models.EmailField(verbose_name='E-mail')
	phone = models.CharField(max_length=13, blank=True, verbose_name='Phone')
	# desired_contact_method = models.ForeignKey(DesiredContactMethod,
	# on_delete=models.CASCADE, verbose_name='Предпочитаемый метод связи')
	desired_contact_method = models.CharField(
		max_length=10, choices=DESIRED_CONTACT_METHOD, default='email', verbose_name='Предпочитаемый метод связи')
	products = models.ForeignKey(
		ProductCategory, on_delete=models.CASCADE, verbose_name='Желаемый продукт')
	message = models.TextField(blank=True, verbose_name='Коментарий')

	status = models.ForeignKey(
		ContactStatus, on_delete=models.CASCADE, default=None, null=True, verbose_name='Статус заявки')
	session_key = models.CharField(max_length=130, default='')

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'
		ordering = ('name',)

	def __str__(self):
		return f'{self.name}'


class CompanyInfo(models.Model):
	name = models.CharField(max_length=30, verbose_name='Имя')
	email = models.EmailField(verbose_name='E-mail')
	phone = models.CharField(max_length=13, blank=True, verbose_name='Phone')

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'
		ordering = ('name',)

	def __str__(self):
		return f'{self.name}'


class Product(models.Model):
	name = models.CharField(max_length=40, verbose_name='Название')
	short_description = models.CharField(max_length=40, verbose_name="Краткое описание")
	slug = models.SlugField(verbose_name='Краткое название', help_text="Ссылка")
	category = models.ManyToManyField(ProductCategory, verbose_name="Категории продуктов")
	image = models.ImageField(upload_to='site_preview')
	url = models.URLField()

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
		ordering = ('name',)

	def __str__(self):
		return f'{self.name}'



