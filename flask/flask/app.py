from curses import flash
from os import path
import os
from click import File
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     # return render_template('index.html')


UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = set(['pdf', 'txt', 'doc', 'docx'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img-file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['img-file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash()
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'))
        else:
            return render_template('error.html')

    return render_template('index.html')
        
        # return redirect(url_for('uploads'))
   
if __name__=="__main__":
     app.run(debug=True)
     





