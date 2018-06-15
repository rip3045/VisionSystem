import image_sectioner
import video_capture
import video_feed_test
import pyueye_main
import video_capture_with_IDS

def main():
    user_input = None
    while user_input != '0':
        user_input = input("""
        
0 - Quit the program
1 - test video input feed
2 -test video input feed IDS camera
3 - capture images with webcam
4 - capture images with IDS camera
5 - section captured images
        
What would you like to do?""")

        if user_input == '0':
            pass
        elif user_input == '1':
            video_feed_test.main()
        elif user_input == '2':
            pyueye_main.main()
        elif user_input == '3':
            video_capture.main()
        elif user_input == '4':
            video_capture_with_IDS.main()
        elif user_input == '5':
            image_sectioner.main()
        else:
            print("\nthat is not a valid option")

    print("***Exiting main program***")

if __name__=="__main__":
    main()