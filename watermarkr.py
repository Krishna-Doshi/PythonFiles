import aspose.words as aw
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray
from PIL import Image
from pdf2image import convert_from_path

# doc=aw.Document("Input.pdf")

# for page in range(0, doc.page_count):
# 	extracted_page =doc.extract_pages(page,1)
# 	extracted_page.save(f"Output_{page +1}.jpg")
images = convert_from_path('Input.pdf')
for i in range(len(images)):
    images[i].save("Output_{page +1}.jpg", 'JPEG')
# image = Image.open("Output_2.jpg")
# print(image.dtype)
# print(image.shape)
pyplot.imshow(image)
pyplot.show()

# for x in list(range(200, 429)):
#     for y in list(range(660, 729)):
#         image.putpixel((x, y), (255, 255, 255))
#
# image.show()
# box= (200, 660, 429, 729)
# region= image.crop(box)
# print(region.getpixel())
# region.show()

# for x in list(range(image.width)):
# 	for y in list(range(image.height)):
# 		if region in image:
# 			image.putpixel((x,y), (255,255,255))

# image.show()
