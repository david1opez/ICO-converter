from PIL import Image
from os import listdir
import os
from os.path import isfile, join
import shutil 

onlyfiles = [f for f in listdir("C:/Users/david/Desktop/Coding/ico converter/files") if isfile(join("C:/Users/david/Desktop/Coding/ico converter/files", f))]

for file in onlyfiles:
    filename = "./files/"+file

    img = Image.open(filename)

    newfilename = file.replace('.png', '')
    newfilename = newfilename+".ico"

    img.save(newfilename,format = 'ICO', sizes=[(64,64)])

    destination = 'C:/Users/david/Pictures/icons'

    shutil.move(newfilename, destination)

    os.remove("newfilename.ico")