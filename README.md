
If you are using Anaconda you should have no problems in installing all the libraries required for this lab. You can either search the libraries within the Anaconda environment or by using conda from the anaconda prompt.

Required libraries (install them in this order on a clean environment (using Python 2.7))

- matplotlib (install it via Anaconda)
- basemap (install it via Anaconda)
- shapely (`conda install -c scitools shapely `)
- fiona (`conda install -c conda-forge fiona=1.6 `)
- descartes (`conda install -c conda-forge descartes `)


There are always different problems with the libraries and using the anaconda prompt may help in understanding what is the problem going on. Here are some useful commands that can be used for fixing your environment.

`conda info --envs` prints out all the environments that you have defined. A `*` will indicate the environment in use

`conda list` prints out a list of all the modules installed in the current environment

`activate myenv` (for windows) activate the environment `myenv`

`source activate myenv` (for mac) activate the environment `myenv`

`conda remove mypackage` uninstall the module `mypackage`

`python -c "import mypackage"` for testing if `mypackage` can be imported succesfully in a script





### Loading a shapefile with Fiona

For this part use `input_shapefile.py`

Here you will try to load the shapefile containing all the buildings that we want to show on our map.

The files we will be using are `se_england_small.*`. This is a smaller version of the shp files that you can find at this [link](https://www.dropbox.com/sh/kioja4ofr2azihn/AACSCu9nvAG_a-6wiM2y4TF8a?dl=0) representing all the buildings in UK.

- Use the command

  ```
  with fiona.open(filename, 'r') as shp_input :
  ```

  to open your file. Remember that you can use any of the files sharing the same name. The open function will automatically load all of them.

- Print the content of shp_input for getting an idea of what we have loaded. If you try `print shp_input` you will notice that shp_input is actually just a collection of objects.

- Print shp_input.schema and shp_input.crc for obtaining more information about your shape files

- Now we know that our shapefile is containing 3D Polygons. For studying the format of one of these entris try printing `print shp_input[0]`. Recall that Fiona loads files organized as dictionaries.

- You will notice that under 'geometry' and 'coordinates' are stored the actual coordinates of our polygon. Let's create a Polygon out of it

  - all you have to do is accessing the list of coordiantes (remember you are working with a dictionary) and pass it to the function Polygon()

  -  to check if this is working create a PolygonPatch out of it and visualize it with descartes


- At this point let's create a figure for visualizing all these buildings together.

  - prepare an empty list for storing all the patches

  - create a `for` loop for cyclying other the buildings in shp_input

  - for each of them, create a polygon patch and append it to the list

  - once the list is ready, supposing that your list is called `buildings_patch` use the command
  ```
    ax.add_collection(mpl.collections.PatchCollection(buildings_patch, match_original=True))
  ```

  for adding the entire collection of patches to `ax`

Save the figure and upload it on GitHub


### Basics on Basemap

For this part use `input_basemap.py`

In this part of the lab we will get some confidence with Basemap. The features provided by this module are particularly useful for projecting data on a map.

- The key command that we will use is `Basemap` which will create the map. This command expects different inputs (look at the documentation). The most important for us will be:

  - the first four, indicating lat and lon of the bottom and upper corner of our image

  - `resolution`, indicating the level of detail for the obtained map

- Run the script and try to recognize the area depicted

- Now change the resolution to h

- Familiarize with the other functions involved in the script



### Drawing a shapefile on a map

For this part use `shp_basemap.py`

The libray Basemap provides a useful function for visualizing shapefiles `readshapefile()`. Unfortunantly, this function expect all the input coordinates expressed as (long, lat) and our input shapefile is in the wrong format. We will have to reproject them. Moreover the function can only visualize 2D Polygons while our input file stores 3D Polygons.

Work on the function `update_file()` first and complete the missing parts. This will be the function that will create a new file with the correct format to be read from `readshapefile()`

  - As first thing open the input file with the command `with ... as shp_input :`

  - Once opened prepare the projecting systems by using the following commands (copy them in your script)

  ```
  ori = pyproj.Proj(shp_input.crs, preserve_units=True )
  dest= pyproj.Proj(init='EPSG:4326',preserve_units=True)
  ```

  The one for the origin (ori) is deduced by the input file. The one for the destination file (dest) is provided manually.

  - We want to create a new shape file having the same schema as the input file, but storing normal `Polygons` instead of `3D Polygons`.

    - Search into `shp_input.schema` to find where the tag name `3D Polygons` is stored.

    - create a copy of `shp_input.schema` and call it `newschema`

    - modify the variable of `newschema` from `3D Polygons` to `Polygons`

    - Now we can open the output file by using the following command

    ```
    with fiona.open(name_file_out, 'w', 'ESRI Shapefile', newschema) as output:
    ```

  - It is time to actually write values in our new file. You already know how to create a loop over all the geometries stored in `shp_input`. For each object in `shp_input`:

    - access the coordinates. Remember, A polygon in shapely can have internal rings. For this reason its geometry is stored as a list of rings. Each ring is a list of tuples (/points).

    - for each pair of coordinate x,y modify them by using the following function
    ```
    pyproj.transform(ori, dest, x, y)
    ```

    - save back the new coordinates inside the object

    - write the object in the new file with the function `output.write(...)`

Load your shapefile on your map and verify that everything is working. Save the image produced and upload it on GitHub.


### Variable resolution

For this part modify `shp_basemap.py`. We will try focusing on the buildings in the city of London.

- Download the full shapefile from this [link](https://www.dropbox.com/sh/kioja4ofr2azihn/AACSCu9nvAG_a-6wiM2y4TF8a?dl=0) select `south_east_england_buildings_clipped.*`

The new script will implement a function for filtering out all the buildings which are not necessary before visualizing the results.

- start by visiting this [website](http://boundingbox.klokantech.com). From there draw a bounding box around the city center of London and (by selecting CVS format) copy the lat and long coordinates of the bounding box.

- modify the first four parameters of Basemap with such coordinates.

- now implement a function that will loop over the buildings in the shapefile. If a building is not contained in the boundingbox it won't be written in the output file. Note the input file is quite big so this function will need to run for quite a long time.

Debug your code and upload both your script and the resulting figure on GitHub
