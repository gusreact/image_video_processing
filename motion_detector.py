import cv2, pandas as pd
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[]
df=pd.DataFrame(columns=["Start", "End"]) # Create a DataFrame to store the start and end times of motion
video=cv2.VideoCapture(0) # Open the default camera

while True:
    check, frame=video.read()
    status=0 # Check if the contour is bigger than 100 x 100 pixels
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame to grayscale
    gray=cv2.GaussianBlur(gray, (21, 21), 0) # Apply Gaussian blur to the grayscale frame
    
    if first_frame is None:
        first_frame=gray # Set the first frame to the current frame
        continue
    
    delta_frame=cv2.absdiff(first_frame, gray) # Calculate the absolute difference between the first frame and the current frame
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # Apply binary thresholding to the delta frame
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) # Dilate the threshold frame to fill in holes
    
    (contours,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours in the threshold frame
    
    for contour in contours:
        if cv2.contourArea(contour) < 10000: # Ignore small contours than less than 100 x 100 pixels
            continue
        status=1 # Set status to 1 if a contour is found
        
        (x, y, w, h) = cv2.boundingRect(contour) # Get the bounding rectangle of the contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) # Draw a rectangle around the contour on the original frame
    
    status_list.append(status)
    status_list=status_list[-2:] # Keep only the last two status values
    
    if(status_list[-1] == 1 and status_list[-2] == 0): # If motion is detected
        times.append(datetime.now()) # Append the current time to the times list if motion is detected
    if(status_list[-1] == 0 and status_list[-2] == 1): # If motion is not detected
        times.append(datetime.now())
    
    cv2.imshow("Frame", frame) # Display the original frame
    cv2.imshow("Gray Frame", gray) # Display the delta frame
    cv2.imshow("Delta Frame", delta_frame) # Display the delta frame
    cv2.imshow("Threshold Frame", thresh_frame) # Display the threshold frame
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break # Exit the loop if 'q' is pressed

for i in range(0, len(times), 2): # Iterate through the times list in pairs
    df = pd.concat([df, pd.DataFrame([{"Start": times[i], "End": times[i + 1]}])], ignore_index=True)

df.to_csv("Times.csv") # Save the DataFrame to a CSV file
video.release() # Release the camera