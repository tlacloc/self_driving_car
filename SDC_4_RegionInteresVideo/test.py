import numpy as np
import cv2 as cv
import time


#Una vez abierto el video, es necesario presionar "q" para cerrarlo
video = cv.VideoCapture("videos/video_carretera.mp4")
while(video.isOpened()):
    ret, frame = video.read()
    alto= frame.shape[0]
    ancho= frame.shape[1]
    ratio=0.8
    frame =cv.resize(frame, ( int(ancho*ratio) , int(alto*ratio) ), interpolation=cv.INTER_NEAREST )
    time.sleep(0.002) #Variar la velocidad de reproducción del vídeo
    print(ret)
    if ret:
        cv.imshow("video original", frame)   
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
video.release()
cv.destroyAllWindows()
