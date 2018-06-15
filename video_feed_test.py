import cv2 as cv
import sys
import numpy as np

def main():
    vid_stream = cv.VideoCapture(0)


    while True:
        ret, frame = vid_stream.read()
        cv.imshow('Video stream', frame)

        if cv.waitKey(1) and 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__=='__main__':
    print("\nthis is a component program, not the main program")