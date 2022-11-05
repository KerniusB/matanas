from ctypes import sizeof
from operator import length_hint
from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('small.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())

im2 = Image.open('small2.jpg', 'r')
width2, height2 = im2.size
pixel_values2 = list(im2.getdata())

def getBrightness(pixelValues):
    brightnessArray = []

    for x in pixelValues:
        rgbSum = x[0] + x[1] + x[2]
        brightness = rgbSum / 3
        brightnessArray.append(brightness)  
    return brightnessArray

brightnessArray = getBrightness(pixel_values)
brightnessArray2 = getBrightness(pixel_values2)

def showImage(array):
    image_array = np.array(array, dtype=np.uint8)
    img = PIL.Image.fromarray(image_array)
    img.show()

def prepareForViewing(brightnessArray):
    l = []
    temp = []
    tempLine = []

    h = 0
    while h < height:
        w = 0
        tempLine = []
        while w < width:
            index = h * width + w
            value = round(brightnessArray[index])
            temp = [value, value, value]
            tempLine.append(temp)
            w += 1
        h += 1
        l.append(tempLine)
    
    showImage(l)

prepareForViewing(brightnessArray)
prepareForViewing(brightnessArray2)


def getSkaidinys(brightnessArray):
    l2 = []
    temp2 = []
    tempLine2 = []

    h = 0
    while h < height:
        w = 0
        tempLine2 = []
        while w < width:
            index = h * width + w

            value = round(brightnessArray[index])
            value2 = round(brightnessArray[index+1])
            value3 = round(brightnessArray[index+width])
            value4 = round(brightnessArray[index+width+1])

            rounded = (value + value2 + value3 + value4)/4

            temp2 = [rounded, rounded, rounded]
            tempLine2.append(temp2)
            w += 2
        h += 2
        l2.append(tempLine2)

    showImage(l2)
    return l2

l2 = getSkaidinys(brightnessArray)
belekas = getSkaidinys(brightnessArray2)

def drawGraph(doubleArray, doubleArray2):
    x = list(range(1, len(doubleArray)* len(doubleArray[0])+1))
    y=[]
    for w in doubleArray:
        for h in w:
            y.append(h[0])

    print(len(x))
    print(len(y))

    # plotting the points 
    plt.plot(x, y, label = "line 1")
    # plt.scatter(x, y, label= "first", color= "green", 
    #         marker= ".", s=1)

    # line 2 points
    x2 = x
    y2 = []

    for w in doubleArray2:
        for h in w:
            y2.append(h[0])

    # plotting the line 2 points 
    plt.plot(x2, y2, label = "line 2")
    # plt.scatter(x2, y2, label= "second", color= "blue", 
    #         marker= ".", s=1)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title('Two lines on same graph!')
    
    # show a legend on the plot
    plt.legend()
    
    # function to show the plot
    plt.show()
  

# pip install matplotlib
drawGraph(l2, belekas)