import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import folium
import geopandas as gpd
import pandas as pd
import dash_bootstrap_components as dbc
from folium import plugins





df = pd.read_csv('bus_stops_and_terminals_654.csv')


# Create a map centered at a specific location
center_latitude = df['latitude'].mean()
center_longitude = df['longitude'].mean()
m = folium.Map(location=[7.291726, 80.721430], zoom_start=15)

# Define colors based on direction
colors = {'Digana-Kandy': 'green', 'Kandy-Digana': 'blue'}

# Add markers for each bus's GPS coordinate
for _, row in df.iterrows():
    direction = row['direction']
    color = colors.get(direction, 'gray')  # Use gray if direction is not in colors dict
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Stop ID: {row['stop_id']}<br>Direction: {row['direction']}<br>Bus Stop: {row['address']}",
        icon=folium.Icon(color=color),
        legend_name='Unemployment Rate (%)'
    ).add_to(m)

import branca

legend_html = '''
{% macro html(this, kwargs) %}
<div style="
    position: fixed; 
    bottom: 50px;
    left: 50px;
    width: 200px;
    height: 80px;
    z-index:9999;
    font-size:14px;
    ">
    <p><a style="color:#36a6da;font-size:150%;margin-left:20px;"><i class="fa fa-map-marker-alt" style="color: #36a6da;"></i></a>&emsp;Digana-Kandy</p>
    <p><a style="color:#70af27;font-size:150%;margin-left:20px;"><i class="fa fa-map-marker-alt" style="color: #70af27;"></i></a>&emsp;Kandy-Digana</p>
</div>
<div style="
    position: fixed; 
    bottom: 50px;
    left: 50px;
    width: 150px;
    height: 80px; 
    z-index:9998;
    font-size:14px;
    background-color: #ffffff;

    opacity: 0.7;
    ">
</div>
{% endmacro %}
'''
legend = branca.element.MacroElement()
legend._template = branca.element.Template(legend_html)

folium.LayerControl().add_to(m)
m.get_root().add_child(legend)

# Save the map to an HTML file
m.save("gps_map.html")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Iframe(srcDoc=open('gps_map.html', 'r').read(), width='100%', height='600')
])

if __name__ == '__main__':
    app.run_server(debug=True)