#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:14:49 2017

@author: willkochtitzky
"""

import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import fiona
#import rasterio
#import rasterio.plot
import matplotlib as mpl
#from descartes import PolygonPatch
from matplotlib import cm
import numpy as np
 

#cd /Volumes/Ice_sheet/St_Elias/Donjek/Elevation_data/2000LiDAR/

xdata2000 = []
ydata2000 = []
zdata2000 = []

xdata2012 = []
ydata2012 = []
zdata2012 = []

filename2000 = '/Users/willkochtitzky/Desktop/2000LiDAR_data_Donjek.csv' 
filename2012 = '/Users/willkochtitzky/Desktop/Donjek_lidar2012.csv'

with open(filename2000) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        x = row[0]
        y = row[1]
        z = row[2]
        
        xdata2000.append(x)
        ydata2000.append(y)
        zdata2000.append(z)

with open(filename2012) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        x = row[0]
        y = row[1]
        z = row[2]
        
        xdata2012.append(x)
        ydata2012.append(y)
        zdata2012.append(z)

plt.figure(1)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)
ax.set_title("Donjek LiDAR scan 2000",fontsize=14)
ax.set_xlabel("Easting",fontsize=12)
ax.set_ylabel("Northing",fontsize=12)
ax.grid(True,linestyle='-',color='0.75')



# scatter with colormap mapping to z value
sc = ax.scatter(xdata2000,ydata2000,s=20,c=zdata2000, marker = 'o', cmap = cm.jet );
plt.colorbar(sc)

plt.show()
plt.axes().set_aspect('equal', 'datalim')



plt.figure(2)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)
ax.set_title("Donjek LiDAR scan 2012",fontsize=14)
ax.set_xlabel("Easting",fontsize=12)
ax.set_ylabel("Northing",fontsize=12)
ax.grid(True,linestyle='-',color='0.75')



# scatter with colormap mapping to z value
sc = ax.scatter(xdata2012,ydata2012,s=20,c=zdata2012, marker = 'o', cmap = cm.jet );
plt.colorbar(sc)

plt.show()
plt.axes().set_aspect('equal', 'datalim')



#plt.plot(xdata, ydata)
#plt.ylabel('Northing (m)')
#plt.xlabel('Easting (m)')
#plt.legend()
#
#
#
#
#src = rasterio.open("/Users/willkochtitzky/Desktop/LC08_L1TP_063017_20170518_20170519_01_RT_B8.TIF")
#
#with fiona.open("tests/data/box.shp", "r") as shapefile:
#    features = [feature["geometry"] for feature in shapefile]
#
#rasterio.plot.show((src, 1))
#ax = mpl.pyplot.gca()
#
#patches = [PolygonPatch(feature) for feature in features]
#ax.add_collection(mpl.collections.PatchCollection(patches))