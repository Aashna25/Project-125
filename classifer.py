import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps
X = np.load('image.npz')['arr_0']
y = pd.read_csv("labels.csv")["labels"]
print(pd.Series(y).value_counts())
classes =['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nclasses = len(classes)
xtrain,xtest,ytrain,ytest=train_test_split(X,y, random_state=9,train_size=3500,test_size=500)


def getPrediction(image):
    imPIL=Image.open(image)
    image_bw=imPIL.convert("L")
    image_bw_resize=image_bw.resize((22,30),Image.ANTIALIAS)
    pixelfilter=20
    minpixel=np.percentile(image_bw_resize,pixelfilter)
    image_bw_resize_inverted_scale= np.clip(image_bw_resize-minpixel,0,255)
    maxpixel=np.math(image_bw_resize)
    image_bw_resize_inverted_scale=np.asarray(image_bw_resize_inverted_scale)/maxpixel
    testsample=np.array(image_bw_resize_inverted_scale).reshape(1,660)
    testpred=clf.predict(testsample)
    return testpred[0]

    
    


    
