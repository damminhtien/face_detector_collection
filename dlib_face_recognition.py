import cv2 as cv
import face_recognition
image = face_recognition.load_image_file('data/4/10102395343514191.jpg')

face_locations = face_recognition.face_locations(image)
print(face_locations)

for (top, right, bottom, left) in face_locations:
    cv.rectangle(
        image,
        (left, top),
        (right, bottom),
        (0, 255, 0),
        2
    )

cv.imshow('Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
