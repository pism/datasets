The file tc-9-2215-2015-supplement.csv was created via:
ogr2ogr -f CSV x.csv tc-9-2215-2015-supplement/GreenlandGlacierNames_GGNv01_WGS84.shp



Greenland glacier IDs from tc-9-2215-2015-supplement.csv [] are used
as unique identifier and location for each glacier; and can be
searched for names as well.  For glaciers that do not appear in that
dataset, this information is extended by glaciers_locations_ext.csv;
which is to be edited as needed.

The file glacier_names.csv may also be used to match names to glaciers.  Names are highly variable; sometimes abbreviated; sometimes Greenlandic or Danish or other.  So each glacier may be in this table more than once.  The file should be extended as needed to match glaciers as they come up.

Sometimes the same name is used for glaciers in different regions of Greenland.  To disambiguate, glacier_names.csv has a *coast* attribute, determining which region of the Greenland Coast a glacier is located in.  See ../GreenlandGlacierStats/GreenlandGlacierStats.csv

