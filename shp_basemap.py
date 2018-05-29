
from shapely.geometry import Polygon, MultiPolygon
from descartes.patch import PolygonPatch

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap

import pyproj
import fiona
import fiona.crs

import os
os.chdir('S:\\476\\Fall17\\jbell129\\fiona-basemap-juliaabell-master')
%matplotlib inline

input_file ='S:\\476\\Fall17\\jbell129\\fiona-basemap-juliaabell-master\\se_england_small.shp' 
modified_file = 'S:\\476\\Fall17\\jbell129\\fiona-basemap-juliaabell-master\\modified'

def update_file(name_file_in, name_file_out):
    with fiona.open(name_file_in, 'r') as shp_input :
        ori = pyproj.Proj(shp_input.crs, preserve_units=True )
        dest= pyproj.Proj(init='EPSG:4326',preserve_units=True)
        new_schema= shp_input.schema.copy()

        new_schema['geometry']='Polygon'
        #print new_schema
        with fiona.open(name_file_out, 'w', 'ESRI Shapefile', new_schema) as output:
            for building in shp_input:
                #print building['geometry']['coordinates']
                for i in range(0,len(building['geometry']['coordinates'])):
                    coords = building['geometry']['coordinates'][i]
                    new_list=[]
                    for x,y,z in coords:
                        new_coords=pyproj.transform(ori, dest, x, y)
                        
                        new_list.append(new_coords) 
                        
                    building['geometry']['coordinates'][i]=new_list


                output.write(building)


update_file(input_file, modified_file)


fig = plt.figure(figsize=(10,10), dpi=90)


map = Basemap(llcrnrlon=-1.0,llcrnrlat=51.,urcrnrlon=0.8,urcrnrlat=52.,
             resolution='c', projection='tmerc', lat_0 = 49., lon_0 = -2)


map.readshapefile('S:\\476\\Fall17\\jbell129\\fiona-basemap-juliaabell-master\\modified\\modified', 'buildings', drawbounds = True, color='red')

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='white',lake_color='aqua')
map.drawcoastlines() 
