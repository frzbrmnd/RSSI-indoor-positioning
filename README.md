# RSSI-indoor-positioning
A lightweight indoor localization system using WiFi RSSI measurements, trilateration, and Kalman filtering for real-time tracking.
Designed for research, prototyping, and educational use.

# Research Motivation
Indoor positioning is a challenging research problem due to multipath interference, signal decay, and environmental noise. This project explores signal-based localization using RSSI trilateration combined with predictive filtering. The goal is to understand the limitations of RSSI-based methods and explore techniques to improve accuracy, making it a starting point for future research in indoor navigation, IoT sensing, or wireless localization.

# Overview
This project implements a real-time indoor positioning system (IPS) using:
- WiFi signal strength (RSSI)
- Distance estimation using empirical path-loss model
- 2D trilateration using three known access points
- Kalman filtering to smooth noisy measurements
- GeoJSON indoor floor plan visualization
- Real-time location updates (every 3 seconds)

It is fully implemented in Python and runs on Linux systems that support the iw WiFi scanner.

This repository demonstrates practical knowledge in:
- Wireless localization
- Geo-spatial data processing
- Python scientific computing
- Real-time system design
- Filtering and noise modeling

# Python packages
- matplotlib
- geopandas
- shapely
- numpy
- subprocess

# Methodology
## RSSI to Distance
A log-distance path loss model:

          d=10^(RSSI-A)/(10*n)
          ​
- A = RSSI at 1 meter (must be measured for accuracy)
- n ≈ 1.6 – 3.5 indoors
## Trilateration
Given routers at:

(x1, y1), (x2, y2), (x3, y3)

and distance r1, r2, r3,

the algorithm estimates user position using geometric decomposition (unit vectors, projections).
## Kalman Filter (2D)
State vector:

          [x, y, Vx, Vy]

Used to smooth noisy WiFi measurements  
## Visualization
The indoor layout is drawn in QGIS, exported as GeoJSON, and plotted with Matplotlib

Routers appear as red dots.

User position updates live every 3 seconds
