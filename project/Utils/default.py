import os

path = "imgs"

def getImagesList():
    lab = []
    
    if os.path.isdir(path):
        for dir in os.listdir(path):
            if dir == "stitch":
                continue
            lab.append(os.listdir(os.path.join(path, dir)))
    return lab
            