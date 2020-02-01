# encoding: UTF-8
import glob as gb
import cv2
#img_path = gb.glob("./bdd/training/6a6bee72-3b46eff2_epsnet_pred20.png") 
#img_path.sort()
#img_gt = gb.glob("./Result/FCNS/um_gt/*.png") 
#img_gt = gb.glob("./Result/ESPNET/BDDTrain/6a6bee72-3b46eff2.png") 
#img_gt.sort()
#videoWriter = cv2.VideoWriter('./Result/ESPNET/EPSNETFPS15.avi',cv2.VideoWriter_fourcc(*'MJPG'), 15, (1242,375))
img_path = ".//Result/ESPNET/BDDTrain/6a6bee72-3b46eff2_epsnet_pred20.png" 
img_gt = "./bdd/training/image/6a6bee72-3b46eff2.jpg"
'''
for path ,gt_path in zip(img_path , img_gt):
    print(path)
    img  = cv2.imread(path) 
    img = cv2.resize(img,(1242,375)) 
    img_gt = cv2.imread(gt_path)
    img_gt = cv2.resize(img_gt,(1242,375)) 
    alpha = 0.75
    beta = 1-alpha
    gamma = 0
    img_add = cv2.addWeighted(img_gt, alpha, img, beta, gamma)
    #videoWriter.write(img_add) 
    cv2.imwrite('./Result/ESPNET/BDDTrain/bdd-1.png', img_add)
'''
    
'''
for gt_path in img_gt:
    print(gt_path)
    img_gt = cv2.imread(gt_path)
    img_gt = cv2.resize(img_gt,(1242,375))
    videoWriter.write(img_gt) 
'''
img  = cv2.imread(img_path) 
img = cv2.resize(img,(1280,720)) 
img_gt = cv2.imread(img_gt)
img_gt = cv2.resize(img_gt,(1280,720)) 
alpha = 0.75
beta = 1-alpha
gamma = 0
img_add = cv2.addWeighted(img_gt, alpha, img, beta, gamma) 
cv2.imwrite('./Result/ESPNET/BDDTrain/bdd-1.png', img_add)