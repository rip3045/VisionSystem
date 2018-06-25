from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread

from multiprocessing import Queue, Pipe
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
parent_conn, child_conn = Pipe()
thread = FrameThread(cam, child_conn)
thread.start()
time.sleep(8)
cpt = 0

while True:
    #if input_q.qsize() == 0:
        #break
    #print("Items in Queue:", input_q.qsize())
    image = parent_conn.recv()
    cv.imshow('image', image)
    cv.waitKey(300)
    print("Image number:", cpt)
    #frame = output_q.get()
    time.sleep(1)
    cpt += 1

cv.destroyAllWindows()
thread.stop()