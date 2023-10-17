from flask import Flask, render_template

import urllib.request
import json

app = Flask(__name__)

@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"  
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print(dict["results"])

    return  render_template("locations.html", locations=dict["results"])

@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"  
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print(dict["results"])

    return  render_template("episodes.html", episodes=dict["results"])

@app.route("/location/<int:id>")
def get_location_id(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"  
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print(id)
    print(dict)

    return  render_template("location_id.html", locations=dict)

@app.route("/char/<int:id>")
def get_char_id(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"  
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return  render_template("caracter_id.html", char=dict)

@app.route("/episode/<int:id>")
def get_episode_id(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"  
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print(id)
    print(dict)

    return  render_template("episode_id.html", episodes=dict)