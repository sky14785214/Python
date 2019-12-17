import cv2
import numpy as np
from PIL import Image
import os.path
# from skimage import io,data 

def stretch(img):
    maxi = float(img.max())
    mini = float(img.min())
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i,j] = ((255/(maxi-mini)*img[i,j])-(255*mini)/(maxi-mini))
            return

def dobinaryzation(img):
    maxi = float(img.max())
    mini = float(img.min())
    x=maxi - ((maxi-mini)/2)
    ret,thresh = cv2.threshold(img,x,255,cv2.THRESH_BINARY)
    return thresh

def find_rectangle(contour):
    y,x=[],[]
    for p in contour:
        y.append(p[0][0])
        x.append(p[0][1])
    return  [min(y),min(x),max(y),max(x)]
    maxweight,maxindex=0,-1
    for i in range(len(block)):
        b=afterimg[block[i][0][1]:block[i][0][3],block[i][0][0]:block[i][0][2]]
        hsv = cv2.cvtColor(b,cv2.COLOR_RGB2HSV)
        lower = np.array([100,50,50])
        upper = np.array([140,255,255])
        mask = cv2.inRange(hsv,lower,upper)
        w1=0
        for m in mask:
            w1+=m/255
        w2=0
        for n in w1:
            w2+=n
        if w2>maxindex:
            maxindex=i
            maxweight=w2
    return block[maxindex[0]]

def locate_license(img,afterimg):
    img,contuurs,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    block=[]
    for c in contuurs:
        r =find_rectangle(c)
        a=(r[2]-r[0])*(r[3]-r[1])
        s=(r[2]-r[0])*(r[3]-r[1])
        block.append([r,a,s])
    block = sorted(block,key=lambda b: b[1])[-3:]

def find_license(img):
    m= 400*img.shape[0]/img.shape[1]
    img = cv2.resize(img,(400,int(m)),interpolation=cv2.INTER_CUBIC)
    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    stretchedimg = stretch(gray_img)

    r=16
    h=w=r*2+1
    kernel = np.zeros((h,w),np.uint8)
    cv2.circle(kernel,(r,r),r,1,-1)

    openingimg = cv2.morphologyEx(stretchedimg,cv2.MORPH_OPEN, kernel)
    strtimg = cv2.absdiff(stretchedimg,openingimg)

    binaryimg = dobinaryzation(strtimg)

    canny = cv2.Canny(binaryimg,binaryimg.shape[0],binaryimg.shape[1])

    kernel = np.ones((5,19),np.uint8)
    closingimg = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

    openingimg = cv2.morphologyEx(closingimg,cv2.MORPH_CLOSE,kernel)

    kernel = np.ones((11,5),np.uint8)
    openingimg = cv2.morphologyEx(openingimg,cv2.MORPH_OPEN,kernel)

    rect = locate_license(openingimg,img)

    return rect,img
def cut_license(afterimg,rect):
    rect[2]=rect[2]-rect[0]
    rect[3]=rect[3]-rect[1]
    rect_copy=tuple(rect.copy())
    rect = [0,0,0,0]

    mask=np.zeros(afterimg.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdMOdel = np.zeros((11,65),np.float64)
    cv2.grabCut(afterimg,mask,rect_copy,bgdModel,fgdMOdel,5,cv2.GC_INIT_WITH_RECT)
    mask2= np.where((mask==2)|(mask==0),0,1).astype('uint8')
    
    img_show =afterimg*mask2[:,:,np.newaxis]
    return img_show

def deal_license(licenseimg):
    gray_img = cv2.cvtColor(licenseimg,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3,3),np.float32)/9
    gray_img=cv2.filter2D(gray_img,-1,kernel)

    ret,thresh = cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY)
    return thresh

def find_end(start,arg,black,white,width,black_max,white_max):
    end = start + 1
    for m in range(start+1,width-1):
        if (block[m] if arg else white[m])>(0.98*black_max if arg else 0.98*white_max):
            end = m
            break
    return end






if __name__=='__main__':
    img = cv2.imread(r"C:/Users/sky14/Desktop/GitHub/keras-yolo3-master/rgb_card.png",cv2.IMREAD_COLOR)
    rect,afterimg = find_license(img)
    cv2.rectangle(afterimg,rect)
    cv2.imshow("afterimg",afterimg)

    cutimg = cut_license(afterimg,rect)
    cv2.imshow('cutimg',cutimg)

    
    thresh=deal_license(cutimg)
    cv2.imshow('thresh',thresh)
    cv2.waitKey(0)

    white=[]
    black=[]
    height=thresh.shape[0]
    width=thresh.shape[1]


    white_max = 0
    black_max = 0
    for i in range(width):
        line_white = 0
        line_black = 0
        for j in range(height):
            if thresh[j][i]==255:
                line_white+=1
            if thresh[j][i]==0:
                line_black+=1
        white_max = max(white_max,line_white)
        black_max = max(black_max,line_black)
        white.append(line_white)
        black.append(line_black)
        print("white",white)
        prinr('black',black)
    
    arg=True
    if black_max<white_max:
        arg=False
    
    n=1
    start=1
    end=2
    s_width=28
    s_height=28
    while n<width-2:
        n+=1
        if(white[n] if arg else black[n])>(0.02*white_max if arg else 0.02*black_max):
            start = n
            end = find_end(start,arg,block,white,black_max,white_max)
            n=end
        if end-start > 5:
            cj = img_thre[1:height, start:end]

        print("result/%s.jpg" % (n))
        infile = "result%s.jpg" %(n)
        io.imsave(infile,cj)

        cv2.imshow('cutlicense',cj)







    cv2.waitKey(0)
    cv2.destroyAllWindows()