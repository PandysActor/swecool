token = "pk.eyJ1IjoicGFuZHlzYWN0b3IiLCJhIjoiY2sxYWdwMmlkMTdlcDNubGwzbzhpc3drMSJ9.a1m4P6JEaNBgZcK7qGfJtA"  # you will need your own token

from urllib.request import urlopen
import json

with urlopen(
        'https://raw.githubusercontent.com/PandysActor/swecool/master/RVO/static/data/townships.geojson') as response:
    nld = json.load(response)

import pandas as pd

df = pd.read_csv(r"C:\Users\Yashv\Desktop\RVO\ongevallen\Ongevallen.csv",
                 dtype={
                     "gemeente": str,
                     "hectolttr": str,
                     "aantal_partijen": str,
                     "wegnummer": str,
                     "wegdeelltr": str,
                     "baansubsoort": str,
                     "woonplaats": str,
                     "straatnaam": str,
                     "actueel": str,
                     "distrnaam": str,
                     "wegbehsrt": str,
                     "dienstnaam": str
                 })

print(df)

import plotly.express as px

fig = px.scatter_mapbox()
fig.update_layout(mapbox_style="light",
                  mapbox_accesstoken=token,
                  mapbox_zoom=7,
                  mapbox_center={"lat": 52.1079593, "lon": 5.1893384},
                  margin={"r": 0, "t": 0, "l": 0, "b": 0},
                  mapbox_layers=[
                      {
                          "sourcetype": "geojson",
                          "type": "line",
                          "source": [
                              "https://raw.githubusercontent.com/PandysActor/swecool/master/RVO/static/data/flevo.geojson"
                          ]
                      }
                  ])

fig.show()
