'''
## @File Sobeldemo.py

Lab 4 - Sobel Tranformation for Edge Detection


### @Functions:
    - sobelDemo(fileName: str, ksize: int, weight: int)
    - liveCameraSobel(sf: float)
    - liveCameraLapacian(sf: float)
'''

import cv2 as cv
import numpy as np


def sobelDemo(fileName: str = "Lena.jpg", ksize: int = 3, weight: int = 0.5):
    """
    By default it will use Lena image.
    """

    ## Reading and validating the Image.
    img = cv.imread(f"imgs\lab4\{fileName}")
    if img is None:
        print(f"Error reading image, `{fileName}`")
        return None

    cv.imshow("Default Image, Lena", img)

    ## Pre-Processing stage
    img = cv.GaussianBlur(img, (3, 3), 0)
    
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale image of Lena", img)

    ## Sobel Edge detection
    gradient_x = cv.Sobel(
        img,
        cv.CV_16S,
        1,
        0,
        ksize=ksize,
        scale=1,
        delta=0,
        borderType=cv.BORDER_DEFAULT,
    )
    gradient_y = cv.Sobel(
        img,
        cv.CV_16S,
        0,
        1,
        ksize=ksize,
        scale=1,
        delta=0,
        borderType=cv.BORDER_DEFAULT,
    )

    # Convert the gradient into an image for display.
    abs_grad_x = cv.convertScaleAbs(gradient_x)
    abs_grad_y = cv.convertScaleAbs(gradient_y)

    edgeImg = cv.addWeighted(abs_grad_x, weight, abs_grad_y, weight, 0)
    cv.imshow("edge detected, Lena", edgeImg)

    cv.waitKey(0)  # Wait for an input
    cv.destroyAllWindows()  # destroyes all windows after input is detected.


def liveCameraSobel(sf: float = 0.5):
    '''
    Live capture and sobel tranformation for real-time edge detection
    '''
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Could not open video stream!")
        exit(-1)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error: Could not read frame")
            exit(-1)

        # Pre-processing : resizing, blurring and grayscale tranformation.
        frame = cv.resize(
            frame, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR
        )  # resize the frame capture.
        frame_og = frame.copy()

        frame = cv.GaussianBlur(frame, (3, 3), 0)

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        eq_frame = cv.equalizeHist(gray_frame)

        # Sobel convolution
        sobelx = cv.Sobel(gray_frame, cv.CV_64F, 1, 0, ksize=3)  # Horizontal edges
        sobely = cv.Sobel(gray_frame, cv.CV_64F, 0, 1, ksize=3)  # Vertical edges

        # Combine both x and y sobel edge into a single image
        magnitude = np.sqrt(sobelx**2 + sobely**2)
        magnitude_norm = cv.normalize(magnitude, None, 0, 150, cv.NORM_MINMAX, cv.CV_8U)

        # Display
        cv.imshow("Original Frame", frame)
        cv.imshow("Equilised Frame", eq_frame)
        cv.imshow("Sobel Edge", magnitude_norm)

        if cv.waitKey(1) & 0xFF == ord("q"):
            capture.release()
            cv.destroyAllWindows()
            break


def liveCameraLapacian(sf: float = 0.5):
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Could not open video stream!")
        exit(-1)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error: Could not read frame")
            exit(-1)

        frame = cv.resize(
            frame, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR
        )  # resize the frame capture.

        frame = cv.GaussianBlur(frame, (3, 3), 0)

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_eq = cv.equalizeHist(gray_frame)
        
        laplacian = cv.Laplacian(frame_eq, cv.CV_64F, ksize=1)
        
        cv.imshow("Original", gray_frame)
        cv.imshow("equilised image", frame_eq)
        cv.imshow("Lacplacian", laplacian)
        
        if cv.waitKey(1) & 0xFF == ord("q"):
            capture.release()
            cv.destroyAllWindows()
            break
