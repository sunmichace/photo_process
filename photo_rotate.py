# -*- coding:utf-8 -*-

import numpy
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "-image", required =True, help="path to input image file")
args = vars(ap.parse_args())

