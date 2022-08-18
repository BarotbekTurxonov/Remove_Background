import cv2
import cvzone
# from cvzone.HandTrackingModule import HandDetector
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
segmentor = SelfiSegmentation()
imgBg = cv2.imread('images/3.jpg')

listImg = os.listdir('images')
print(listImg)

imgList = []
for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0


while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    
    print(indexImg)
    cv2.imshow('Removed_BG', imgStacked)
    # cv2.imshow('Original', img)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break






















# cap=cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# detector = HandDetector(detectionCon=0.8, maxHands=4)




# while True:
#     success, img = cap.read()
#     img = detector.findHands(img,draw=True)
#     cv2.imshow('handTrackingModule', img)


#     cv2.waitKey(1)















