import cv2
import glob # It finds the path names of some files given a certain pattern

img = cv2.imread("galaxy.jpg",0)
print(type(img))
print(img)
print(img.shape) # The image resolution
print(img.ndim) # The number of dimensions
print(img.size) # The number of pixels

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) # Resize the image to 800x600
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resize.jpg", resized_img) # Save the resized image
cv2.waitKey(0) # Wait for a key press to close the window
cv2.destroyAllWindows()

images=glob.glob("sample_images/*.jpg") # Get all jpg files in the current directory

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) # Resize the image to 800x600
    cv2.imshow("Galaxy", re)
    cv2.waitKey(500) # Wait for a key half a second to close the window
    cv2.destroyAllWindows()
    print(image.split("\\")[-1])
    cv2.imwrite("sample_images/resize_"+image.split("\\")[-1], re) # Save the resized image
