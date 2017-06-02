""" 
A simple webserver that returns canned data
"""

from __future__ import print_function
from random import randint

from bottle import run, get, static_file

def make_random_coordinate():
    """ Make a random coordinate dictionary"""
    return make_coordinate(randint(0, 100), randint(0, 100))

def make_coordinate(x_coord, y_coord):
    """ Make a coordinate dictionary"""
    return \
        {
            "x": x_coord,
            "y": y_coord
        }

def get_data():
    """ Returns a sorted array of random data """
    data = [
        make_coordinate(55, 29),
        make_coordinate(103, 2),
        make_coordinate(17, 42),
        make_coordinate(12, 33),
        make_coordinate(66, 57),
        make_random_coordinate(),
        make_random_coordinate(),
        make_random_coordinate(),
        make_random_coordinate()
    ]
    return sorted(data, key=lambda i: i["x"])

@get("/test-hello")
def return_html():
    return "<h3 color='red'>HELLO THIS IS REAL</h3>"

@get("/data")
def return_data():
    """ Return a dictionary that NVD3 will understand """
    return {
        "key": "Random Data",
        "color": "#000000",
        "values": get_data()
        }

@get("/")
def index_page():
    """ Print out the index page """
    return route_to_static_file("index.html")

@get("<path:path>")
def route_to_static_file(path):
    """ Route to a static file if the user puts it in """
    return static_file(path, root="static")

# 0.0.0.0 binds on public IP and localhost
print("Go to http://localhost:8181")
run(host="0.0.0.0", port=8181, debug=True)
