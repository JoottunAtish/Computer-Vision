from project.lab4.Sobeldemo import *
from project.lab5.cannyDemo import *
from project.lab6.houghDemo import *
from project.lab7.CornerDetectionDemo import *
from project.lab7.imageStitchDemo import *

def main():
    
    ## Lab 4
    # sobelDemo(weight=0.4, ksize=1, path="imgs\lab4\house.jpg")
    # liveCameraSobel(sf=0.5)
    # liveCameraLapacian(sf=0.5)
    
    ## Lab 5
    # cannydemo()
    # cannyVarVal("carplate2.png")
    # autoCanny()
    # liveCameraCanny(0.3)
    
    ## Lab 6
    # HoughLineDemo("sudoku2.png")
    # print("Error") if liveCaptureHoughLine() == -1 else None
    
    # houghCircleDemo()
    # HoughCircleVarDemo("brown-eyes.jpg")
    
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


if __name__ == "__main__":
    main()
