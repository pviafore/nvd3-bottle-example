from __future__ import print_function
import json
from bottle import run, get, static_file

def get_data():
    data = [
        {
            "x": 55,
            "y": 29,
        },
        {
            "x": 103,
            "y": 2,
        },
        {
            "x": 17,
            "y": 42,
        },
        {
            "x": 12,
            "y": 33,
        },
        {
            "x": 66,
            "y": 57,
        }
    ]
    return sorted(data, key=lambda i: i["x"])


@get("/data")
def return_data():
    return {
        "key": "Random Data",
        "color": "#ffaa00",
        "values": get_data()
        }

@get("/")
def index_page():
    route_to_static_file("index.html")

@get("<path:path>")
def route_to_static_file(path):
    return static_file(path, root="static")

# 0.0.0.0 binds on public and localhost
print("Go to http://localhost:8181")
run(host="0.0.0.0", port=8181, debug=True)
