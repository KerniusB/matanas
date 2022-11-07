from ctypes import sizeof
from operator import length_hint
from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt
import time

skaidinysSize = 10

im = Image.open('big.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())

im2 = Image.open('greenBlack.jpg', 'r')
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


def current_milli_time():
    return round(time.time() * 1000)


def showImage(array):
    image_array = np.array(array, dtype=np.uint8)
    img = PIL.Image.fromarray(image_array)

    current_time = str(current_milli_time())

    img.save(current_time+'.jpg')


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

            count = 0
            sum = 0

            for i in range(0, skaidinysSize):
                for j in range(0, skaidinysSize):
                    count += 1
                    sum += brightnessArray[index+j+(width*i)]

            rounded =int(sum/count)

            temp2 = [rounded, rounded, rounded]
            tempLine2.append(temp2)
            w += skaidinysSize
        h += skaidinysSize
        l2.append(tempLine2)

    showImage(l2)
    return l2


skaidinys = getSkaidinys(brightnessArray)
skaidinys2 = getSkaidinys(brightnessArray2)


def findMax(array1, array2):
    maxDiff = 0
    maxDiffX = 0

    i = 0
    while i < len(array1):
        if (abs(array1[i]-array2[i]) > maxDiff):
            maxDiff = abs(array1[i]-array2[i])
            maxDiffX = i
        i += 1
    print("Maksimalus skirtumas tarp tasku: ", maxDiff)
    if (maxDiffX == 0):
        x = 0
        y = 0
    else:
        x = maxDiffX % (width/skaidinysSize)
        y = maxDiffX//(width/skaidinysSize)

    print("X: ", x)
    print("Y: ", y)


def drawGraph(doubleArray, doubleArray2):
    x = list(range(1, len(doubleArray) * len(doubleArray[0])+1))
    y = []
    for w in doubleArray:
        for h in w:
            y.append(h[0])

    # plotting the points
    plt.plot(x, y, label="Pirma nuotrauka")
    # plt.scatter(x, y, label= "first", color= "green",
    #         marker= ".", s=1)

    # line 2 points
    x2 = x
    y2 = []

    for w in doubleArray2:
        for h in w:
            y2.append(h[0])

    # plotting the line 2 points
    plt.plot(x2, y2, label="Antra nuotrauka")
    # plt.scatter(x2, y2, label= "second", color= "blue",
    #         marker= ".", s=1)

    # naming the x axis
    plt.xlabel('x - skaidiniai')
    # naming the y axis
    plt.ylabel('y - ryškumas')
    # giving a title to my graph
    plt.title('Nuotraukų palyginimo grafikas')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

    findMax(y, y2)


# pip install matplotlib
drawGraph(skaidinys, skaidinys2)
