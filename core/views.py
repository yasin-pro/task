from django.shortcuts import render , redirect

from django.contrib import messages

from .models import Images , ImagesGray

from .widget import grayscale

# Create your views here.



def index_view(request):

	'''
		a function for give pic
	'''

	if request.method == 'POST':

		user_image = request.FILES.get('user_image' , None)

		if user_image == None or user_image == '':

			messages.error(request , 'عکس خودتان را انتخاب کنید')

			return redirect('core:index')

		new_image = Images.objects.create(image = user_image)

		new_image.save()

		# save image uploaded id in session
		request.session['image_id'] = new_image.id

		return redirect('core:result')

	return render(request , 'core/index.html')




def result_view(request):

	'''
		a function for process on image
	'''

	try:

		image_id = int(request.session.get('image_id' , None))

	except:

		messages.error(request , 'اول عکس خود را آپلود کنید')

		return redirect('core:index')


	if image_id == '' or image_id == None:

		messages.error(request , 'اول عکس خود را آپلود کنید')

		return redirect('core:index')

	# get converted image...
	gray_image = grayscale(image_id)

	context = {

		'image' : ImagesGray.objects.get(image = gray_image)

	}

	return render(request , 'core/result.html' , context)