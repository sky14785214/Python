# -*- coding: utf-8 -*-
"""
Class definition of YOLO_v3 style detection model on image and video
"""

import colorsys
import os
from timeit import default_timer as timer

import numpy as np
from keras import backend as K
from keras.models import load_model
from keras.layers import Input
from PIL import Image, ImageFont, ImageDraw

from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from yolo3.utils import letterbox_image
import os
from keras.utils import multi_gpu_model
#--
import csv
import pytesseract
from PIL import Image
import cv2
import serial
import numpy as np

COM_PORT = 'COM3'    # 指定通訊埠名稱
BAUD_RATES = 115200    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠
label_test = []
Safenumber=["MPT3983","165BFE","BDC0771","2251WJ"]
code = ""
class YOLO(object):
    _defaults = {
        "model_path": 'logs/000/trained_weights_final.h5',
        "anchors_path": 'model_data/yolo_anchors.txt',
        "classes_path": 'model_data/my_class.txt',
        "score" : 0.3,
        "iou" : 0.3,
        "model_image_size" : (480, 480),
        "gpu_num" : 1,
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults) # set up default values
        self.__dict__.update(kwargs) # and update with user overrides
        self.class_names = self._get_class()
        self.anchors = self._get_anchors()
        self.sess = K.get_session()
        self.boxes, self.scores, self.classes = self.generate()

    def _get_class(self):
        classes_path = os.path.expanduser(self.classes_path)
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

    def _get_anchors(self):
        anchors_path = os.path.expanduser(self.anchors_path)
        with open(anchors_path) as f:
            anchors = f.readline()
        anchors = [float(x) for x in anchors.split(',')]
        return np.array(anchors).reshape(-1, 2)

    def generate(self):
        model_path = os.path.expanduser(self.model_path)
        assert model_path.endswith('.h5'), 'Keras model or weights must be a .h5 file.'

        # Load model, or construct model and load weights.
        num_anchors = len(self.anchors)
        num_classes = len(self.class_names)
        is_tiny_version = num_anchors==6 # default setting
        try:
            self.yolo_model = load_model(model_path, compile=False)
        except:
            self.yolo_model = tiny_yolo_body(Input(shape=(None,None,3)), num_anchors//2, num_classes) \
                if is_tiny_version else yolo_body(Input(shape=(None,None,3)), num_anchors//3, num_classes)
            self.yolo_model.load_weights(self.model_path) # make sure model, anchors and classes match
        else:
            assert self.yolo_model.layers[-1].output_shape[-1] == \
                num_anchors/len(self.yolo_model.output) * (num_classes + 5), \
                'Mismatch between model and given anchor and class sizes'

        # print('{} model, anchors, and classes loaded.'.format(model_path))

        # Generate colors for drawing bounding boxes.
        hsv_tuples = [(x / len(self.class_names), 1., 1.)
                      for x in range(len(self.class_names))]
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
        self.colors = list(
            map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
                self.colors))
        np.random.seed(10101)  # Fixed seed for consistent colors across runs.
        np.random.shuffle(self.colors)  # Shuffle colors to decorrelate adjacent classes.
        np.random.seed(None)  # Reset seed to default.

        # Generate output tensor targets for filtered bounding boxes.
        self.input_image_shape = K.placeholder(shape=(2, ))
        if self.gpu_num>=2:
            self.yolo_model = multi_gpu_model(self.yolo_model, gpus=self.gpu_num)
        boxes, scores, classes = yolo_eval(self.yolo_model.output, self.anchors,
                len(self.class_names), self.input_image_shape,
                score_threshold=self.score, iou_threshold=self.iou)
        return boxes, scores, classes

    def detect_image(self, image):
        start = timer()

        if self.model_image_size != (None, None):
            assert self.model_image_size[0]%32 == 0, 'Multiples of 32 required'
            assert self.model_image_size[1]%32 == 0, 'Multiples of 32 required'
            boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
        else:
            new_image_size = (image.width - (image.width % 32),
                              image.height - (image.height % 32))
            boxed_image = letterbox_image(image, new_image_size)
        image_data = np.array(boxed_image, dtype='float32')

        # print(image_data.shape)
        image_data /= 255.
        image_data = np.expand_dims(image_data, 0)  # Add batch dimension.

        out_boxes, out_scores, out_classes = self.sess.run(
            [self.boxes, self.scores, self.classes],
            feed_dict={
                self.yolo_model.input: image_data,
                self.input_image_shape: [image.size[1], image.size[0]],
                K.learning_phase(): 0
            })

        # print('Found {} boxes for {}'.format(len(out_boxes), 'img')) #辨識物件座標

        font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
                    size=np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))
        thickness = (image.size[0] + image.size[1]) // 300

        for i, c in reversed(list(enumerate(out_classes))):
            predicted_class = self.class_names[c]
            box = out_boxes[i]
            score = out_scores[i]

            label = '{} {:.2f}'.format(predicted_class, score)
            draw = ImageDraw.Draw(image)
            label_size = draw.textsize(label, font)

            top, left, bottom, right = box
            top = max(0, np.floor(top + 0.5).astype('int32'))
            left = max(0, np.floor(left + 0.5).astype('int32'))
            bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
            right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
            # print(label, (left, top), (right, bottom)) #辨識物件座標
            
            label_test.append(label)
            # print(label_test)
            # print(type(label))
            #-------------------
            
            with open('car_test.csv','a', newline='',encoding='utf-8') as car_csv: #紀錄用
                writer = csv.writer(car_csv)
                # data_0 = ('類別','左','上','右','下')
                writer.writerow(['類別','左','上','右','下'])
                # data_1 = (label,left,top,right,bottom)
                writer.writerow([label,left,top,right,bottom])
            with open('car_test_1.csv','w', newline='',encoding='utf-8') as car_csv_1: #實作讀取用
                writer0 = csv.writer(car_csv_1)
                writer0.writerow([label,left,top,right,bottom])


            # file = open('car_test.csv',mode = 'w') as car_csv:
            # file.write(label)
            # file.close()
            #-------------------
            if top - label_size[1] >= 0:
                text_origin = np.array([left, top - label_size[1]])
            else:
                text_origin = np.array([left, top + 1])

            # My kingdom for a good redistributable image drawing library.
            for i in range(thickness):
                draw.rectangle(
                    [left + i, top + i, right - i, bottom - i],
                    outline=self.colors[c])
            draw.rectangle(
                [tuple(text_origin), tuple(text_origin + label_size)],
                fill=self.colors[c])
            draw.text(text_origin, label, fill=(0, 0, 0), font=font)
            del draw

        end = timer()
        # print(end - start)  # 運行時間
        return image

    def close_session(self):
        self.sess.close()

