#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:11:06 2019

@author: emad
"""
'''

import statistics as st
x = [3,1.5,4.5,6.75,2.25,5.75,2.25]
print (st.mean(x))
print (st.harmonic_mean(x))
print (st.median(x))
print (st.median_low(x))
print (st.median_high(x))
print (st.median_grouped(x))
print (st.mode(x))
print (st.pstdev(x))
print (st.Pvariance(x))
print (st.stdev(x))
print (st.variance(x))





import random
print( random.random() )
print(  random.randrange(10) )
print ( random.choice('ali',
'khalid','hussam') )
print ( random.sample(range(1000), 10) )

print ( random.choice('orange academe') )
items = [1, 5,8,9,2,4]
random.shuffle(items)
print( items )
print ( random.randint(20, 30) )
print ( random.randrange(1000, 2111, 5) )
print (( random.uniform(10000, 11000)))





import math
print ('pi: %.40f' % math.pi)
print ('e: %.40f' % math.e)
print ('arcsine(%.1f) = %5.2f' % (30,
math.asin(30)))
print ('arccosine(%.1f) = %5.2f' % (200,
math.acos(200)))
print ('arctangent(%.1f) = %5.2f' % (180,
math.atan(180)))
n = 100.7
print(math.floor(10.8))

print(math.ceil(10.8))

'''



from PIL import Image,ImageFilter,ImageDraw
im1=Image.open('emad.jpeg')
im2=Image.open('emad.jpeg').resize(im1.size)
im1.show()
print (im1.format , im1.size , im1.mode)
im1_filp=im1.transpose(Image.FLIP_TOP_BOTTOM)
im1_filp.show()
greyscale_image=im1.convert('L')
greyscale_image.show()
croppedImage=im1.crop((0,0,50,50))
croppedImage.show()
draw=ImageDraw.Draw(im1)
draw.line((0,0)+im1.size, fill = (225,225,225))
draw.line((0,im1.size[1], im1.size[0],0),fill=(225,225,225))
draw.text((im1.size[0]/2-im1.size[0]/2,im1.size[1]/2+20),'emad',fill=(225,225,0))
draw.text((im1.size[0]/2-im1.size[0]/2,im1.size[1]/2-60),'Image',fill=(225,225,0))
im1.show()
newImage2=im2.filter(ImageFilter.SHARPEN)
newImage2.show()
newImage2=im2.filter(ImageFilter.EDGE_ENHANCE)
newImage2.show()
newImage3=im2.filter(ImageFilter.FIND_EDGES)
newImage3.show()
newImage4=im2.filter(ImageFilter.SMOOTH)
newImage4.show()
Image.blend(im1,im2,0.5).save('images.jpeg'.format(0.5))
im=Image.open('images.jpeg')
im.show()
blurred=im1.filter(ImageFilter.BLUR)
im1.show()
size=(128,128)
saved="jordan.png"
try:im
except:print("Unable to load image")
im.thumbnail(size)
im.save(saved)
im.show()
im1_flip=im1.transpose(Image.ROTATE_90)
im1_flip.show()
mask=Image.open('mask.png')
mask=mask.resize(im1.size)
Image.composite(im1,im2,mask).save('maskimage.jpg')
imagMask=Image.open('maskimage.jpg')
imagMask.show()
































