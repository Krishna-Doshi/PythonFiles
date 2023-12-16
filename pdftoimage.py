from pdf2image import convert_from_path
from PIL import Image
images = convert_from_path('Input.pdf')
for i in range(len(images)):
   
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

image = Image.open("page0.jpg")
for x in list(range(471,862)):
	for y in list(range(1381,1480)):
		image.putpixel( (x,y), (255,255,255))

image.show()



