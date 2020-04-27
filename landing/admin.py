from django.contrib import admin
from . import models


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = ['name',
					'slug',
					'is_active', ]
	prepopulated_fields = {"slug": ("name",)}


@admin.register(models.ContactStatus)
class ContactStatusAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'color_bootstrap',
		'is_active',
	]
	ordering = [
		'name',
		'color_bootstrap',
		'is_active',
	]


@admin.register(models.DesiredContactMethod)
class DesiredContactMethodAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'is_active',
	]
	ordering = [
		'name',
		'is_active',
	]


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'email',
		'phone',
		'products',
		'message',
		'is_active',
		'updated',
		'created',
	]
	ordering = [
		'name',
		'email',
		'phone',
		'products',
		'is_active',
		'updated',
		'created',
	]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'slug',
		'category',
		'image',
		'url',
		'is_active',
		'created',
	]


