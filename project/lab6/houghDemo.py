import cv2 as cv
import numpy as np
import math


def HoughLineDemo(fileName: str = "sudoku1.png"):
    img = cv.imread(f"imgs\lab6\{fileName}")

    if img is None:
        print(f"Error: Unable to open/read image, {fileName}")
        return None

    windowName = "Canny Value"

    cv.namedWindow(windowName, cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("Min value", windowName, 0, 500, empty)
    cv.createTrackbar("Max value", windowName, 0, 500, empty)

    ## Using Variable Canny Edge detection
    cannyEdge = cv.Canny(img, 0, 0)

    while True:
        minVal = cv.getTrackbarPos("Min value", windowName)
        maxVal = cv.getTrackbarPos("Max value", windowName)

        img = cv.GaussianBlur(img, (3, 3), 0)

        cannyEdge = cv.Canny(img, minVal, maxVal)

        cannyEdge_cpy = cannyEdge

        cannyEdge_cpy_col = cv.cvtColor(cannyEdge_cpy, cv.COLOR_GRAY2BGR)
        cannyEdge_cpy_Prob = np.copy(cannyEdge_cpy_col)

        lines = cv.HoughLines(
            cannyEdge_cpy,  # The edge Detected using Canny Detection
            1,  # Rho: The Resolution of Parameter r. We used a resolution of 1 pixel
            np.pi
            / 180,  # theta: The resolution of parameter θ in radian. We used 1 degrees (pi / 180 = 1 deg)
            150,  # Threshold: The number of intersection required to have a line.
            None,  # Lines: Is set to None
            0,  # srn
            0,  # stn
        )

        if lines is None:
            print("No Lines could be detected.")
            return -1

        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))

            cv.line(cannyEdge_cpy_col, pt1, pt2, (0, 0, 225), 1, cv.LINE_AA)

        linesProb = cv.HoughLinesP(cannyEdge_cpy, 1, np.pi / 180, 50, None, 50, 10)

        if linesProb is None:
            print("could not detect Line Probability!")
            return -1

        for i in range(0, len(linesProb)):
            l = linesProb[i][0]
            cv.line(
                cannyEdge_cpy_Prob,
                (l[0], l[1]),
                (l[2], l[3]),
                (0, 225, 0),
                1,
                cv.LINE_AA,
            )

        cv.imshow(f"Original Image, {fileName}", cannyEdge)
        cv.imshow("Standard Hough Line Transform", cannyEdge_cpy_col)
        cv.imshow("Probabilistic Hough Line Transform", cannyEdge_cpy_Prob)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    pass


def liveCaptureHoughLine(sf: float = 0.3):
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Could not open video Stream!")
        return -1

    windowName = "Canny Value"
    cv.namedWindow(windowName, cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("Min value", windowName, 0, 500, empty)
    cv.createTrackbar("Max value", windowName, 0, 500, empty)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error: Could not read frame")
            return -1

        ## Using Variable Canny Edge detection
        cannyEdge = cv.Canny(frame, 0, 0)

        minVal = cv.getTrackbarPos("Min value", windowName)
        maxVal = cv.getTrackbarPos("Max value", windowName)

        frame = cv.GaussianBlur(frame, (3, 3), 0)

        frame = cv.resize(
            frame, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR
        )  # Resizing frame to 0.5 scale factor

        cannyEdge = cv.Canny(frame, minVal, maxVal)

        cannyEdge_cpy = cannyEdge

        cannyEdge_cpy_col = cv.cvtColor(cannyEdge_cpy, cv.COLOR_GRAY2BGR)
        cannyEdge_cpy_Prob = np.copy(cannyEdge_cpy_col)

        lines = cv.HoughLines(
            cannyEdge_cpy,  # The edge Detected using Canny Detection
            1,  # Rho: The Resolution of Parameter r. We used a resolution of 1 pixel
            np.pi
            / 180,  # theta: The resolution of parameter θ in radian. We used 1 degrees (pi / 180 = 1 deg)
            150,  # Threshold: The number of intersection required to have a line.
            None,  # Lines: Is set to None
            0,  # srn
            0,  # stn
        )

        # if lines is None:
        #     print("No Lines could be detected.")
        #     return -1

        try:
            for i in range(0, len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))

                cv.line(cannyEdge_cpy_col, pt1, pt2, (0, 0, 225), 1, cv.LINE_AA)

            linesProb = cv.HoughLinesP(cannyEdge_cpy, 1, np.pi / 180, 50, None, 50, 10)
        except:
            pass  # If no line is detected do nothing

        # if linesProb is None:
        #     print("could not detect Line Probability!")
        #     return -1

        try:
            for i in range(0, len(linesProb)):
                l = linesProb[i][0]
                cv.line(
                    cannyEdge_cpy_Prob,  # img
                    (l[0], l[1]),  # Point 1
                    (l[2], l[3]),  # Point 2
                    (0, 225, 0),  # Colour
                    1,  # Line Thinkness
                    cv.LINE_AA,  # Line Type
                )
        except:
            pass  # If no line is detected do nothing

        cv.imshow(f"Original frames", cannyEdge)
        cv.imshow("Standard Hough Line Transform", cannyEdge_cpy_col)
        cv.imshow("Probabilistic Hough Line Transform", cannyEdge_cpy_Prob)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break


