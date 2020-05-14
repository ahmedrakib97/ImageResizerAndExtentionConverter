from PIL import Image
import glob

image_list = []
resized_images = []

for filename in glob.glob('ben_afflek/*.png'):
    print(filename)
    img = Image.open(filename)
    image_list.append(img)

for image in image_list:
    image = image.resize((300, 300))
    resized_images.append(image)

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('ben_afflek/resized/', i+1, '.png'))
