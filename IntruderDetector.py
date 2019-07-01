import cv2, time

# contains the data regarding recognising a face front on
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# starts taking data from camera
video=cv2.VideoCapture(0) # if more than 1 camera is accessable increment the parameter until desired camera is obtained

fr = 1
start = time.time()
while True:
    # reads current frame from camera
    check, frame = video.read()

    #obtain a grey version of the frame as it gives a higher accuracy
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # creates a list of co-ordinates and widhts and heights of faces seen in the image
    faces=face_cascade.detectMultiScale(grey,
    scaleFactor=1.05,
    minNeighbors=5)
    # adds a rectangle around the face to highlight that face was detected
    for x, y, width, height in faces:
        frame=cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 255, 0), 2)

    #displays current frame
    cv2.imshow("Capturing", frame)
    #cv2.imshow("Grey", grey)

    # if q is pressed then exit the loop and end the program
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
end = time.time()

# calculates framerate
time_taken = end - start
minutes = time_taken / 60
frame_rate = fr/minutes/60
print("Framerate was " + str(frame_rate) + " frames per second")

video.release()
cv2.destroyAllWindows()
