# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:35:34 2022

@author: GUSTAVO
"""

# desenfoque
from scipy import ndimage
from skimage import io
import matplotlib.pyplot as plt

img = io.imread("lena.jpeg")

# plt.imshow(img, cmap='gray')

blurred_img = ndimage.gaussian_filter(img, sigma=3)
# plt.imshow(blurred_img, cmap='gray')

masBorroso = ndimage.gaussian_filter(img, sigma=10)

filtroMedia = ndimage.uniform_filter(img, size=13)

plt.figure(figsize=(9, 3))
plt.subplot(141)
plt.title("imagen original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(142)
plt.title("imagen borrosa")
plt.imshow(blurred_img, cmap='gray')
plt.axis('off')

plt.subplot(143)
plt.title("imagen mas borrosa")
plt.imshow(masBorroso, cmap='gray')
plt.axis('off')

plt.subplot(144)
plt.title("imagen con mean")
plt.imshow(filtroMedia, cmap='gray')
plt.axis('off')

plt.subplots_adjust(wspace=0, hspace=0, top=2,
                    bottom=0.01, left=0.01,
                    right=0.99)