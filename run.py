from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

css = Bundle(
    'css/main.scss',
    filters=('scss',),
    output='gen/main.%(version)s.css'
)
js = Bundle(
    'js/jquery.min.js',
    'js/jquery.scrolly.min.js',
    'js/jquery.dropotron.min.js',
    'js/jquery.scrollex.min.js',
    'js/skel.min.js',
    'js/util.js',
    'js/main.js',
    output='gen/all.%(version)s.js'
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
