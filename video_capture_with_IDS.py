#!/usr/bin/env python

from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread
from multiprocessing import Pipe
import time

import cv2 as cv



def main():
    parent_conn, child_conn = Pipe()
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
    thread = FrameThread(cam, child_conn)

    thread.start()
    while cpt < max_frames:
        img = parent_conn.recv()
        cv.imshow("Image", img)
        cv.waitKey(200)
        cv.imwrite('train_file/image%04i.jpg' %cpt, img)
        print("image captured")
        #print(input_q.qsize())

        time.sleep(5)
        cpt += 1

    #time.sleep(10)

    thread.stop()
    #thread.join()

    cam.stop_video()
    cam.exit()
    print("Exiting the program")

if __name__ == "__main__":
    #print("\nthis is a component program, not the main program")
    main()