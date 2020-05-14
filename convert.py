from PIL import Image
import os

image_size = (300, 300)

# covert every jpegs in the current directories into png format
for f in os.listdir('.'):  # specify your directory here
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))  # specify your directory here
