# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:59:28 2020

@author: Administrator
"""
from __future__ import division
from imageai.Prediction.Custom import CustomImagePrediction
from flask import Flask,request
import os
app = Flask(__name__)#创建一个服务，赋值给APP
@app.route('/color_api',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post
def color_API():
#    Path='./1'
        url=[]
        url = request.args.get('path')#使用request.args.get方式获取拼接的入参数据
#        fileList = os.listdir('./1')
#    print(url)
#    i=1
#    for fileName in fileList: 
      #遍历文件夹中所有文件
        name=[]
        pro=[]
#        n=len(fileList)
#        print('本次需要检测',n,'张照片')
#        k=n-i
#        print('还剩',k,'张待检测照片名称',fileName)
        prediction.loadModel(num_objects=2)
#      predictions, probabilities = prediction.predictImage(('./1/Cropped.jpg'),result_count=2)  
        predictions, probabilities = prediction.predictImage((url),result_count=2)  
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction,':',eachProbability)
            name.append(eachPrediction)
            pro.append(eachProbability)

#        i=i+1
        if(pro[0]>pro[1]):
            Name=name[0]
        else:
            Name=name[1]
        print(Name)
        url=[]
        return Name
#        if(Name=='0'):
#            img=cv.imread('./input/'+fileName)
#            cv.imwrite('./0/'+fileName,img)
#        else:
#            img=cv.imread('./input/'+fileName)
#            cv.imwrite('./1/'+fileName,img)
#            Name=name[1]
#    print('finish')
#    return 'ok'
if __name__ == '__main__':
    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("./model_data/best_color.h5")
    prediction.setJsonPath("./model_data/color_class.json")
    urls=[]
    app.run(
       host='0.0.0.0',
       port= 9999,
       )


