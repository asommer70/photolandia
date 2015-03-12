#!/usr/bin/python
#
# Photolandia JSON API server.
#

from flask import Flask, request, render_template, redirect, flash, jsonify, send_from_directory
from werkzeug import secure_filename

import json
import shutil
import os

from os import listdir

app = Flask(__name__)


@app.route("/")
def index():
    """Send a directories files."""
    #files = listdir("/Users/adam/Pictures")
    pics_dir = "/Users/adam/Pictures/"
    files = [] 
    for filename in os.listdir(pics_dir):
        if (filename[0] != '.' and not os.path.isdir(pics_dir + filename)):
            info = os.stat(pics_dir + filename)
            files.append({"file_name": filename, "mtime": info.st_mtime, "size": info.st_size})

    return jsonify({"files": files})


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
