# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:59:28 2020

@author: Administrator
"""
from __future__ import division
#from color_Model import color_model
from imageai.Prediction.Custom import CustomImagePrediction
#from imageai.Prediction.Custom import CustomImagePrediction
#from PIL import Image
#import cv2 as cv


class Color(object):
        prediction = CustomImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath("./model_data/best_color.h5")
        prediction.setJsonPath("./model_data/color_class.json")
        prediction.loadModel(num_objects=2)

        def color_API(path):
            name=[]
            pro=[]
            predictions, probabilities = Color.prediction.predictImage(path, result_count=2)  
            for eachPrediction, eachProbability in zip(predictions, probabilities):
                    print(eachPrediction,':',eachProbability)
                    name.append(eachPrediction)
                    pro.append(eachProbability)
            if(pro[0]>pro[1]):
                    Name=name[0]
            else:
                    Name=name[1]
        #    print(Name)
            if(Name=='0'):
                return 0
            else:
                return 1

       


