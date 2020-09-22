# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:34:40 2020

@author: zhyf
E-mail:zhyfwcy@gmail.com

说明：
#                       draw = ImageDraw.Draw(image)
##                       print('new上下左右',top,bottom,left,right)
#                       draw.rectangle(
#                      [left , top , right, bottom ],
#                        outline=self.colors[c]
#                              )
#根据字典value排序：
#sorted(d.items(), key = lambda x:x[1])
#倒序
#sorted(d.items(), key = lambda x:x[1], reverse = True)   
#                       draw = ImageDraw.Draw(image)
##                       print('new上下左右',top,bottom,left,right)
#                       draw.rectangle(
#                      [left , top , right, bottom ],
#                        outline=self.colors[c]
#                              )
 #                       for i in range(left,right):#遍历所有长度的点
#                            for j in range(bottom,top):#遍历所有宽度的点
#                                 image.putpixel((i,j),(234,53,57,255))  
 
"""
import operator
import os
import math
import numpy as np
import colorsys
from PIL import Image
from keras import backend as K
from keras.models import load_model
from keras.layers import Input
import cv2 as cv
from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from yolo3.utils import letterbox_image
from keras.utils import multi_gpu_model
from PIL import ImageFont, ImageDraw

class YOLO(object):
    _defaults = {
        "model_path": 'model_data/yolo.h5',
        "anchors_path": 'model_data/yolo_anchors.txt',
        "classes_path": 'model_data/coco_classes.txt',
        "score" : 0.3,
        "iou" : 0.45,
        "model_image_size" : (416, 416),
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

#        print('{} model, anchors, and classes loaded.'.format(model_path))

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

    def detect_image(self,name,img):
        print('hello1')
#        image=image.resize((1200, 900), Image.BILINEAR)
        img=cv.resize(img,(1920, 1080))
#        print(name,img)
        image = Image.fromarray(cv.cvtColor(img,cv.COLOR_BGR2RGB))   
        if self.model_image_size != (None, None):
            assert self.model_image_size[0]%32 == 0, 'Multiples of 32 required'
            assert self.model_image_size[1]%32 == 0, 'Multiples of 32 required'
            boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
        else:
            new_image_size = (image.width - (image.width % 32),
                              image.height - (image.height % 32))
            boxed_image = letterbox_image(image, new_image_size)
        image_data = np.array(boxed_image, dtype='float32')
        image_data /= 255.
        image_data = np.expand_dims(image_data, 0)
        out_boxes, out_scores, out_classes = self.sess.run(
            [self.boxes, self.scores, self.classes],
            feed_dict={
                self.yolo_model.input: image_data,
                self.input_image_shape: [image.size[1], image.size[0]],
            })
        print('Found1 {} boxes for {}'.format(len(out_boxes),name))
        card_box=[]
        center_point=[]
        line_segment=[]
        new_index=[]
#        X_distanse=[]
        top, left, bottom, right = 0,1024,1024,0
        if(len(out_boxes)==0):
            return  3,-1,-1,0
        elif(len(out_boxes)>0):
             for i, c in reversed(list(enumerate(out_classes))):
                     predicted_class = self.class_names[c]
                     score = out_scores[i]
                     if(score>0.10):
                          box = out_boxes[i]
                          score = '{:.2f}'.format(score)
                          top, left, bottom, right = box
                          card_box.append(box)
                          top = max(0, np.floor(top + 0.5).astype('int32'))
                          left = max(0, np.floor(left + 0.5).astype('int32'))
                          bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
                          right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
                          print('new',predicted_class,score)
             print(name,'精度在10%以上的标签有',len(card_box),'个')
             print('上下左右',top,bottom,left,right)
             if(len(card_box)==4):
                       print('标准卡')
                       w=int((abs(out_boxes[1][3]-out_boxes[1][1])+abs(out_boxes[0][3]-out_boxes[0][1])
                       +abs(out_boxes[2][3]-out_boxes[2][1])+abs(out_boxes[3][3]-out_boxes[3][1]))/4)
                       h=int((abs(out_boxes[1][2]-out_boxes[1][0])+abs(out_boxes[0][2]-out_boxes[0][0])
                       +abs(out_boxes[2][2]-out_boxes[2][0])+abs(out_boxes[3][2]-out_boxes[3][0]))/4)
                       for n in range (len(card_box)):
                            y=int((card_box[n][0]+card_box[n][2])/2)
                            x=int((card_box[n][1]+card_box[n][3])/2)
                            point=(x,y)
                            line=int(math.sqrt(x*x+y*y))
                            line_segment.append(line)
                            center_point.append(point)
                            if(top<y):
                                 top=y
                            if(bottom>y):
                                 bottom=y
                            if(left>x):
                                 left=x
                            if(right<x):
                                 right=x
#                       print('卡的中心点到原点的距离',line_segment)          
#                       print('卡的中心点',center_point)
                       new_index=np.argsort(line_segment)
                       x1=center_point[new_index[2]][0]
                       y1=center_point[new_index[2]][1]
                       x2=center_point[new_index[3]][0]
                       y2=center_point[new_index[3]][1]   
                       if((x2-x1)==0):
                           rotate_angle=0
                       else:
                           rotate_angle= float(y2-y1)/(x2-x1)
                       left=int(left)-w
                       right=int(right)+w
                       bottom=int(bottom)-h
                       top=int(top)+h
                       if(left<0):
                            left=0
                       if(right>1920):
                            right=1920
                       if(bottom<0):
                            bottom=0
                       if(top>1080):
                            top=1080
#                       print('img',img)
                       print('img的尺寸：',img.shape)
                       cropped = img[bottom:top,left:right]
                       print('cropped的尺寸',cropped.shape)
                       cv.imwrite('./cropped.jpg',cropped)

                       shang=int(bottom-2.5*h)
                       if((shang)<0):
                           return  0,-1,cropped,rotate_angle
                       else:
                           if(shang<0):
                               shang=0
                           return  0,-1,cropped,rotate_angle

             elif(len(card_box)>0 and len(card_box)<4):
                 print(len(card_box))
                 return  5,-1,-1,0
             elif(len(card_box)>4 and len(card_box)<8 ):
                 return  4,-1,-1,0
             else:
                 return  5,-1,-1,0
        else:
#             print('没有存猪卡')
             return  7,-1,-1,0
    def detect_imageback(self,name,img):
        print('hello2')
        target_points=[]
        angle_points=[]
        angle_pointsdes=[]
        H=[]
        W=[]
        image = Image.fromarray(cv.cvtColor(img,cv.COLOR_BGR2RGB))
        cuting_img=img.copy()        
        
        if self.model_image_size != (None, None):
            assert self.model_image_size[0]%32 == 0, 'Multiples of 32 required'
            assert self.model_image_size[1]%32 == 0, 'Multiples of 32 required'
            boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
        else:
            new_image_size = (image.width - (image.width % 32),
                              image.height - (image.height % 32))
            boxed_image = letterbox_image(image, new_image_size)
        image_data = np.array(boxed_image, dtype='float32')
        font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
               size=np.floor(2e-2 * image.size[1] + 0.2).astype('int32'))
        thickness = (image.size[0] + image.size[1]) // 500
        image_data /= 255.
        image_data = np.expand_dims(image_data, 0)  # Add batch dimension.
        out_boxes, out_scores, out_classes = self.sess.run(
            [self.boxes, self.scores, self.classes],
            feed_dict={
                self.yolo_model.input: image_data,
                self.input_image_shape: [image.size[1], image.size[0]],
            })
#        print('Found {} boxes for {}'.format(len(out_boxes), '切割后的图片')) # 提示用于找到几个bbox
#开始创作
        top, left, bottom, right = 0,1024,1024,0
        card_box=[]
        center_point=[]
        if(len(out_boxes)>0 and len(out_boxes)<9 ):
            for i, c in reversed(list(enumerate(out_classes))):
#                     k=0
                     predicted_class = self.class_names[c]
                     score = out_scores[i]
                     if(score>0.10):
                          box = out_boxes[i]
                          label = '{} {:.2f}'.format(predicted_class, score)
                          score = '{:.2f}'.format(score)
                          top, left, bottom, right = box
                          card_box.append(box)
                          top = max(0, np.floor(top + 0.5).astype('int32'))
                          left = max(0, np.floor(left + 0.5).astype('int32'))
                          bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
                          right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
            if(len(card_box)>0 and len(card_box)<4):
                cv.imwrite('error.jpg',img)
                print('小于4精度不够')
                return 6,-1
            elif(len(card_box)==4):
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
                    if top - label_size[1] >= 0:
                        text_origin = np.array([left, top - label_size[1]])
                    else:
                        text_origin = np.array([left, top + 1])
                    for i in range(thickness):
                        draw.rectangle(
                            [left + i, top + i, right - i, bottom - i],
                            outline=self.colors[c])
                    draw.rectangle(
                        [tuple(text_origin), tuple(text_origin + label_size)],
                        fill=self.colors[c])
                    draw.text(text_origin, label, fill=(0, 0, 0), font=font)
                    del draw
                    top, left, bottom, right = box
                    top = max(0, np.floor(top + 0.5).astype('int32'))
                    left = max(0, np.floor(left + 0.5).astype('int32'))
                    h=int(abs(top-bottom)/2)
                    w=int(abs(left-right)/2)
                    bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
                    right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
                    centerPoint=[int((left+right)/2),int((top+bottom)/2)]
                    target_points.append(centerPoint)
                    H.append(h)
                    W.append(w)
                aera1=(target_points[0][0]*target_points[0][1])
                aera2=(target_points[1][0]*target_points[1][1])
                aera3=(target_points[2][0]*target_points[2][1])
                aera4=(target_points[3][0]*target_points[3][1])
                aera=[aera1,aera2,aera3,aera4]

                for i in range(len(aera)):
                    angle= math.asin(target_points[i][1]/math.sqrt(math.pow(target_points[i][0],2)+math.pow(target_points[i][1],2)))
                    angle=format(angle,'.3f')
                    angle_points.append(angle)
                arr =  np.array(angle_points)
                new_arr=np.argsort(arr)
                for i in range(len(new_arr)):
                    j=new_arr[i]
                    x=target_points[j][0]
                    x1=W[j]+5
                    y=target_points[j][1]
                    y1=H[j]+5
#缩放面积
                    if(i==0):
                        X=x+x1
                        Y=y-y1
                        angle_pointsdes.append([X,Y])
                    if(i==1):
                        X=x+x1
                        Y=y+y1
                        angle_pointsdes.append([X,Y])
                    if(i==2):
                        X=x-x1
                        Y=y-y1
                        angle_pointsdes.append([X,Y])
                    if(i==3):
                        X=x-x1
                        Y=y+y1
                        angle_pointsdes.append([X,Y])
                angle_pointsdes=np.float32(angle_pointsdes)
                four_points=np.float32([[1200,0],[1200,900],[0,0],[0,900]])
                M = cv.getPerspectiveTransform(np.array(angle_pointsdes), np.array(four_points))
                Rotated_img= cv.warpPerspective(cuting_img, M, (1200,900))
                return 0,Rotated_img
            else: 
                print('精度不够')
                return 6,-1
#            elif(len(card_box)==4):            
            
            
        else:
            print('未知错误')
            return 7,-1


