import cv2 as cv
import os
import sys


def main():
## initialize variables
    cpt = 0
    max_frames = int(input("How many pictures would you like? "))

    try:
        vid_stream = cv.VideoCapture(0)             #camera index
    except:
        print("Problem opening input stream")       #exception handling, user feedback
        sys.exit(1)

    fp = open('train_file/train.txt', 'w')
    while cpt < max_frames:
        ret, frame = vid_stream.read()              #read frame and return code
        if not ret:                                 #if code is bad exit
            sys.exit(1)
            print("Feed has value Nonetype")
        cv.imshow("test window", frame)             #show window image
        frame = cv.resize(frame, (640, 480))
        cv.imwrite('train_file/image%04i.jpg' %cpt, frame)  #write to designated folder
        cv.waitKey(5000)
        image = ("image%i " %cpt)
        fp.write(image)                             #write designation to a txt file
        cpt += 1
    cv.destroyAllWindows()
    fp.close()                                      #close all of the
    vid_stream.release()                            #open files


    input("\n\nPress the enter key to exit")

if __name__=='__main__':
    print("\nthis is a component program, not the main program")