import cv2

face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Convert the image to grayscale

faces=face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.1,
                                    minNeighbors=5,
                                    minSize=(30, 30)) # Detect faces in the image

for (x, y, w, h) in faces:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) # Draw rectangles around the detected faces

#resized_img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3))) # Resize the image to half its size

cv2.imshow("Gray", img) # Display the grayscale image
cv2.waitKey(0) # Wait for a key press to close the window
cv2.destroyAllWindows()