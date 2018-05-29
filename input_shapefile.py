import fiona.crs
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch
import matplotlib.pyplot as plt
import matplotlib as mpl

#this creates the figure
fig = plt.figure(figsize=(10,10), dpi=90)
ax = plt.gca()



#your code here

#your code here

import fiona.crs
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
os.chdir('S:\\476\\Fall17\\jbell129\\fiona-basemap-juliaabell-master')
%matplotlib inline

with fiona.open('se_england_small.shp', 'r') as shp_input :
    test= shp_input[0]
    #rint test
    coords=test['geometry']['coordinates']
    print coords
    poll=Polygon(coords[0])
    patch=PolygonPatch(poll, alpha=0.5, zorder=2)
    fig=plt.figure(2, figsize=(4,4), dpi=90)
    ax=fig.add_subplot(121)
    ax.add_patch(patch)
    ax.autoscale()
    fig.show()

buildings_patch=[]
with fiona.open('se_england_small.shp', 'r') as shp_input:
    for buildings in shp_input:
        buildings_patch.append(PolygonPatch(Polygon(buildings['geometry']['coordinates'][0])))
    fig=plt.figure(figsize=(10,10), dpi=90)
    ax=plt.gca()
    ax.add_collection(mpl.collections.PatchCollection(buildings_patch,match_original=True))
    ax.autoscale()
    ax.plot()


ax.plot()



ax.plot()
