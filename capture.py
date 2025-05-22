import cv2

video = cv2.VideoCapture(0) # Open the default camera
while True:
    ret, frame = video.read() # Read a frame from the camera, ret is a boolean indicating if the frame was read correctly and frame is the image
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame to grayscale
    if not ret:
        break # If there is no frame, break the loop
    cv2.imshow("Camera", gray) # Display the frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Wait for 'q' key to exit
        break
video.release() # Release the camera
cv2.destroyAllWindows() # Close all OpenCV windows
