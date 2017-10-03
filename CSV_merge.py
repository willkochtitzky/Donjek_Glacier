
import csv

lat = []
lon = []

with open('/Volumes/Ice_sheet/St_Elias/Donjek/GPR_Data/all_GPR_data/100MHz_May23_17_Donjek/Combined _radar_data_cleaned.csv') as csvdatafile:
    csvReader = csv.reader(csvdatafile)
    for row in csvReader:
        lat.append(row[0])
        lon.append(row[1])
lat.pop(0)
lon.pop(0)

#%%

import matplotlib.pyplot as plt
plt.plot([lat], [lon],'ro')
plt.show()