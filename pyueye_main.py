#!/usr/bin/env python

from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread
from time import sleep

from multiprocessing import Queue, Pool
import cv2
import numpy as np

def main():

    #initialized variables
    cpt = 0
    max_frames = int(input("How many pictures would you like?: "))
    # camera class to simplify uEye API access
    cam = Camera()
    cam.init()
    cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
    cam.set_aoi(0,0, 1920, 1080)

    cam.alloc()
    cam.capture_video()


    # a thread that waits for new images and processes all connected views
    thread = FrameThread(cam)
    thread.start()
    while cpt < max_frames:

        cv2.imshow('image', thread.img)
        cv2.imwrite('train_file/image%04i.jpg' %cpt, thread.img)
        cv2.waitKey(2000)
        sleep(5)
        cpt += 1
    thread.stop()
    thread.join()

    cam.stop_video()
    cam.exit()

if __name__ == "__main__":
    main()


