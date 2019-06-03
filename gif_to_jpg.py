import os
import sys
from PIL import Image

originPath = '/Volumes/VCIP2_PC/2019-05 Goad Cut Gif and JPEG'


def getFiles (originPath):
    originPaths = []
    for (dirpath, dirnames, filenames) in os.walk(originPath):
        originPaths.append([dirpath, filenames] )
    return originPaths

originPaths = getFiles(originPath)


def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print("Cant load", infile)
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            # new_im = Image.new("RGBA", im.size)
            new_im = Image.new("RGB", im.size)
            new_im.paste(im)
            infileLength = len(infile.split('.')[0].split('/'))

            print('./jpgs/'+ infile.split('.')[0].split('/')[infileLength - 1] +'.jpg')
            new_im.save('./jpgs/'+ infile.split('.')[0].split('/')[infileLength - 1] +'.jpg')

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence

for p in originPaths:
    for f in p[1]:
        if 'gif' in f:
            fileName = p[0] + '/' + f
            # print(fileName)
            processImage(fileName)
