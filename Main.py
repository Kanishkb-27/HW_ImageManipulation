import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("Cat.jpg")
image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap="gray")
plt.title("Gray Image")
plt.show()
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("grayscale_image.jpg", image_gray)
    print("Image saved as grayscale_image.jpg")
else:
    print("Image not saved")
cropped_image=image[100:300, 200:400]
cropped_rgb=cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("cropped_image.jpg", cropped_rgb)
    print("Image saved as cropped_image.jpg")
else:
    print("Image not saved")
(h,w)=image.shape[:2]
center=(w//2, h//2)
M=cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image=cv2.warpAffine(image, M, (w,h))
rotated_rgb=cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()
if key==ord("s"):
    cv2.imwrite("rotated_image.jpg", rotated_rgb)
    print("Image saved as rotated_image.jpg")
else:
    print("Image not saved")
brightness_matrix=np.ones(image.shape, dtype="uint8")*50
brighter_image=cv2.add(image, brightness_matrix)
brighter_rgb=cv2.cvtColor(brighter_image, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("brightened_image.jpg", brighter_rgb)
    print("Image saved as brightened_image.jpg")
else:
    print("Image not saved")