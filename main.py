from project.lab4.Sobeldemo import *
from project.lab5.cannyDemo import *
from project.lab6.houghDemo import *
from project.lab7.CornerDetectionDemo import *
from project.lab7.imageStitchDemo import *

import os


def main():

    while True:
        MainMenuList()
        labChoice = input("Enter Your choice: ").lower()

        if labChoice == "1":
            print("Lab 4 Choosen")
            lab4Menu()

        elif labChoice == "2":
            print("Lab 5 Choosen")
            lab5Menu()

        elif labChoice == "3":
            print("Lab 6 Choose")
            lab6Menu()

        elif labChoice == "4":
            print("Lab 7 Choosen")
            lab7Menu()

        elif labChoice == "q":
            print("Exiting program...")
            break

        else:
            print("Invalid Input!!")

    ## Lab 4
    # sobelDemo(weight=0.3, ksize=1, fileName="house.jpg")
    # liveCameraSobel(sf=0.3)
    # liveCameraLapacian(sf=0.3)

    ## Lab 5
    # cannydemo()
    # cannyVarVal("carplate2.png")
    # autoCanny()
    # liveCameraCanny(0.3)

    ## Lab 6
    # houghLineDemo("sudoku2.png")
    # print("Error") if liveCaptureHoughLine(sf=0.3) == -1 else None

    # houghCircleDemo()
    # houghCircleVarDemo("brown-eyes.jpg")

    ## Lab 7
    # cornerDetectionDemo()
    # cornerDetectionVarDemo()
    # liveCaptureCornerDetection()

    # harrisCornerDetectionDemo("scissors.jpg")
    # harrisCornerVarDemo("pyramid.png")

    # contourDemo("ferrari-spider.jpg")
    # liveCaptureContours()

    # imageStitchDemo(dirName="sedona_left", sf=0.6)

    pass


## Menu List
def MainMenuList():
    clearTerminal()
    print(
        """
-----------------------------------------------------------------------
    Computer Vision Main Menu Lab 4 - 7
    
    Options:  
        1 - Sobel and Laplacian Demo                                                (Lab 4)
        2 - Canny Demo                                                              (Lab 5)
        3 - Hough Line and Circle Demo                                              (Lab 6)
        4 - Corner Detection, Harris Corner Detection and Image stitching Demo      (Lab 7)
        
        q - Quit Program
-----------------------------------------------------------------------
        """
    )


def lab4Menu():
    while True:
        clearTerminal()
        print(
            """
-----------------------------------------------------------------------
        Lab 4 - Sobel and laplacian demo
        
        Options:
            1 - Sobel Demo with Image (default Image `lena.jpg`)
            2 - Live Camera Sobel Demo
            3 - Live Camera Laplacian Demo
            
            q - Quit Lab 4 Demo 
-----------------------------------------------------------------------
            """
        )

        demoChoice = input("Enter Choice: ").lower()

        if demoChoice == "1":
            print("Sobel Demo with Image")

            img = getImgData("lab4")
            if img is None:
                sobelDemo()
            elif img == -1:
                continue
            else:
                sobelDemo(img)

        elif demoChoice == "2":
            print("Live Camera Sobel Demo")
            liveCameraSobel(sf=0.3)

        elif demoChoice == "3":
            print("Live Camera Laplacian Demo")
            liveCameraLaplacian(sf=0.3)

        elif demoChoice == "q":
            print("Exiting Lab 4 Demo...")
            break

        else:
            print("Invalid Input!!")


def lab5Menu():
    while True:
        clearTerminal()
        print(
            """
-----------------------------------------------------------------------
        Lab 5 -  Canny Edge Detection Demo

            Options:
            1 - Canny Demo (default image `plate.jpg`)
            2 - Canny with Variable Treshold Values Demo (default image `plate.jpg`)
            3 - Canny with Auto detection demo (default image, `plate.jpg`)
            4 - Live Camera Canny Demo
            
            q - Quit Lab 5 Demo
-----------------------------------------------------------------------
            """
        )

        demoChoice = input("Enter your choice: ").lower()

        if demoChoice == "1":
            print("Canny Demo with Image")

            img = getImgData("lab5")
            if img is None:
                cannydemo()
            elif img == -1:
                continue
            else:
                cannydemo(img)

        elif demoChoice == "2":
            print("Canny with Variable Threshold Demo")

            img = getImgData("lab5")
            if img is None:
                cannyVarVal()
            elif img == -1:
                continue
            else:
                cannyVarVal(img)

        elif demoChoice == "3":
            print("Canny with Auto detection Demo")

            img = getImgData("lab5")
            if img is None:
                autoCanny()
            elif img == -1:
                continue
            else:
                autoCanny(img)

        elif demoChoice == "4":
            print("Live Camera Canny Demo")
            liveCameraCanny(sf=0.3)

        elif demoChoice == "q":
            print("Exiting Lab 5 Demo...")
            break

        else:
            print("Invalid Input!!")


