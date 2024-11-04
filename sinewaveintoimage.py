import cv2
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(256)
y=np.sin(2*np.pi*x/30)
y+=max(y)
img=np.array([[y[j]*127 for j in range(256) for i in range(256)]], dtype=np.uint8)
plt.imshow(img)
dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum=20*np.log((cv2.magnitude(dft_shift[:,:,0]), (dft_shift[:,:,0]))+1)
fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('imputimage')
ax2=fig.add_subplot(2,2,2)
ax2.imshow(img)
ax2.title.set_text('FFT')
