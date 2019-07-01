import cv2, time

# contains the data regarding recognising a face front on
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# starts taking data from camera
video=cv2.VideoCapture(0) # if more than 1 camera is accessable increment the parameter until desired camera is obtained

while True:
    # reads current frame from camera
    check, frame = video.read()

    #obtain a grey version of the frame as it gives a higher accuracy
    grey = cv2.cvtColor(frame, cv2.BGR2GRAY)

    #displays current frame
    cv2.imshow("Capturing", frame)
    cv2.imshow("Grey", grey)

    # if q is pressed then exit the loop and end the program
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
