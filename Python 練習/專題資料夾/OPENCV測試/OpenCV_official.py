import cv2


cap = cv2.VideoCapture(0)

while(True):
    ret,camera_frame=cap.read()
   
    
    Gray_frame = cv2.cvtColor(camera_frame,cv2.COLOR_BGR2GRAY) #讀取鏡頭畫面並灰化
    
    
    # img_0 = cv2.Sobel(Gray_frame, cv2.CV_8U, 1, 0, ksize=3)
     #黑白兩值
    # ret,thresh_0 = cv2.threshold(img_0,230,255,cv2.THRESH_BINARY)
    # ret,thresh_1 = cv2.threshold(Gray_frame,230,255,cv2.THRESH_BINARY)

    # elemrnt_0 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,1))
    # element_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (8,6))

    # dilation_0 = cv2.dilate(thresh_0,element_1,iterations=1)
    # erosion = cv2.erode(dilation_0,elemrnt_0,iterations=1)
    # dilation_1 = cv2.dilate(erosion,element_1,iterations=1)

    # contours,hierarchy = cv2.findContours(thresh_0,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   

    # cv2.imshow("camera0",Gray_frame)
    cv2.imshow("camera0",camera_frame)
    # cv2.imshow("camera1",thresh_0)
    # cv2.imshow("camera2",thresh_1)
    # cv2.imshow("camera3",dilation_1)
    

    if cv2.waitKey(1) & 0xFF == ord("q"):  
        break
cap.release()
cv2.destroyAllwindows()