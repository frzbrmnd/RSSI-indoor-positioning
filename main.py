import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import time

from trilateration import trilaterate, rssi_to_distance
from wifi_scanner import scan_wifi
from filters import KalmanFilter2D


sketch = gpd.read_file("./data/sketch.geojson")

routers_coords = {
    "frzbrmnd": (273.1, -285.2),  
    "frzbrmnd1": (273.1, -279.1),  
    "frzbrmnd2": (280.7, -282.3),         
}

router_names = list(routers_coords.keys())
router_xy = list(routers_coords.values())

routers = gpd.GeoDataFrame(geometry=[Point(xy) for xy in routers_coords.values()], crs="EPSG:3857")

kf = KalmanFilter2D()

plt.ion()

fig, ax = plt.subplots(figsize=(10, 8))

sketch.plot(ax=ax, facecolor="none", edgecolor="black")
routers.plot(ax=ax, color="red", label="Routers")
user_plot = None

while True:

    #try:
     #   signals = scan_wifi()
    #except:
     #   time.sleep(1)
      #  continue
    

    # test 
    signals = {"frzbrmnd": -30, "frzbrmnd1": -50, "frzbrmnd2": -47}


    available_routers = {ssid: rssi for ssid, rssi in signals.items() if ssid in router_names}
    print(available_routers)

    if len(available_routers) < 3:
        print("Not enough routers detected. Found:", available_routers)
        time.sleep(5)
        continue
    

    #distances = [rssi_to_distance(available_routers[ssid], A=-40, n=2.0) for ssid in router_names]
    distances = [
        rssi_to_distance(available_routers["frzbrmnd"], A=-30),
        rssi_to_distance(available_routers["frzbrmnd1"]),
        rssi_to_distance(available_routers["frzbrmnd2"])]
    
    user_estimate = trilaterate(router_xy, distances)

    kf.predict()
    filtered = kf.update(user_estimate)

    user_x, user_y = filtered[0,0], filtered[1,0]


    # Update live plot  
    if user_plot is not None:
        user_plot.remove()

    user_plot = ax.scatter(user_x, user_y, color="blue", s=100, label="User location")
    plt.legend(loc='upper center')


    plt.pause(0.1)

    time.sleep(3)