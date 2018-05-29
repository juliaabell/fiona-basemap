import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(10,10), dpi=90)


map = Basemap(llcrnrlon=-7.1,llcrnrlat=55.,urcrnrlon=-0.7,urcrnrlat=58.,
             resolution='c', projection='tmerc', lat_0 = 49., lon_0 = -2)


map.readshapefile('se_england_small.shp', 'buildings', drawbounds = True, color='red')


map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='white',lake_color='aqua')
map.drawcoastlines()
