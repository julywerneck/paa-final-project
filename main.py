import numpy as np
import cv2

window = 'Window'

my_img = np.zeros((400, 800, 3), dtype="uint8")
pts = np.array([[100, 70], [200, 300], [700, 200], [500, 100]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(my_img, [pts], True, (0, 255, 255))


cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)
cv2.moveWindow(window, 0, 0)
cv2.setWindowProperty(window, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_GUI_EXPANDED)
cv2.imshow(window, my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()