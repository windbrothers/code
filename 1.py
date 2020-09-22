#from __future__ import division
#from color_Model import color_model
from imageai.Prediction.Custom import CustomImagePrediction
import os
from timeit import default_timer as timer

class Color(object):
        prediction = CustomImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath("./model_data/best_color.h5")
        prediction.setJsonPath("./model_data/color_class.json")
        prediction.loadModel(num_objects=2)

        def color_API(path):
#            name=[]
#            pro=[]
#            predictions, probabilities = Color.prediction.predictImage(path, result_count=2)  
#            for eachPrediction, eachProbability in zip(predictions, probabilities):
#                    print(eachPrediction,':',eachProbability)
#                    name.append(eachPrediction)
#                    pro.append(eachProbability)
#            if(pro[0]>pro[1]):
#                    Name=name[0]
#            else:
#                    Name=name[1]
#        #    print(Name)
#            if(Name=='0'):
#                return 0
#            else:
#                return 1
            i=1
            for fileName in fileList: 
              #遍历文件夹中所有文件
                name=[]
                pro=[]
                n=len(fileList)
                print('本次需要检测',n,'张照片')
                k=n-i
                start = timer()
                print('还剩',k,'张待检测照片名称',fileName)
                Color.prediction.loadModel(num_objects=2)
                predictions, probabilities = Color.prediction.predictImage(('./input/'+str(fileName)), result_count=2)  
                for eachPrediction, eachProbability in zip(predictions, probabilities):
                    print(eachPrediction,':',eachProbability)
                    name.append(eachPrediction)
                    pro.append(eachProbability)
                i=i+1
                if(pro[0]>pro[1]):
                    Name=name[0]
                else:
                    Name=name[1]
                print(Name)
#                if(Name=='0'):
##                    img=cv.imread('./input/'+fileName)
##                    cv.imwrite('./0/'+fileName,img)
#                else:
##                    img=cv.imread('./input/'+fileName)
##                    cv.imwrite('./1/'+fileName,img)
#                    Name=name[1]
                end = timer()
                print('单张照片执行时间',end - start)
            print('finish')
            
            
            
if __name__ == '__main__':
    color=Color()
    fileList = os.listdir(r"./input")
    color.color_API(fileList)