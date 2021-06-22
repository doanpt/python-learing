import json
import os
import glob
import codecs
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    dir_name = '2021-06'
    if not os.path.isdir(dir_name):
        return 'Không tồn tại thư mục chứa dữ liệu'

    data = []
    for fn in glob.glob('%s/*.json' % dir_name):
        f = codecs.open(fn, mode='r', encoding='utf-8')
        data.append(json.load(f))
    return render_template('app.html', articles=data)


@app.route('/article/<post_id>')
def article_detail(post_id):
    dir_name = '2021-06'
    fn = '%s/%s.json' % (dir_name, post_id)
    if not os.path.isfile(fn):
        return 'Không tồn tại tile %s.json' % post_id

    f = codecs.open(fn, mode='r', encoding='utf-8')
    d = json.load(f)

    return render_template('article_detail.html', article=d)