def lab6Menu():
    while True:
        clearTerminal()
        print(
            """
-----------------------------------------------------------------------
        Lab 6 - Hough tranformation Line and Circle Demo
        
        Options:
            1 - Hough Line demo (default image `sudoku1.png`)
            2 - Live Capture Hough Line demo
            3 - Hough Circle Demo (default image, `coin1.jpg`)
            4 - Hough Circle with Variable Threshold Demo (default image, `coin1.jpg`)
            
            q - Quit Lab 6 Demo
-----------------------------------------------------------------------
            """
        )

        demoChoice = input("Enter your choice: ").lower()

        if demoChoice == "1":
            print("Hough Line Demo with Image")

            img = getImgData("lab6")
            if img is None:
                houghLineDemo()
            elif img == -1:
                continue
            else:
                houghLineDemo(img)

        elif demoChoice == "2":
            print("Live Capture Hough Line Demo")
            print("Error") if liveCaptureHoughLine(sf=0.3) == -1 else None

        elif demoChoice == "3":
            print("Hough Circle Demo with Image")

            img = getImgData("lab6")
            if img is None:
                houghCircleDemo()
            elif img == -1:
                continue
            else:
                houghCircleDemo(img)

        elif demoChoice == "4":
            print("Hough Circle with Variable Threshold Demo")

            img = getImgData("lab6")
            if img is None:
                houghCircleVarDemo()
            elif img == -1:
                continue
            else:
                houghCircleVarDemo(img)

        elif demoChoice == "q":
            print("Exiting Lab 6 Demo...")
            break

        else:
            print("Invalid Input!!")


def lab7Menu():
    while True:
        clearTerminal()
        print(
            """
-----------------------------------------------------------------------
        Lab 7 - Default Corner Detection, harris Corner Detection and Contour Detection
        
        Options:
            1 - Corner Detection Demo (default image, `furniture.jpg`)
            2 - Coner Detection with Variable Threshold Values Demo (default image, `furniture.jpg`)
            3 - Live Capture Corner Detection
            
            4 - Harris Corner Detection Demo (default image, `chessboard.jpg`)
            5 - Harris Corner Detection with Variable Threshold Values Demo (default image, `chessboard.jpg`)
            
            6 - Contour Detection Demo (default image, `furniture.jpg`)
            7 - Live Capture Contours Demo
            
            q - Quit Lab 7 Demo
-----------------------------------------------------------------------
            """
        )

        demoChoice = input("Enter your choice: ").lower()

        if demoChoice == "1":
            print("Corner Detection Demo with Image")

            img = getImgData("lab7")
            if img is None:
                cornerDetectionDemo()
            elif img == -1:
                continue
            else:
                cornerDetectionDemo(img)

        elif demoChoice == "2":
            print("Corner Detection with Variable Threshold Demo")

            img = getImgData("lab7")
            if img is None:
                cornerDetectionVarDemo()
            elif img == -1:
                continue
            else:
                cornerDetectionVarDemo(img)

        elif demoChoice == "3":
            print("Live Capture Corner Detection Demo")
            liveCaptureCornerDetection()

        elif demoChoice == "4":
            print("Harris Corner Detection Demo with Image")

            img = getImgData("lab7")
            if img is None:
                harrisCornerDetectionDemo()
            elif img == -1:
                continue
            else:
                harrisCornerDetectionDemo(img)

        elif demoChoice == "5":
            print("Harris Corner Detection with Variable Threshold Demo")

            img = getImgData("lab7")
            if img is None:
                harrisCornerVarDemo()
            elif img == -1:
                continue
            else:
                harrisCornerVarDemo(img)

        elif demoChoice == "6":
            print("Contour Detection Demo with Image")

            img = getImgData("lab7")
            if img is None:
                contourDemo()
            elif img == -1:
                continue
            else:
                contourDemo(img)

        elif demoChoice == "7":
            print("Live Capture Contours Demo")
            liveCaptureContours()

        elif demoChoice == "q":
            print("Exiting Lab 7 Demo...")
            break

        else:
            print("Invalid Input!!")


def getImgData(dirName: str):
    if dirName is None:
        print(f"ERROR: Could not open/read dataset path for `{dirName}`")
        return None

    clearTerminal()

    imgList = os.listdir(os.path.join("imgs", dirName))

    # Diplay Menu
    print("------------------------------------------------------")
    print("\td - Use default image")
    print("\tq - Quit to previous menu\n")
    print("Image list:")
    count = 1
    for img in imgList:
        print(f"\t{count} - {img}")
        count += 1

    print("------------------------------------------------------")

    while True:
        imgChoice = input("Enter image of choice: ").lower()

        if imgChoice == "d" or imgChoice == "":
            return None

        if imgChoice == "q":
            return -1

        imgChoice = int(imgChoice)
        print(f"input choice: {imgChoice}, length of array: {len(imgList)}")
        if imgChoice <= len(imgList) and imgChoice > 0:
            return imgList[imgChoice - 1]
        else:
            print("Invalid choice...")


def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


## Main program

if __name__ == "__main__":
    main()
