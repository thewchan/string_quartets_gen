"""Temporary one-page web app for string quartet generator.


    Copyright (C) 2020  Matt Chan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    The program also utilize 3rd party modules, programs, and packages.
    When required, their license disclaimer are displayed below.

    Lilypond

    LilyPond is Copyright (C) 1998--2020  Han-Wen Nienhuys
    <hanwen@xs4all.nl> Jan Nieuwenhuizen <janneke@gnu.org> and
    published under the GNU General Public License. GNU LilyPond is
    free software: you can redistribute it and/or modify it under the
    terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your
    option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    Magenta/Coconet

    Copyright 2020 The Magenta Authors.
    Magenta/Coconet is licensed under the Apache License, Version 2.0.
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


    Music21

    Music21 is Copyright © 2006-2020 Michael Scott Cuthbert
    and cuthbertLab" and is freely licensed under the BSD 3-Clause
    License <https://spdx.org/licenses/BSD-3-Clause.html> (beginning
    with music21 v.2.0) or (for all versions) the GNU Lesser General
    Public License v3 or subsequent versions
    <https://www.gnu.org/licenses/lgpl-3.0-standalone.html>.
"""
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
