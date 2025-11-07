import cv2 as cv
import numpy as np
import os

def imageStitchDemo(dirName: str = "bryce_left", sf: float = 0.4):
    path = os.path.join("imgs", "stitch", dirName)

    if not os.path.isdir(path):
        print(f"Folder `{dirName}` does not exist in `imgs/stitch`.")
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

    # --- Use OpenCV’s built-in Stitcher (MUCH more reliable) ---
    print("Using OpenCV's built-in Stitcher for best results...")
    stitcher = cv.Stitcher_create(cv.Stitcher_PANORAMA)
    (status, stitched) = stitcher.stitch(imgs)

    if status != cv.Stitcher_OK:
        print(f"Stitching failed (error code: {status})")
        return -1

    # Optional crop to remove black borders
    gray = cv.cvtColor(stitched, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 1, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv.boundingRect(contours[0])
        stitched = stitched[y:y + h, x:x + w]

    cv.imshow("Stitched Panorama", stitched)
    cv.waitKey(0)
    cv.destroyAllWindows()
