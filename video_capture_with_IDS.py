from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread
from multiprocessing import Process
import time
from queue import Queue
import cv2 as cv
import numpy as np

# initialize all variables
max_frames = int(input("how many pictures would you like?: "))

time1 = time.time()
#filepath = None
input_q = Queue()
output_q = Queue()

def saver_worker(output_q, max_frames):
    cpt = 0
    while cpt < max_frames:
        while output__q.empty() == True:
            time.sleep(0.1)
        img = output_q.get()
        cv.imshow('Frame', img)
        cv.imwrite('train_file/image%04i.jpg' %cpt, img)
        cpt += 1

def move_from_one_to_the_other(input_q, output_q):
    while True:
        if not input_q.empty():
            img = input_q.get()
            output_q.put(img)
        else:
            time.sleep(0.1)

# camera class to simplify uEye API access
print("**Opening input camera**")
cam = Camera(0)
cam.init()
cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
cam.set_aoi(0, 0, 1920, 1080)
cam.alloc()
cam.capture_video()

thread = FrameThread(cam, input_q)
thread.setDaemon(True)

t = Process(None, target=saver_worker, args=(output_q, max_frames,))
t.start()
move_from_one_to_the_other()





print("Items in the queue =", q.qsize())
t.join()
t.stop()

cam.stop_video()
cam.exit()
time2 = time.time()
total = time2-time1
print("Time to execute: ", total)
print("**Exiting the Camera**")

exit()

