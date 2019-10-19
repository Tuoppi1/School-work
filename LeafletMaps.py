# Press run in jupyter notebook

from IPython.display import display as disp
from ipywidgets import Layout, HTML
from ipyleaflet import CircleMarker, Map
import time
import requests

center = (61.491111, 23.794797)
m = Map(center=center, zoom=13, layout=Layout(width='900px', height='600px'))
disp(m)
    
while True:
    busData = requests.get("http://data.itsfactory.fi/journeys/api/1/vehicle-activity").json()
    busList = []
    for bus in busData["body"]:
        currentBus = []
        currentBus.append([bus["monitoredVehicleJourney"]["lineRef"]])
        currentBus.append(bus["monitoredVehicleJourney"]["vehicleLocation"]["longitude"])
        currentBus.append(bus["monitoredVehicleJourney"]["vehicleLocation"]["latitude"])
        busList.append(currentBus)

    markerList = []
    for i in busList:
        busMarker = CircleMarker(location=(i[2], i[1]), radius=5, popup=HTML(str(i[0])))
        markerList.append(busMarker)
    for i in markerList:
        m.add_layer(i)
    time.sleep(5)
    for i in markerList:
        m.remove_layer(i)
