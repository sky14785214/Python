import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()

cv2.destroyAllwindows()

#-------------擷取當下畫面一幀

# vid = cv2.VideoCapture(0)
# if vid.isOpened():
#   print ("Connected....")
#   while True:
#     ret, frame = vid.read()
#     if ret:
#       cv2.imshow("image", frame)
#     else:
#       print ("Error aqcuiring the frame")
#       break
#     if cv2.waitKey(10) & 0xFF:
#       break
# else:
#   print ("Not Connected....")

# cv2.waitKey(0)
# vid.release()
# cv2.destroyAllWindows()

# -----------------------------