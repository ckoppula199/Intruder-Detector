import cv2, time, pandas
from datetime import datetime

status_list = [None, None] # list requires 2 intitial values
times = []
dataframe = pandas.DataFrame(columns=["Face entered frame", "Face exited frame"])

# contains the data regarding recognising a face, front on
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# starts taking data from camera
video=cv2.VideoCapture(0) # if more than 1 camera is accessable increment the parameter until desired camera is obtained

first_frame = True
fr = 0
start = time.time()
while True:
    #increment frame rate counter
    fr+=1

    # reads current frame from camera
    check, frame = video.read()
    status = 0

    #obtain a grey version of the frame as it gives a higher accuracy
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # creates a list of co-ordinates and widhts and heights of faces seen in the image
    faces=face_cascade.detectMultiScale(grey,
    scaleFactor=1.05,
    minNeighbors=5)

    # adds a rectangle around the face to highlight that face was detected
    for x, y, width, height in faces:
        frame=cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 255, 0), 2)
        if first_frame:
            times.append(datetime.now())
            print("first_frame")
        status = 1
    first_frame = False

    status_list.append(status)

    #only need the last two values so shortens list to save memory
    status_list = status_list[-2:]

    # checks to see if a face has entered/exited the frame
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
        current_time = str(datetime.now())
        #replace certian chars to conform to image file name rules
        current_time = current_time.replace(".", "_")
        current_time = current_time.replace(" ", "_")
        current_time = current_time.replace(":", "_")
        cv2.imwrite("Intruder_Photos/" + current_time + ".jpeg", frame)
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    #displays current frame
    cv2.imshow("Capturing", frame)
    #cv2.imshow("Grey", grey)

    # if q is pressed then exit the loop and end the program
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break
end = time.time()


# calculates framerate
time_taken = end - start
minutes = time_taken / 60
frame_rate = fr/minutes/60
print("Framerate was " + str(frame_rate) + " frames per second")

# converts the data to a csv file that can be viewed in excel
for i in range(0, len(times), 2):
    dataframe = dataframe.append({"Face entered frame": times[i], "Face exited frame": times[i+1]}, ignore_index=True)
dataframe.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
