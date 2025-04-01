import imageio.v3 as iio
cat_images = ['nyan-cat1.jpg', 'nyan-cat2.jpg', 'nyan-cat3.jpg']
images = []
for cat_image in cat_images:
    images.append(iio.imread(cat_image))

iio.imwrite('Rainbow Cat.gif', images, duration = 200, loop = 0)