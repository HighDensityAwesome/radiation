#!/usr/bin/env python
# -*- coding: utf-8 -*-
#check to see if need sys at all, or if it could be useful


import os, sys
import cv2

n = 1

#calibrate res to full HD (1600x1200)
os.system(‘./ov2650_capture -s 1600x1200’)

while(n < 5):
	os.system(‘./ov2640_capture -c %s’ % (n))
	
	print(‘Image ‘ + str(n) + ‘ taken’)

'''
Old placement of "import cv2
	import cv2
'''

#make directory to put all test data into
	os.system(‘mkdir ~/test_data’)

#move all test data into directory
	#os.system(‘mv ~/Quberider/*.jpg ~/test_data’)

#Move ONLY current n-value.jpg
	os.system(‘mv ~/Quberider/%s' %s (n) '.jpg ~/test_data’)

#check to see if need to change to (‘~/Quberider/%s.jpg’ %s (n) )
	im = cv2.imread(‘~/Quberider/%s’ %s (n) ‘.jpg')
	bnw = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	
	os.system(‘mkdir ~/test_data/greyscale’)

#again, check to see position of placeholder (%s)
	cv2.imwrite(‘~test_data/greyscale/%s’ %s (n) ‘greyscale.jpg’)

	n += 1
