import cv2

#image /vid
#img = cv2.imread('car1.png')
video = cv2.VideoCapture('cycle.mp4')

#pre-trained data
car_data = cv2.CascadeClassifier('car.xml')
pedestrian_data = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:

    (read_successful, frame) = video.read()

    if read_successful:

        #conv to b/w
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break


    #detection and pedestrians
    car_coordinates = car_data.detectMultiScale(grayscaled_frame)
    pedestrian_coordinates = pedestrian_data.detectMultiScale(grayscaled_frame)

    #rectangles around detections of cars
    for (x,y,w,h) in car_coordinates:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),2)

    #rectangles around detections of pedestrians 
    for (x,y,w,h) in pedestrian_coordinates:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,255),2)


    #disp img with tracking
    cv2.imshow('Car Detection',frame)
    key = cv2.waitKey(1)
    # stop when Q is pressed 
    if key==81 or key==113:
        break


video.release()
cv2.destroyAllwindows()    


print("code completed")
