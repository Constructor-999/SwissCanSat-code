import pandas as pd
from sklearn import linear_model
import numpy as np

timeHeight = pd.read_csv("testDirec.csv", usecols=['time', 'hauteur'])
timelat = pd.read_csv("testDirec.csv", usecols=['time', 'lat'])
timelong = pd.read_csv("testDirec.csv", usecols=['time', 'long'])

Xheight = timeHeight.drop(['hauteur'], axis=1)
modelHeight = linear_model.LinearRegression()
modelHeight.fit(Xheight, timeHeight['hauteur'])
predsHeight = modelHeight.predict(Xheight)
arrayHeight = np.array(predsHeight).astype(int)

#Déterminer la valeur du taux de variation (a) (a * x + b)
aH = (arrayHeight[0] - arrayHeight[-1]) / (timeHeight['time'][0] - timeHeight['time'][timeHeight['time'].size -1])
#determiner le parmètre b
bH = arrayHeight[0] - (aH * timeHeight['time'][0])
print(f"fonction hauteur: {aH}x + {bH}")



Xlat = timelat.drop(['lat'], axis=1)
modelLat = linear_model.LinearRegression()
modelLat.fit(Xlat, timelat['lat'])
predsLat = modelLat.predict(Xlat)
arrayLat = np.array(predsLat)

#Déterminer la valeur du taux de variation (a) (a * x + b)
aLat = (arrayLat[0] - arrayLat[-1]) / (timelat['time'][0] - timelat['time'][timelat['time'].size -1])
#determiner le parmètre b
bLat = arrayLat[0] - (aLat * timelat['time'][0])
print(f"fonction latitude: {aLat}x + {bLat}")


Xlong = timelong.drop(['long'], axis=1)
modelLong = linear_model.LinearRegression()
modelLong.fit(Xlong, timelong['long'])
predsLong = modelLong.predict(Xlong)
arrayLong = np.array(predsLong)

#Déterminer la valeur du taux de variation (a) (a * x + b)
aLong = (arrayLong[0] - arrayLong[-1]) / (timelong['time'][0] - timelong['time'][timelong['time'].size -1])
#determiner le parmètre b
bLong = arrayLong[0] - (aLong * timelong['time'][0])
print(f"fonction longitude: {aLong}x + {bLong}")