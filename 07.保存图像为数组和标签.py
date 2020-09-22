import os
import numpy as np
def get_path(path_dir='0'):
    Train=[]
    Test=[]
    for (root, dirs, files) in os.walk(path_dir):
        if root==path_dir:
            continue
        elif root==path_dir+'\\train':
            continue
        elif root==path_dir+'\\test':
            continue
        elif 'train' in root:
            Train.append(root)
        elif 'test' in root:
            Test.append(root)
    return Train,Test


from skimage import transform,io
shape=(32,32)
def get_img(f):
    rgb=io.imread(f)
    return transform.resize(rgb, shape)

Trains,Tests=get_path()


Train_data=np.zeros((0,*shape,3))
Train_label=np.zeros((0))
#
Test_data=np.zeros((0,*shape,3))
Test_label=np.zeros((0))
i=0
for (Train,Test) in zip(Trains,Tests):
#    
    coll = io.ImageCollection(Train + '/*.jpg',load_func=get_img)
    mat1=io.concatenate_images(coll) 
#    print(mat1)
    Train_label=np.concatenate([Train_label,np.array([i]*mat1.shape[0])],axis=0)
#    print(Train_label)
    Train_data= np.concatenate([Train_data,mat1],axis=0)
##    
#    coll = io.ImageCollection(Test + '/*.jpg',load_func=get_img)
#    mat2=io.concatenate_images(coll) 
#    Test_label=np.concatenate([Test_label,np.array([i]*mat2.shape[0])],axis=0)
##    print(Test_label)
#    Test_data= np.concatenate([Test_data,mat2],axis=0)
#    
    i+=1
    print(Train,mat1.shape,Train_label.shape,Test,mat2.shape,Test_label.shape)
np.save('Train-img_data-200',Train_data)
np.save('Train-img_label-200',Train_label)
np.save('Test-img_data-200',Test_data)
np.save('Test-img_label-200',Test_label)
print('save img data & label')
#print(Train_data,Train_label,Test_data,Test_label)