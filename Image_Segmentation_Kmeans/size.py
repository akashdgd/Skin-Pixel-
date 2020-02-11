import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
import numpy as np


im =  cv2.imread('akash.jpg') #Reads an image into BGR Format

im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)


print(im.shape)
