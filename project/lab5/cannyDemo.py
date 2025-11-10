'''
## @File CannyDemo.py

Lab 5 - Canny edge detection

### @Functions:
    - cannydemo(fileName: str)
    - cannyVarVal(fileName: str)
    - autoCanny(fileName: str)
    - liveCameraCanny(sf:float)
'''

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def cannydemo(fileName: str = "plate.jpg"):
    img = cv.imread(f"imgs\lab5\{fileName}")
    edges = cv.Canny(img, 150, 225, L2gradient=False)
    plt.imshow(edges, cmap="gray")
    plt.show()


def cannyVarVal(fileName: str = "plate.jpg"):
    """
    @function : Canny Demo with variable Threshold using trackbar.
    """
    img = cv.imread(f"imgs\lab5\{fileName}")
    if img is None:
        print(f"Error: Could Not open image, {fileName}")

    windowName = "canny_edge"
    cv.namedWindow(windowName, cv.WINDOW_AUTOSIZE)

    cv.imshow("Original Image", img)

    ## Define trackbars
    cv.createTrackbar("minValue", windowName, 0, 500, empty)
    cv.createTrackbar("maxValue", windowName, 0, 500, empty)

    canny_edge = cv.Canny(img, 0, 0)

    while True:
        min_val = cv.getTrackbarPos("minValue", windowName)
        max_val = cv.getTrackbarPos("maxValue", windowName)

        canny_edge = cv.Canny(img, min_val, max_val)

        cv.imshow("Canny Edges", canny_edge)

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break


def autoCanny(fileName: str = "plate.jpg"):
    """
    Automatically detect the threshold value using wide threshold and tight threshold.
    """
    sigma = 0.1
    img = cv.imread(f"imgs\lab5\{fileName}")

    if img is None:
        print(f"Error: Could not read/Open image, {fileName}")
        exit(-1)
        
    h, w, _ = img.shape
    
    if (h> 1000 or w > 1000):
        img = cv.resize(img, None, fx=0.4, fy=0.5, interpolation=cv.INTER_LINEAR)

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img, (3, 3), 0)

    # Calc the wide and tight of the img
    wide = cv.Canny(img, 10, 200)
    tight = cv.Canny(img, 225, 250)

    # Auto detect the lower and upper threshold using the mean of the image.
    v = np.mean(img)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    auto = cv.Canny(img, lower, upper)

    cv.imshow("original", img)

    cv.imshow("Edges, wide | Tight | Auto", np.hstack([wide, tight, auto]))
    cv.waitKey(0)
    cv.destroyAllWindows()


def liveCameraCanny(sf: float = 0.5):
    '''
    Live capture canny with variable and auto canny.
    '''
    capture = cv.VideoCapture(0)
    
    sigma = 0.1

    windowName = "CannyTracker"
    cv.namedWindow(windowName)
    cv.createTrackbar("Min value", windowName, 0, 500, empty)
    cv.createTrackbar("Max value", windowName, 0, 500, empty)

    if not capture.isOpened():
        print("Error: Could not open video Stream!")
        exit(-1)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error: Could not read frame")
            exit(-1)

        frame = cv.resize(
            frame, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR
        )  # Resizing frame to 0.5 scale factor

        frame = cv.GaussianBlur(frame, (3, 3), 0)

        minVal = cv.getTrackbarPos("Min value", windowName)
        maxVal = cv.getTrackbarPos("Max value", windowName)
        
        frame_cpy = frame

        frame = cv.Canny(frame, minVal, maxVal) # Change with variables
        
        # Auto canny
        v = np.mean(frame_cpy)
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        auto = cv.Canny(frame_cpy, lower, upper)

        # cv.imshow("Live capture", frame)
        # cv.imshow("Live capture Auto-Canny", auto)
        cv.imshow("Live capture | Live capture Auto", np.hstack([frame, auto]))

        if cv.waitKey(1) & 0xFF == ord("q"):
            capture.release()
            cv.destroyAllWindows()
            break


## Empty callback for trackbar.
def empty(x):
    pass
