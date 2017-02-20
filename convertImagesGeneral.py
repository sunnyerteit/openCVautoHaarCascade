# code used to split video file (terminal):
# avconv -i krone.mp4 -f image2 frame%00d.jpg
#
# documentation here:
# https://libav.org/avconv.html#image2-1
#
# import image library
from PIL import Image
import os
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

# this script requires you to put your images in a directory named yourprefix_vid
# in this case, the prefix is named empty, thus the directory has to be named empty_vid
prefix = 'empty'
if not os.path.exists(str(prefix) + '_img'):
        os.makedirs(str(prefix) + '_img')
if not os.path.exists(str(prefix) + '_vid'):
        os.makedirs(str(prefix) + '_vid')

def resize_images():
    for file_type in [str(prefix) + '_vid']:
        for img in os.listdir(file_type):
            current_image_path = str(file_type)+'/'+str(img)
            im = Image.open(current_image_path)

            # this part is not generalized. You have to consider the video resolution when dimensioning the following
            # line of code
            region = im.crop((0, (1920-1080)/2, 1080, (1920+1080)/2))
            region.save(str(prefix) + '_img/'+str(img))
            imgg = cv2.imread(str(prefix)+"_img/"+str(img), cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(imgg, (100, 100))
            cv2.imwrite(str(prefix)+"_img/"+str(img), resized_image)
resize_images()
