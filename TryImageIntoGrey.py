import cv2
import os


def colortoGray():
    files=os.listdir('/Users/dhingra/PycharmProjects/ImageProcessing/')
    for i in files:
        if i.endswith('.jpeg'):
            color=cv2.imread(i,0)
            cv2.imwrite('Gray_'+i,color)


def resizepercentage(scalerpercentage,height,width):
    newheight=int((height*scalerpercentage)/100)
    newwidth=int((width*scalerpercentage)/100)
    return newheight,newwidth

def resizeimage(scalepercentage,imagepath):
    files = os.listdir(imagepath)
    for i in files:
        if i.endswith('.jpeg'):
            color = cv2.imread(i)
            #print(color.shape)
            new_dim=resizepercentage(scalepercentage,color.shape[0],color.shape[1])
            newimage=cv2.resize(color,new_dim)
            cv2.imwrite(f'Resize_{i.title()}',newimage)


