from flask import Flask, render_template, request
from flask.ext.assets import Environment, Bundle
import sendgrid
import sys
import os
import logging
from webassets.filter import get_filter

scss = get_filter('scss', load_paths='static/css')

app = Flask(__name__)
assets = Environment(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'),
    os.environ.get('SENDGRID_PASSWORD'))

css = Bundle(
    'css/main.scss',
    filters=(scss,),
    output='gen/main.css'
)
js = Bundle(
    'js/jquery.min.js',
    'js/jquery.scrolly.min.js',
    'js/jquery.dropotron.min.js',
    'js/jquery.scrollex.min.js',
    'js/skel.min.js',
    'js/util.js',
    'js/main.js',
    output='gen/all.js'
)

assets.register('css_all', css)

assets.register('js_all', js)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/reserve')
def reserve():
    return render_template('reserve.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/email', methods=["POST"])
def email():
    name = request.form['name']
    email = request.form['email']
    text = request.form['text']

    message = sendgrid.Mail()

    message.add_to("contact@technicolorworld.xyz")
    message.set_from(email)
    message.set_subject("Contact Us")
    message.set_html(text)

    sg.send(message)

    return "Message received!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
