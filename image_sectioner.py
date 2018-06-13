import numpy as np
import os
import cv2 as cv

def sectioner(img, section, folder):
    """This function designates which part is saved, and saves it to the assigned folder"""
    if section == '1':
        img = img[0:480,0:640]
    elif section == '2':
        img = img[0:480, 640:1280]
    elif section == '3':
        img = img[0:480, 1280:1920]
    elif section == '4':
        img = img[480:960, 0:640]
    elif section == '5':
        img = img[480:960, 640:1280]
    elif section == '6':
        img = img[480:960, 1280:1920]

    cv.imwrite(folder, img)

def line_drawer(img):
    cv.line(img, (0, 480), (1920, 480), (255, 0, 0), 3)
    cv.line(img, (640, 0), (640, 960), (255, 0, 0), 3)
    cv.line(img, (1280, 0), (1280, 960), (255, 0, 0), 3)
    return img

def main():
    print("""
            Sections
                1 - Top Left
                2 - Top Middle
                3 - Top Right
                4 - Bottom Left
                5 - Bottom Middle
                6 - Bottom Right
                """)
    section = None
    file_images = os.listdir('train_file')  # load the images as a list
    image_index = 0  # start from first image
    viable_strings = ['1', '2', '3', '4', '5', '6', 'None']  # display available options for input
    print("Press q to quit the program")
    input("\nPress Enter to begin")
    while (image_index < len(file_images))and (section != 'q'):
        img = cv.imread('train_file/'+file_images[image_index])
        img = img[60:1020, 0:1920]
        line_drawer(img)
        img = cv.resize(img, (1300, 650))
        cv.imshow(file_images[image_index], img)
        cv.waitKey(0)

        # if cv.waitKey(100) and 0xFF == 32:
        #     cv.destroyAllWindows()
        section = input("Which section is the part in?: ")
        img = cv.imread('train_file/'+file_images[image_index])
        img = img[60:1020, 0:1920]
        if section in viable_strings:
            if section == 'None':
                 pass
            else:
                folder = 'train_file_save/sectioned_'+file_images[image_index]
                sectioner(img, section, folder)
                cv.destroyAllWindows()
            image_index += 1

        elif section == 'q':
            break
        else:
            print("That is not a viable option")
    print("Exiting the program")



if __name__=='__main__':
    print("\nthis is a component program, not the main program")


