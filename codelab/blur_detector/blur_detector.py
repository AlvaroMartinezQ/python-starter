import os
import argparse
import cv2
import numpy as np
import shutil

from tqdm import tqdm
from time import sleep

# Location dir: ../../statics/imgs/
# Trash dir: ../../statics/trash/
# python3 blur_detector.py -if ../../statics/imgs/ -tf ../../statics/trash/

def blur_detector():
    ap = argparse.ArgumentParser()
    ap.add_argument("-if", "--image_folder", required=True, help="Folder where search should begin")
    ap.add_argument("-tf", "--trash_folder", required=True, help="Folder where trash images should end")
    ap.add_argument("-r", "--report", help="Store report operations in JSON file format. Use as: [name_of_your_file].json")
    args = ap.parse_args()
    img_folder = args.image_folder
    trash_folder = args.trash_folder
    arr = os.listdir(args.image_folder)
    for fil in tqdm(arr):
        sleep(1)
        if fil.endswith(('.png', '.jpg', '.jpeg')):
            search = img_folder + fil
            sourceimage = cv2.imread(search)
            res = is_blurred(sourceimage)
            if res[0] == True:
                folder_n_name = trash_folder + fil
                shutil.move(search, folder_n_name) #src, dst
            else:
                pass

def is_blurred (image, threshold=200):
    imagecv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    graycv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    edgescv = cv2.Laplacian(graycv, cv2.CV_64F)
    variance = edgescv.var()
    return (variance<threshold, variance)

if __name__ == '__main__':
    blur_detector()