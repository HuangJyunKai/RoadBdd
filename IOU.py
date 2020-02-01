# encoding: UTF-8
import glob as gb
import cv2
import numpy as np
img_path = gb.glob("./IOU/Result/*") 
img_path.sort()
img_gt = gb.glob("./IOU/label/*") 
img_gt.sort()
#videoWriter = cv2.VideoWriter('./Result/ESPNET/EPSNETFPS15.avi',cv2.VideoWriter_fourcc(*'MJPG'), 15, (1242,375))

ans=0
for path ,gt_path in zip(img_path , img_gt):
    print(path)
    img = cv2.imread(path,0) 
    img = cv2.resize(img,(1242,375)) 
    #print(img.shape)
    #print(np.unique(img))
    img_gt = cv2.imread(gt_path,0)
    img_gt = cv2.resize(img_gt,(1242,375)) 
    #print(np.unique(img_gt))
    count105=0
    counttrue=0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] == 105 and img_gt[i][j] == 105:
                count105+=1
            if img_gt[i][j] == 105:
                counttrue+=1
    print(count105/counttrue)
    ans+= (count105/counttrue)
print("Total:",ans/95)
