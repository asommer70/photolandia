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

ALLOWED_EXTENSIONS = set(['jpg', 'JPG', 'png'])

@app.route("/", methods=['GET', 'POST'])
def index():
    """Send a directories files."""

    if request.method == 'GET':
        #files = listdir("/Users/adam/Pictures")
        pics_dir = "/Users/adam/Pictures/"
        files = [] 
        for filename in os.listdir(pics_dir):
            if (filename[0] != '.' and not os.path.isdir(pics_dir + filename)):
                info = os.stat(pics_dir + filename)
                files.append({"file_name": filename, "mtime": info.st_mtime, "size": info.st_size})

        #return jsonify({"files": files})
        return app.response_class(json.dumps(files), mimetype='application/json')
    else:
        #print "files:", request.files
        #print "data:", request.data
        #print "form:", request.form
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join('/Users/adam/Pictures', filename)
            file.save(file_path)

        return jsonify({"status": True})


def allowed_file(filename):
    """Only allow certain files to be uploaded."""
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