def detect_video(yolo, video_path, output_path=""):
    import cv2
    vid = cv2.VideoCapture(video_path)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    video_FourCC    = int(vid.get(cv2.CAP_PROP_FOURCC))
    video_fps       = vid.get(cv2.CAP_PROP_FPS)
    video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    isOutput = True if output_path != "" else False
    if isOutput:
        print("!!! TYPE:", type(output_path), type(video_FourCC), type(video_fps), type(video_size))
        out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)
    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()
    while True:
        return_value, frame = vid.read()
        image = Image.fromarray(frame)
        image = yolo.detect_image(image)
        result = np.asarray(image)
        curr_time = timer()
        exec_time = curr_time - prev_time
        prev_time = curr_time
        accum_time = accum_time + exec_time
        curr_fps = curr_fps + 1
        if accum_time > 1:
            accum_time = accum_time - 1
            fps = "FPS: " + str(curr_fps)
            curr_fps = 0
        cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        if isOutput:
            out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    yolo.close_session()



def OCR_test(Image_card):
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
    # image = Image.open("1.png")

    Aimage = cv2.imread(Image_card)
    code = pytesseract.image_to_string(Aimage)
    car_card_number = pytesseract.image_to_string(Aimage)
    # print(car_card_number)
    code = code.replace(" ","");
    code = code.replace("-","");
    # print(type(code))
 
    # print(type(code))
    # print(code)
    return code
    
    


