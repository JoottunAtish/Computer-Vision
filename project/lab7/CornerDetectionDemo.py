'''
## @File CornerDetectionDemo.py

Lab 7 - Harris Corner Detection and Contour Detection

### @Function:
    - CornerDetectionDemo(fileName: str)
    - cornerDetectionVarDemo(fileName: str)
    - liveCaptureCornerDetection(sf: float)
    
    - harrisCornerDetectionDemo(fileName: str)
    - harrisCornerVarDemo(fileName: str)
    
    - contourDemo(fileName: str)
    - liveCaptureContours(sf: float)
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def cornerDetectionDemo(fileName: str = "furniture.jpg"):
    img = cv.imread(f"imgs\lab7\{fileName}")
    if img is None:
        print("ERROR: Could not read image!")
        return -1

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgGray = cv.medianBlur(imgGray, 5)

    corners = cv.goodFeaturesToTrack(imgGray, 150, 0.2, 5)
    corners = np.int64(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    cv.imshow("Original Image", img)

    cv.waitKey(0)
    cv.destroyAllWindows()


def cornerDetectionVarDemo(fileName: str = "furniture.jpg"):
    img = cv.imread(f"imgs\lab7\{fileName}")
    if img is None:
        print("Error: Could not read Image!")
        return -1

    windowName = "Corner Detection"
    cv.namedWindow(windowName, cv.WINDOW_FREERATIO)

    cv.createTrackbar("max corner", windowName, 150, 500, empty)
    cv.createTrackbar("quality level", windowName, 200, 500, empty)
    cv.createTrackbar("min distance", windowName, 5, 500, empty)

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgGray = cv.medianBlur(imgGray, 5)

    while True:
        img_cpy = img.copy()

        maxVal = cv.getTrackbarPos("max corner", windowName)
        qLevel = cv.getTrackbarPos("quality level", windowName) / 1000.0
        minDist = cv.getTrackbarPos("min distance", windowName)
        qLevel = max(qLevel, 0.01)

        corners = cv.goodFeaturesToTrack(imgGray, maxVal, qLevel, minDist)

        try:
            corners = np.int64(corners)
            for corner in corners:
                x, y = corner.ravel()
                cv.circle(img_cpy, (x, y), 4, (0, 0, 255), -1)
        except:
            pass

        cv.imshow("Original Image", np.hstack([img, img_cpy]))

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break


def liveCaptureCornerDetection(sf: float = 0.4):
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Could not open video stream!")
        return -1

    windowName = "Corner Detection"
    cv.namedWindow(windowName, cv.WINDOW_FREERATIO)

    cv.createTrackbar("max corner", windowName, 150, 500, empty)
    cv.createTrackbar("quality level", windowName, 200, 500, empty)
    cv.createTrackbar("min distance", windowName, 5, 500, empty)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error Could not read Frame!")
            return -1

        frame = cv.resize(frame, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR)

        og_frame = frame.copy()
        frame_corner = frame.copy()

        frame = cv.GaussianBlur(frame, (3, 3), 0)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        maxVal = cv.getTrackbarPos("max corner", windowName)
        qLevel = cv.getTrackbarPos("quality level", windowName) / 1000.0
        minDist = cv.getTrackbarPos("min distance", windowName)
        qLevel = max(qLevel, 0.01)

        corners = cv.goodFeaturesToTrack(frame, maxVal, qLevel, minDist)

        try:
            corners = np.int64(corners)
            for corner in corners:
                x, y = corner.ravel()
                cv.circle(
                    frame_corner, (x, y), 4, (0, 0, 255), -1
                )  # Draw circle on image given a cordinate and radius.
        except:
            pass

        cv.imshow("Original Image", np.hstack([og_frame, frame_corner]))

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break


def harrisCornerDetectionDemo(fileName: str = "chessboard.jpg"):
    
    img = cv.imread(f"imgs\lab7\{fileName}")
    
    img_cpy = img.copy()
    
    img_cpy = cv.cvtColor(img_cpy, cv.COLOR_BGR2GRAY)
    img_cpy = np.float32(img_cpy)

    img_corner = cv.cornerHarris(img_cpy, 2, 3, 0.04)
    
    img_corner = cv.dilate(img_corner, None)
    
    img[img_corner> 0.01*img_corner.max()] = [0, 0, 225]
    
    cv.imshow("Harris Corner Detection", img)

    cv.waitKey(0)
    cv.destroyAllWindows()


def harrisCornerVarDemo(fileName: str = "chessboard.jpg"):
    img = cv.imread(f"imgs\lab7\{fileName}")
    
    if img is None:
        print(f"Error: Could not read/open image, {fileName}")
        return -1
    
    namedWindow = "harris Corner"
    cv.namedWindow(namedWindow, cv.WINDOW_FREERATIO)
    
    cv.createTrackbar("block size", namedWindow, 2, 100, empty)
    cv.createTrackbar("ksize", namedWindow, 3, 100, empty)
    cv.createTrackbar("k", namedWindow, 4, 100, empty)
    
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    grayImg = np.float32(grayImg) 
    while True:
        b_size = cv.getTrackbarPos("block size", namedWindow)
        ksize = cv.getTrackbarPos("ksize", namedWindow)
        k = cv.getTrackbarPos("k", namedWindow) / 100
        img_cpy = img.copy()
        
        try:
            corners = cv.cornerHarris(grayImg, b_size, ksize, k) 
        
            corners = cv.dilate(corners, None)
            img_cpy[corners > 0.01 * corners.max()] = [0, 0, 225]
        except:
            pass
         
        cv.imshow("Harris Corner Detection", img_cpy)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break 


def contourDemo(fileName: str = "furniture.jpg"):
    img = cv.imread(f"imgs\lab7\{fileName}")
    if img is None:
        print(f"Error: Could not read/open Image, {fileName}")
        return -1

    windowName = "Contour Detector"
    cv.namedWindow(windowName, cv.WINDOW_AUTOSIZE)

    cv.createTrackbar("Min Thres", windowName, 50, 255, empty)
    cv.createTrackbar("Max Thres", windowName, 225, 255, empty)

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    while True:

        minVal = cv.getTrackbarPos("Min Thres", windowName)
        maxVal = cv.getTrackbarPos("Max Thres", windowName)
        ret, threshold = cv.threshold(imgGray, minVal, maxVal, cv.THRESH_BINARY_INV)

        (contours, hierarchy) = cv.findContours(
            threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        img_cpy = img.copy()

        cv.drawContours(img_cpy, contours, -1, (0, 0, 225), 2, cv.LINE_AA)

        cv.imshow(
            "contours", np.hstack([cv.cvtColor(threshold, cv.COLOR_GRAY2BGR), img_cpy])
        )
        # cv.imshow("Original", img)
        # cv.imshow("Threshold image", threshold)
        # cv.imshow("Contour Image", img_cpy)

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break


def liveCaptureContours(sf: float = 0.3):
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Could not open video stream!")
        return -1

    windowName = "Contour Detector"
    cv.namedWindow(windowName, cv.WINDOW_AUTOSIZE)

    cv.createTrackbar("Min Thres", windowName, 50, 255, empty)
    cv.createTrackbar("Max Thres", windowName, 225, 255, empty)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error Could not read Frame!")
            return -1

        frame = cv.resize(frame, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR)
        frame = cv.GaussianBlur(frame, (5, 5), 0)  # Using a mask of 5x5

        frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        minVal = cv.getTrackbarPos("Min Thres", windowName)
        maxVal = cv.getTrackbarPos("Max Thres", windowName)

        ret, threshold = cv.threshold(frameGray, minVal, maxVal, cv.THRESH_BINARY_INV)

        contours, hierarchy = cv.findContours(
            threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        cv.drawContours(frame, contours, -1, (0, 0, 225), 1, cv.LINE_AA)

        cv.imshow(
            "Live Capture contours",
            np.hstack([cv.cvtColor(threshold, cv.COLOR_GRAY2BGR), frame]),
        )

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break


 
def empty(x):
    pass
