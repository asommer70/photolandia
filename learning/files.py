#!/usr/bin/python
#
# Learning about Python file methods.
#

import os

pics_dir = "/Users/adam/Pictures/"

for filename in os.listdir(pics_dir):
    if (filename[0] != '.' and not os.path.isdir(pics_dir + filename)):
        info = os.stat(pics_dir + filename)
        print info.st_mtime, info.st_size