def segmentation(card_segmentation):
    # 1、讀取圖像，并把圖像轉換灰度像並顯示
    img = cv2.imread(card_segmentation)  # 讀取图片
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 轉换了灰階
    # cv2.imshow('gray', img_gray)  # 顯示圖片
    cv2.waitKey(0)
    
    # 2、將灰度圖像二值化，設定阈值是100
    img_thre = img_gray
    cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV, img_thre)
    # cv2.imshow('threshold', img_thre)
    cv2.waitKey(0)
    
    # 3、保存黑白圖片
    cv2.imwrite('thre_res.png', img_thre)
    
    # 4、分割字符
    white = []  # 紀錄每一列的白色像素總和
    black = []  # ..........黑色.......
    height = img_thre.shape[0]
    width = img_thre.shape[1]
    white_max = 0
    black_max = 0
    # 計算每一列的黑白色像素總和
    for i in range(width):
        s = 0  # 這一列白色總数
        t = 0  # 這一列黑色總数
        for j in range(height):
            if img_thre[j][i] == 255:
                s += 1
            if img_thre[j][i] == 0:
                t += 1
        white_max = max(white_max, s)
        black_max = max(black_max, t)
        white.append(s)
        black.append(t)
        # print(s)
        # print(t)
    
    arg = False  # False表示白底黑字；True表示黑底白字
    if black_max > white_max:
        arg = True
    
    # 分割圖像
    def find_end(start_):
        end_ = start_+1
        for m in range(start_+1, width-1):
            if (black[m] if arg else white[m]) > (0.85 * black_max if arg else 0.85 * white_max):  # 0.95这个参数请多调整，对应下面的0.05
                end_ = m
                break
        return end_
    
    n = 1
    start = 1
    end = 2
    while n < width-2:
        n += 1
        if (white[n] if arg else black[n]) > (0.15 * white_max if arg else 0.15 * black_max):
            # 上面這些判断用来辨别是白底黑字還是黑底白字
            # 0.05這個参数需要多調整，對應上面的0.95
            start = n
            end = find_end(start)
            n = end
            if end-start > 5:
                cj = img_thre[1:height, start:end]
                # cv2.imshow('caijian', cj)
                # cv2.imwrite("1.png",cj)

                cv2.waitKey(0)
    


def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 高斯平滑
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
	# 中值滤波
    median = cv2.medianBlur(gaussian, 5)
	# Sobel算子，X方向求梯度
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0, ksize = 3)
	# 二值化
    ret, binary = cv2.threshold(sobel, 140, 255, cv2.THRESH_BINARY)
	# 膨脹和侵蝕操作的核函数
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 6))
    
	# 膨脹一次，讓輪廓突出
    dilation = cv2.dilate(binary, element2, iterations = 1)
	# 侵蝕一次，去掉細節
    erosion = cv2.erode(dilation, element1, iterations = 1)
	# 再次膨脹，讓輪廓明顯一些
    dilation2 = cv2.dilate(erosion, element2,iterations = 1)
    # print(dilation2)
    # cv2.imshow('dilation2',dilation2)
    cv2.imwrite("dilation2.jpg",dilation2)
    cv2.waitKey(0)
    # return dilation2
    a = np.array(dilation2) # 二質化圖片
    b = np.where(a==255)

    test=[]
    test.append(b)
    # print(b)
    card_xy=[]
    for i in test:
        for a in i:
            # print(a)
            x_= min(a)
            y_= min(a)
            w_= max(a)
            h_= max(a)
            # print(x_)
            # print(y_)
            card_xy.append(x_)
            card_xy.append(y_)
            card_xy.append(w_)
            card_xy.append(h_)

            # print(card_xy)
    
    # print(test)
    img_test = img[card_xy[0]:card_xy[2],card_xy[4]:card_xy[6]]
    
    gray_img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("img_test.jpg",gray_img_test)
    
    


        



