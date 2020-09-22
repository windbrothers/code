"""
迁移学习，使用vgg16模型现有的数据
"""
import keras
from keras.models import Sequential,Model,load_model
from keras.layers import Dense,Reshape,Input,Dropout,Flatten
from keras.layers import SimpleRNN,GRU, Activation
from keras.optimizers import Adam

import numpy as np
batch_size=64
label=np.load('./features/label.npy',allow_pickle=True)
dic=eval(str(label))
#print(dic)
models=["VGG16","VGG19","InceptionV3","ResNet50"]
tag="VGG16"
train_data = np.load('./features/%s_data_训练.npy'%tag)
train_labels = np.load('./features/%s_labels_训练.npy'%tag)

validation_data = np.load('./features/%s_data_验证.npy'%tag)
validation_labels =np.load('./features/%s_labels_验证.npy'%tag)

test_data = np.load('./features/%s_data_测试.npy'%tag)
test_labels =np.load('./features/%s_labels_测试.npy'%tag)
inputShape=1
for i in range(1,len(train_data.shape),1):
    inputShape*=train_data.shape[i]

train_data=train_data.reshape(-1,inputShape)
test_data=test_data.reshape(-1,inputShape)
validation_data=validation_data.reshape(-1,inputShape)
print(train_data.shape)
Train=True
if Train:
    input = Input(shape=(inputShape,))
    x = Dense(10, activation='relu')(input)
    #x = Dense(100, activation='relu')(x)
    x = Dropout(0.4)(x)
    output = Dense(len(dic), activation='softmax')(x)
    model = Model(inputs=input, outputs=output)
    # optimizer
    
    
    model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['acc'])
    
    
    model.summary()
    epochs=50
    
    history = model.fit(x=train_data,y=train_labels,
              epochs=epochs,
              batch_size=batch_size,
              validation_data=(validation_data,validation_labels),
              verbose=2)
    
    
    import pandas as pd
    d=pd.DataFrame(data=history.history)
    d.to_csv('history.csv')
    loss,accuracy=model.evaluate(test_data,test_labels)
    print(loss,'accuracy:',accuracy)
    model.save('model_'+str(epochs)+'_'+str(round(accuracy,2))+'_.h5')
    
    import matplotlib.pyplot as plt
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.legend(['Train Loss', 'Valid Loss'])
    plt.xlabel('Epoch Number')
    plt.ylabel('Loss')
    plt.ylim(0, 1)
    plt.savefig('loss.png')
    plt.show()
    
    import matplotlib.pyplot as plt
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.legend(['Train acc', 'Valid acc'])
    plt.xlabel('Epoch Number')
    plt.ylabel('acc')
    plt.ylim(0, 1)
    plt.savefig('acc.png')
    plt.show()
else:
    model=load_model("model.h5")
from sklearn import metrics
y_true=test_labels.argmax(axis=1)
y_pred_=model.predict(test_data)
y_pred=y_pred_.argmax(axis=1)
print(y_true.shape,y_pred.shape)
#print(y_true,y_pred)
uniques = np.unique(y_true,axis=0)
print(uniques.shape, uniques)
classify_report = metrics.classification_report(y_true, y_pred)
confusion_matrix = metrics.confusion_matrix(y_true, y_pred)
overall_accuracy = metrics.accuracy_score(y_true, y_pred)
acc_for_each_class = metrics.precision_score(y_true, y_pred, average=None)
average_accuracy = np.mean(acc_for_each_class)
score = metrics.accuracy_score(y_true, y_pred)
print('classify_report : \n', classify_report)
print('confusion_matrix : \n', confusion_matrix)
print('acc_for_each_class : \n', acc_for_each_class)
print('average_accuracy: {0:f}'.format(average_accuracy))
print('overall_accuracy: {0:f}'.format(overall_accuracy))
print('score: {0:f}'.format(score))




