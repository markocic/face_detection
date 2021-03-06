import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


def detect_with_classifier(image, classifier):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    hits = classifier.detectMultiScale(gray_img,
                                       scaleFactor=1.1,
                                       minNeighbors=5)

    for x, y, w, h in hits:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    resized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))
    cv2.imshow("Image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_with_classifier("photo.jpg", eye_cascade)
