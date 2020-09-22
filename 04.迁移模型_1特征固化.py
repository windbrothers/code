# -*- coding: utf-8 -*-
"""
迁移学习，使用vgg16模型现有的数据
"""
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras import applications,Model
from keras.models import load_model
import numpy as np
import os,gc
gc.collect()
batch_size=200#ResNet50，VGG16,InceptionV3
shape=(50, 50)
#models=["VGG16","VGG19","InceptionV3","ResNet50","AlexNet"]
models=["ResNet50"]
for modelname in models:
    if modelname=="VGG16":
        base = applications.VGG16(include_top=False,input_shape=(*shape,3), weights='imagenet')
    elif modelname=="VGG19":
        base=applications.VGG19(include_top=False,input_shape=(*shape,3), weights='imagenet')
    elif modelname=="InceptionV3":
        base=applications.InceptionV3(include_top=False,input_shape=(*shape,3), weights='imagenet')
    elif modelname=="ResNet50":
        base=applications.ResNet50(include_top=False,input_shape=(*shape,3), weights='imagenet')
    print(modelname)
    model= Model(input=base.input, output=base.layers[-1].output)
    #model.summary();import sys;sys.exit()
    dirList=['训练','验证','测试']
    datagen = ImageDataGenerator()#(rescale=1.0 / 255)
    root_path='./features/'
    data_path='data'
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    for path in dirList:
        generator = datagen.flow_from_directory(data_path+'-'+path,
                                                target_size=shape,
                                                batch_size=batch_size,
                                                class_mode='categorical',
                                                shuffle=False)
        print(generator.class_indices)#输出数据的labels
        labels= np_utils.to_categorical(generator.classes)
        np.save(open(root_path+'label.npy', 'wb'), generator.class_indices)
        features= model.predict_generator(generator, len(generator.classes)/generator.batch_size)
        print('result.shape: ',features.shape)
        #import sys;sys.exit()
        print(len(generator.classes))
        print(path,'集-卷积池化数据固化成功！')
        np.save(open('%s%s_data_%s.npy'%(root_path,modelname,path), 'wb'), features)
        np.save(open('%s%s_labels_%s.npy'%(root_path,modelname,path), 'wb'), labels)
        np.save(open('%s%s_fileName_%s.npy'%(root_path,modelname,path), 'wb'), generator.filenames)