import plotly.graph_objects as go
token = "pk.eyJ1IjoicGFuZHlzYWN0b3IiLCJhIjoiY2sxYWdwMmlkMTdlcDNubGwzbzhpc3drMSJ9.a1m4P6JEaNBgZcK7qGfJtA"  # you will need your own token

fig = go.Figure(go.Scattermapbox())

fig.update_layout(
    mapbox={
        'style': "stamen-terrain",
        'center': {'lon': 5.1893384, 'lat': 52.1079593},
        'zoom': 7, 'layers': [{
            'source': "https://raw.githubusercontent.com/PandysActor/swecool/master/RVO/static/data/townships.geojson",
            'type': "line", 'below': "traces", 'color': "royalblue"}]},
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0})

fig.update_layout(mapbox_style="light", mapbox_accesstoken=token,
                  mapbox_zoom=7, mapbox_center = {"lon": 5.1893384, "lat": 52.1079593})

fig.show()
