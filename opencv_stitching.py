import numpy as np
import imutils
import cv2 as cv

class Stitcher(object):
    def __init__(self):
        #find opencv version number
        self.isv3 = imutils.is_cv3()

    def Stitch(self, images, ratio = 0.75, reprojThresh = 4.0, showMatches = False):
        #unpack the images, then detect keypoints and extract
        #local invariant descriptors from them
        (imageA, imageB) = images
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)

        #match features between the two images
        M = self.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)

        #if the match is none, then there aren't enough matched keypoints
        #to create a panorama
        if M = None:
            return None

        #otherwise perform a perspective warp to join the images
        (matches, H, status) = M
        result = cv.warpPerspective(imageA, H, (imageA.shape[1]+imageB.shape[1], imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]]-imageB

        #check to see if the matches should be visualized
        if showMatches:
            vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches, status)
            # return a tuple of the stitched image and the visualization
            return (result, vis)

        return result

    def detectAndDescribe(self, image):
        #convert the image to grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        #check the opencv version
        if self.isv3:
            #detect and extract features from the image
            descriptor = cv.xfeatures2d.SIFT_create()
            (kps, features) = descriptor.detectAndCompute(image, None)

        #otherwise we are using openCV 2.4.X
        else:
            #detect keypoints in the image
            detector = cv.FastFeatureDetector_create("SIFT")
















