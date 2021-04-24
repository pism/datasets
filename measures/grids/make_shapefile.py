from uafgi import shputil
import uafgi.data.wkt
import uafgi.data.ns481
from osgeo import ogr,osr


# QGIS 3.0 sadly does not respect the lat/lon coordinate order
# wkt = uafgi.data.wkt.wgs84
wkt = uafgi.data.wkt.nsidc_ps_north
ns481 = uafgi.data.ns481.read(wkt)

with shputil.ShapefileWriter(
    'nsidc0481_grids.shp', 'Polygon',
    [('grid', ogr.OFTString)],
    wkt=wkt) as out:

    for row in ns481.df[['ns481_grid', 'ns481_poly']].itertuples():
        out.write(row.ns481_poly, grid=row.ns481_grid)
#        print(row.ns481_grid, )
#        print('xxxxxxxxxxx')
#        print(row['ns481_grid'])#, row['ns481_grid'])
