from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread
from multiprocessing import Process
from threading import Thread
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

class saver_worker(Thread):
    def __int__(self, queue, maxframes):
        self.cpt = 0
        self.max_frames = max_frames
        self.img = None
        self.q = queue
        while self.cpt < self.max_frames:
            print("Items in the queue: ", q.size())
            if q.empty:
                time.sleep(0.1)
            else:
                img = output_q.get()
                cv.imshow('Image', img)
                cv.imwrite('train_file/image%041.jpg' %self.cpt, img)
                self.cpt += 1



# camera class to simplify uEye API access
print("**Opening input camera**")
cam = Camera(0)
cam.init()
cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
cam.set_aoi(0, 0, 1920, 1080)
cam.set_full_auto()
cam.alloc()
cam.capture_video()

thread = FrameThread(cam, q)
thread.setDaemon(True)
save_thread = saver_worker(q, max_frames)
thread.start()
save_thread.start()
save_thread.join()
save_thread.stop()

cam.stop_video()
cam.exit()
time2 = time.time()
total = time2-time1
print("Time to execute: ", total)
print("**Exiting the Camera**")

exit()