# This code will come in handy to read all the images in a folder.

import os
x = os.scandir("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images")
for i in x:
    print(i.name)