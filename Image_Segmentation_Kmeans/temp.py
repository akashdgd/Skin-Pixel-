import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
import numpy as np


im =  cv2.imread('elephant.jpg') #Reads an image into BGR Format

im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

all_pixels  = im.reshape((-1,3))
dominant_colors = 4

km = KMeans(n_clusters=dominant_colors)
km.fit(all_pixels)

centers = km.cluster_centers_
centers = np.array(centers,dtype='uint8')
#print(im.shape)

i = 1

#plt.figure(0,figsize=(8,2))


colors = []

for each_col in centers:
    plt.subplot(1,4,i)
    plt.axis("off")
    i+=1
    
    colors.append(each_col)
    
    #Color Swatch
    a = np.zeros((100,100,3),dtype='uint8')
    a[:,:,:] = each_col
    plt.imshow(a)
    
plt.show()

# size has to be entered manually


new_img = np.zeros((330*500,3),dtype='uint8')

print(new_img.shape)
for ix in range(new_img.shape[0]):
    new_img[ix] = 255

# for specific color extraction
for ix in range(new_img.shape[0]):
    if km.labels_[ix] == 2:
        new_img[ix] = colors[km.labels_[ix]]
    
    
new_img = new_img.reshape((im.shape))
plt.imshow(new_img)
plt.show()































