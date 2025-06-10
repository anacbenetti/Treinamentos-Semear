import numpy as np
import cv2

img = cv2.imread('/home/anabenetti/Semear_25/meuprojeto/filhote.jpg', -1)
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)

cv2.imwrite('filhote.jpg', img)

cv2.imshow('filhote', img)
cv2.waitKey(0)
cv2.destroyAllWindows()