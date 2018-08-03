new_minimum_detection = input("What is the minimum confidence?: ")

with open('object_detection_webcam.py', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line[0:18] == '    min_detection_':
            line = '    min_detection_confidence = '+new_minimum_detection+'         ###EDITED BY SETTINGS PROGRAM###\n'
            print(line)

#for line in lines:
    #print(line, end='')