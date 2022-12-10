from django.db import models

from django_jalali.db import models as jmodels

# Create your models here.

class Images(models.Model):

	'''
		a model for save images in db
	'''

	image = models.ImageField(upload_to = 'images/')

	created_date = models.DateTimeField(auto_now_add = True)

	updated_date = models.DateTimeField(auto_now = True)

	created_date_jalali = jmodels.jDateField(auto_now_add = True , blank = True , null = True)

	updated_date_jalali = jmodels.jDateField(auto_now = True , blank = True , null = True)

	# Methods
	def __str__(self):

		return str(self.id)

	# META
	class Meta:

		ordering = ['-created_date']

class ImagesGray(models.Model):

	'''
		a model for save images converted to gray in db
	'''

	image = models.ImageField(upload_to = 'gray-images/')

	created_date = models.DateTimeField(auto_now_add = True)

	updated_date = models.DateTimeField(auto_now = True)

	created_date_jalali = jmodels.jDateField(auto_now_add = True , blank = True , null = True)

	updated_date_jalali = jmodels.jDateField(auto_now = True , blank = True , null = True)

	# Methods
	def __str__(self):

		return str(self.id)

	# META
	class Meta:

		ordering = ['-created_date']