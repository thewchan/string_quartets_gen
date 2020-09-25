"""Temporary one-page web app for string quartet generator."""
import os
import subprocess

import music21
from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'mid', 'midi'}
UPLOAD_FOLDER = './samples/result/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Parse filename and make sure their extensions are allowed."""
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
            )


def run_model(filename):
    """Take file and run through coconet."""
    subprocess.run([
        'python',
        './coconet_sample.py',
        f'--prime_midi_melody_fpath={UPLOAD_FOLDER}{filename}',
        '--checkpoint=./coconet_checkpoint/coconet-64layers-128filters',
        '--gen_batch_size=1',
        '--logtostderr',
        '--piece_length=32',
        '--temperature=0.99',
        '--strategy=harmonize_midi_melody',
        '--tfsample=false',
        '--generation_output_dir=./samples/',
    ])


def convert_pdf():
    """Convert midi from model to pdf."""
    music = music21.converter.parse('./samples/result/midi/result_0.midi')
    music.write('lilypond', './samples/result/result.ly')
    subprocess.run([
        'lilypond',
        '-o',
        './samples/result/',
        './samples/result/result.ly'
    ])


@app.route('/', methods=['GET', 'POST'])
def index():
    """Temporary home page for string quartet web-app."""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')

            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')

            return redirect(request.url)

        if file and allowed_file(file.filename):
            subprocess.run(['rm', '-rd', './samples/result/*'])
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(filename)
            run_model(filename)
            convert_pdf()
            return redirect(url_for('uploaded_file', filename='./result.pdf'))

    return render_template('index.html')


@app.route('/samples/result/<filename>')
def uploaded_file(filename):
    """Return filename."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
