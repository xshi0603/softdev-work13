from flask import Flask, render_template
import urllib2
import json

my_app = Flask(__name__)

@my_app.route('/')
def root():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=q8swkCopUNHfG2Te4avaacozGrZbEyxF0gJlIDoE")
    html =  data.read()
    data_dict = json.loads(html)
    imgURL = data_dict["url"]
    explanation = data_dict["explanation"]
    return render_template('index.html', img = imgURL, explained = explanation)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
