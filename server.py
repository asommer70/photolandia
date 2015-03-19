#!/usr/bin/python
#
# Photolandia JSON API server.
#

from flask import Flask, request, render_template, redirect, flash, jsonify, send_from_directory, abort
from werkzeug import secure_filename

import json
import shutil
import os
import ConfigParser

from os import listdir

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(__location__, 'config.cfg')))

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['jpg', 'JPG', 'png'])

@app.route("/<folder>", methods=['GET', 'POST'])
def index(folder):
    """Send a directories files."""
    if (folder in config.get('Uploads', 'folders')):

        if request.method == 'GET':
            pics_dir = config.get('Uploads', 'base_folder') + '/' + folder + '/'
            files = [] 
            for filename in os.listdir(pics_dir):
                if (filename[0] != '.' and not os.path.isdir(pics_dir + filename)):
                    info = os.stat(pics_dir + filename)
                    files.append({"file_name": filename, "mtime": info.st_mtime, "size": info.st_size})

            return app.response_class(json.dumps(files), mimetype='application/json')
        else:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(config.get('Uploads', 'base_folder'), folder, filename)
                print file_path
                file.save(file_path)

            return jsonify({"status": True})
    else:
        #return app.errorhandler(404)
        abort(404)


def allowed_file(filename):
    """Only allow certain files to be uploaded."""
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
