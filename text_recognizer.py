import cv2
import easyocr
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
img = cv2.imread("signBoard.jpeg")

reader = easyocr.Reader(['en'],gpu=True)

threshold = 0.25
data = reader.readtext(img)
for i in data:
    bbox,text,confidence = i

    if confidence > threshold:
        cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
        cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_SIMPLEX,0.65,(100,150,255),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()