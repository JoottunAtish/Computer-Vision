'''
## @File imageStitchDemo.py

Lab 7 - Image Stitching using Features (corners and edge) Detection

### @Function:
    - imageStitchDemo(dirName: str, sf: float)
'''

import cv2 as cv
import numpy as np
import os

def imageStitchDemo(dirName: str = "scottdale_left", sf: float = 0.4):
    '''
    Using openCV's Stitcher_create(), it stitches 2 or more images given their features (corners and edges).
    '''
    path = os.path.join("imgs", "stitch", dirName)

    if not os.path.isdir(path):
        print(f"Folder `{dirName}` does not exist in `imgs\stitch`.")
        return -1

    # Load and resize all images
    fileList = sorted([
        os.path.join(path, f) for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ])

    imgs = []
    for file in fileList:
        img = cv.imread(file)
        if img is None:
            print(f"Could not read {file}")
            continue
        img = cv.resize(img, None, fx=sf, fy=sf, interpolation=cv.INTER_LINEAR)
        imgs.append(img)

    if len(imgs) < 2:
        print("Need at least two valid images to stitch.")
        return -1

    # create a panorama stitcher 
    stitcher = cv.Stitcher_create(cv.Stitcher_PANORAMA)
    (status, stitched) = stitcher.stitch(imgs)

    if status != cv.Stitcher_OK:
        print(f"Stitching failed (error code: {status})")
        print("No common feature found.")
        cv.destroyAllWindows()
        return -1


    cv.imshow("Stitched Panorama", stitched)
    cv.waitKey(0)
    cv.destroyAllWindows()

# imageStitchDemo("scottdale_left")