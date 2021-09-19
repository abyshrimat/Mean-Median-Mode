import cv2
import dropbox
import time
import random

start_time = time.time()
 
def take_snapShot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + "png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
        return img_name
    print("snapshottaken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "wb0xkdh89xsAAAAAAAAAAUizxjY7Pj5RE5Y7m_XVDG52L7STulEkbwRtfD9pKMC4"
    file = img_name
    file_from = file
    file_to = "/testfolder/" + (img_name)

    dbx = dropbox.dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.file_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")



def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapShot()
            upload_file(name)

main()