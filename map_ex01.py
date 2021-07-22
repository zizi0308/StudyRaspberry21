import folium
import json
import webbrowser
import os
from folium.plugins import HeatMap


point_data = json.loads(open('./data/point.json', mode='r', encoding='utf-8').read())

m2 = folium.Map(location=[36.505354, 127.704334], zoom_start=7, tiles='Cartodb Positron')
HeatMap(point_data).add_to(m2)

m2.save('heatmap.html')

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'    # 라즈비안에서는 필요없음
webbrowser.get(chrome_path).open(os.getcwd() + '/data/heatmap.html')
