# Rainbow Cat GIF  🎉

## About the Project
I created an animated GIF of Rainbow Cat using Python and the ImageIO library! This project combines multiple images into a fun animation, bringing my favorite Nyan Cat to life. 🚀

## Technologies & Libraries Used
- ✅ Python 🐍
- ✅ ImageIO for handling GIF creation

What I Learned
✅ How to use ImageIO for image processing

✅ How to generate animated GIFs using Python

✅ Debugging issues like file paths, image formats, and array shape mismatches

Final Output (Rainbow Cat GIF🎥)
I had a blast working on this, and I’d love to hear your thoughts! Any feedback or suggestions are welcome. 🚀


## Code:
```python
import imageio.v3 as iio

cat_images = ['nyan-cat1.jpg', 'nyan-cat2.jpg', 'nyan-cat3.jpg']
images = []
for cat_image in cat_images:
    images.append(iio.imread(cat_image))

iio.imwrite('Rainbow Cat.gif', images, duration=200, loop=0) 
