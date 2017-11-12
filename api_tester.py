from flask import Flask, render_template
import urllib2
import json

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template("index.html")

@my_app.route('/nasa', methods=['POST', 'GET'])
def nasa():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=q8swkCopUNHfG2Te4avaacozGrZbEyxF0gJlIDoE")
    html =  data.read()
    data_dict = json.loads(html)
    imgURL = data_dict["url"]
    explanation = data_dict["explanation"]
    return render_template('nasa.html', img = imgURL, explained = explanation)

@my_app.route('/weather', methods=['POST', 'GET'])
def weather():
    data = urllib2.urlopen("http://api.wunderground.com/api/ab6209433554e030/conditions/q/CA/San_Francisco.json")
    html =  data.read()
    data_dict = json.loads(html)
    area = data_dict["current_observation"]["observation_location"]["full"]
    lat = data_dict["current_observation"]["observation_location"]["latitude"]
    longi = data_dict["current_observation"]["observation_location"]["longitude"]
    weather = data_dict["current_observation"]["weather"]
    temp = data_dict["current_observation"]["temp_f"]
    return render_template('weather.html', curr_area = area, curr_lat = lat, curr_long = longi, curr_weather = weather, curr_temp = temp)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
