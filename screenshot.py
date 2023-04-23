import cv2

def cam_get():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow('huevis')

    img_counter = 0
    while True:
        # intializing the frame, ret
        ret, frame = cam.read()

        if not ret:
            print('failed to grab frame')
            break

        # the frame will show with the title of test
        cv2.imshow('huevis', frame)
        #to get continuous live video feed from my laptops webcam
        k  = cv2.waitKey(1)
        # if the escape key is been pressed, the app will stop
        if k%256 == 27:
            print('escape hit, closing the app')
            break
        
        # if the spacebar key is been pressed
        # screenshots will be taken
        elif k%256  == 32:
            # the format for storing the images scrreenshotted
            img_name = f'opencv_frame_{img_counter}.jpg'
            # saves the image as a png file
            cv2.imwrite(img_name, frame)
            print('screenshot taken')
            # the number of images automaticallly increases by 1
            img_counter += 1

    # release the camera
    cam.release()

    # stops the camera window
    cam.destoryAllWindows()
    

if __name__ == '__main__':
    cam_get()