def test_new():
    try:
        image = Image.open(path_0)#camer_frame
    except:
        print('Open Error! Try again!')
    else:
        r_image= yolo.detect_image(image)

        r_image.show()
        
        # yolo.close_session()


        b = [v.split(' ')[0] for v in label_test]
        b = [''.join(b)]
       
        # print(b)
        car1 = "carc"
        moto1 = "moto"
        dcar1 = "dcar"

        # print(b)
        for i in b:
            # print(i[0:4])
            # print(i[-0:-4])
            # print(i[0:3])

            if i[0:4]  == moto1 :
                print("車種:機車")
                break
            elif i[-0:-4] == moto1 :
                print("車種:機車")
                break
            elif i[0:4] == car1 :
                print("車種:小客車")
            elif i[-0:-4] == dcar1 :
                print('車種:小客車')
            else:
                pass
            
        

        with open("car_test_1.csv",'r',encoding='UTF-8') as cartest_open:  #newline='' 是為了讓換行更可以被解析
            rows = csv.reader(cartest_open)
            
            for row in rows:
                # print(row)
                row_test = row[0]

                # print(row_test)
                
        OK_X = int(row[1]) -int(0)
        OK_y = int(row[2]) -int(0)
        OK_w = int(row[3]) +int(0)
        OK_h = int(row[4]) +int(0)
        # print(type(path_0))

        path_1 = cv2.imread("fps.jpg")

        ok_image = path_1[OK_y:OK_h, OK_X:OK_w]
        cv2.imwrite("rgb_card.png",ok_image)
        # print(path_1)

        Gray_ok_image = cv2.cvtColor(ok_image,cv2.COLOR_BGR2GRAY) #讀取鏡頭畫面並灰化

        ret,thresh_car_card = cv2.threshold(Gray_ok_image,100,255,cv2.THRESH_BINARY) #車牌切割後　二值化



        # cv2.imshow('ok_image',thresh_car_card)
        cv2.imwrite('car_card.png', thresh_car_card)   #輸出切割後車牌
        # cv2.waitKey(0)
        cap.release()

        
    
if __name__ == '__main__':
        
    # 打開yolo辨視 fps.jpg
    yolo=YOLO() 
    try:
        while True:
            data = ser.readline().decode("utf-8")
            if "\n" in data:
                cap = cv2.VideoCapture(0)
                ret,camer_frame = cap.read()
                # cv2.imshow('fps',camer_frame)
                # cv2.waitKey(0)

                cv2.imwrite('fps.jpg',camer_frame)
                cap.release()
                
                path_0 = r'fps.jpg'
                test_new()
                label_test = []

                imagePath = 'rgb_card.png'
                img = cv2.imread(imagePath)
                detect(img)
                card_segmentation = "img_test.jpg"
                segmentation(card_segmentation)
                Image_card = "thre_res.png"
                code = OCR_test(Image_card)
                print("車牌號碼:",code)                
                for i in Safenumber:
                    # print(i)
                    
                    # print(type(i))
                    if i == code:
                        print("安全車牌 開啟閘門")
                        ser.write(b"Servo_ON\n")
                        break
                    else:
                        # pass
                        # print("Flase")
                        ser.write(b"Servo_OFF\n")
                cv2.destroyAllWindows()
                cv2.waitKey(0)
                
    


    except KeyboardInterrupt:
        ser.close()    # 清除序列通訊物件
        cv2.destroyAllWindows()
        print('再見！')

# cap.release()








