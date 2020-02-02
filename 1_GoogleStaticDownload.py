import pandas as pd
import urllib, os

coords = pd.read_csv("../y1314_df.csv")

coords = coords.sample(100)

coords.head()
coords.shape

    
def GetGoogleStatic(lat, long, school_id, intervention):
    base = "https://maps.googleapis.com/maps/api/staticmap?center="
    lat = str(lat)
    long = str(long)
    url = base + lat + ',' + long + "&zoom=17&size=224x224&maptype=satellite&key=AIzaSyALr09JYKxdo34t8g3kI8Uzk0fanDZ9oNw"
    file = "./imagery/" + str(school_id) + ".png"
    urllib.request.urlretrieve(url, file)
  
  
count = 1

for index, row in coords.iterrows():
    msg = "File #" + str(count)
    print(msg)
    GetGoogleStatic(row['latitude'], row['longitude'], row['school_id'], row['intervention'])
    count += 1


