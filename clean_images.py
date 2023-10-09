from PIL import Image
import os
import glob

# We need to make sure the images dont exceed a certain size however not all images have the same channels. Some are RGBA (A-Alpha which is transperancy)
# some are RGB. We can convert them to PNG as PNG supports Alpha. Or we can do this and then save the images as a certain size.

# size_300 = (300,300) 

# for f in os.listdir('.'): # make sure you are in right directory
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f) # splits into filename and file extension

#         rgb_im = i.convert('RGB') # converts to RGB so same number of channels for all images

#         rgb_im.thumbnail(size_300)
#         rgb_im.save('../new_300/{}{}'.format(fn, fext)) # we get to keep it as jpg



# image1 = Image.open('images/d9263b63-92c5-4e0a-9a78-cdfc194543ca.jpg')
# image1.show()

