import cv2
import numpy as np
from matplotlib import pyplot as plt
# ***** WCZYTANIE ZDJĘCIA *****
src = cv2.imread("zadanieBIN.png")
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# ***** METODA OPTYMALNEGO PROGOWANIA ***** 
hist,bins = np.histogram(gray.flatten(),256,[0,256])
t = 100
while True:
    tmp = t
    a=0
    b=0
    c=0
    d=0
    for i in range(0,int(t)):
        a = a + hist[i] *i
        b = b + hist[i]
    tcz = a/b
    for i in range(int(t)+1,256):
        c = c + hist[i] *i
        d = d + hist[i]
    tb = c/d
    t = ((tcz+tb)/2)
    if(tmp == t):
        break
ret,opt = cv2.threshold(gray,t,255,cv2.THRESH_BINARY)

# ***** METODA OTSU *****
ret1,otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ***** METODA ADAPTACYJNA *****
adapt = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# ***** WYSWIETLANIE *****

plt.subplot(2,2,1),plt.imshow(otsu,'gray')
plt.title('ORYGINAŁ'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.hist(otsu.flatten(),10,[0,256], color = 'r')
plt.title('HIST ORG')

plt.subplot(2,2,3),plt.imshow(adapt,'gray')
plt.title('PROGOWANIE'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.hist(adapt.flatten(),10,[0,256], color = 'r')
plt.title('HIST PROG')
plt.show()
cv2.waitKey(0)