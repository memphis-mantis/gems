from PIL import Image

gem_path = 'quantum_gem_11.jpg'
file_path = 'every_day_is_a_gift_justin.jpg'


with Image.open(gem_path) as gem:
	with Image.open(file_path) as just_im:
		
		pix_val_gem = list(gem.getdata())
		pix_val_just = list(just_im.getdata())

		# create list of unique pixel values, from justin image
		pix_val_just_unique = list(dict.fromkeys(pix_val_just))


		n = 1
		pix_overlap = []
		for i in pix_val_just_unique:
			print("iteration: {}".format(n))
			if i in pix_val_gem:
				pix_overlap.append(i)
			n = n + 1

		print(pix_overlap)

		# # im.show()

		# # print total pixels
		# print("total_pixels_gem: {}".format(len(pix_val_gem)))
		# print("total_pixels_just: {}".format(len(pix_val_just)))

		# # print pixel format (image mode)
		# print("pixel_format: {}".format(gem.mode))
		# print("pixel_format: {}".format(just_im.mode))

