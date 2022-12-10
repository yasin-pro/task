from datetime import datetime

from PIL import Image

from pathlib import Path

from .models import Images , ImagesGray

def grayscale(image_id):

	'''
		a function for convert orginal image to gray image
	'''

	BASE_DIR = Path(__file__).resolve().parent.parent

	get_image = Images.objects.get(id = image_id)

	# save absolute url image of original 
	absolute_path = f'{BASE_DIR}{get_image.image.url}'

	img_rgb = Image.open(absolute_path)

	img_gray = img_rgb.convert('L')

	# save absolute url image of converted
	absolute_path_of_save_new_image = f'{BASE_DIR}/media/gray-images/{datetime.now()}.jpg'

	img_gray.save(absolute_path_of_save_new_image)

	new_gray_image = ImagesGray.objects.create(image = absolute_path_of_save_new_image)

	# clean url (delete base dir in url)
	cleaned_url = str(new_gray_image.image.url).replace(f'{BASE_DIR}' , '')[6:]

	new_gray_image.image = cleaned_url
	
	new_gray_image.save()

	return str(new_gray_image.image)