from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread

from multiprocessing import Queue
import time
import cv2 as cv

input_q = Queue(2)
output_q = Queue(2)
cam = Camera()
cam.init()
cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
cam.set_aoi(0, 0, 1920, 1080)

cam.alloc()
cam.capture_video()

thread = FrameThread(cam, input_q)
thread.start()
time.sleep(8)
cpt = 0
while True:
    if input_q.qsize() == 0:
        break
    print(input_q.qsize())
    image = input_q.get()
    #cv.imshow('image', image)
    cv.waitKey(300)
    print("Image number:", cpt)
    #frame = output_q.get()
    time.sleep(3)
    cpt += 1

cv.destroyAllWindows()
thread.stop()