import cv2

#image/vid
img = cv2.imread('car1.png')


#pre-trained data
car_data = cv2.CascadeClassifier('car.xml')


#conv to b/w
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detection
car_coordinates = car_data.detectMultiScale(grayscaled_img)

for (x,y,w,h) in car_coordinates:
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),2)

print(car_coordinates)


#disp img with tracking
cv2.imshow('Car Image',img)
cv2.waitKey()
print("code completed")