def houghCircleDemo(fileName: str = "coin1.jpg"):
    img = cv.imread(f"imgs\lab6\{fileName}")
    if img is None:
        print("ERROR: Could not open file")
        return -1

    img_cpy = img.copy()
    

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.medianBlur(img_gray, 7)

    circles = cv.HoughCircles(
        img_gray,
        cv.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=100,
        param2=38,
        minRadius=45,
        maxRadius=120
    )

    circles = np.uint16(np.around(circles))
    
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img, center, 1, (0, 100, 100), 2)
        # circle outline
        radius = i[2]
        cv.circle(img, center, radius, (255, 0, 255), 2)
        
        
    cv.imshow(f"Original image, {fileName}", img_cpy)
    cv.imshow(f"Hough Circle Detection", img)

    cv.waitKey(0)


def HoughCircleVarDemo(fileName: str = "coin1.jpg"):
    img = cv.imread(f"imgs\lab6\{fileName}")
    if img is None:
        print("ERROR: Could not open file")
        return -1
    
    windowName = "Hough variables"
    cv.namedWindow(windowName, cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("dp", windowName, 120, 200, empty)
    cv.createTrackbar("minDist", windowName, 100, 500, empty)
    cv.createTrackbar("param1", windowName, 100, 500, empty)
    cv.createTrackbar("param2", windowName, 38, 500, empty)
    cv.createTrackbar("minRadius", windowName, 45, 500, empty)
    cv.createTrackbar("maxRadius", windowName, 110, 500, empty)

    img_cpy = img.copy()
    img_cpy_1 = img.copy()

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.medianBlur(img_gray, 7)


    while True:
        
        dpVal = cv.getTrackbarPos("dp", windowName) / 100
        minDistVal = cv.getTrackbarPos("minDist", windowName)
        param1Val = cv.getTrackbarPos("param1", windowName)
        param2Val = cv.getTrackbarPos("param2", windowName)
        minRadiusVal = cv.getTrackbarPos("minRadius", windowName)
        maxRadiusVal = cv.getTrackbarPos("maxRadius", windowName)
        

        try:
            circles = cv.HoughCircles(
                img_gray,
                cv.HOUGH_GRADIENT,
                dp=dpVal,
                minDist=minDistVal,
                param1=param1Val,
                param2=param2Val,
                minRadius=minRadiusVal,
                maxRadius=maxRadiusVal
            )

            circles = np.uint16(np.around(circles))
            img_cpy_1 = img.copy()
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv.circle(img_cpy_1, center, 1, (0, 100, 100), 2)
                # circle outline
                radius = i[2]
                cv.circle(img_cpy_1, center, radius, (255, 0, 255), 2)
        except:
            pass
            
            
        cv.imshow(f"Original image, {fileName}", img_cpy)
        cv.imshow(f"Hough Circle Detection", img_cpy_1 )
        
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
        
        
        
# Dummy Modules
def empty(x):
    pass
