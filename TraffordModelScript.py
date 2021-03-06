import arcpy

arcpy.env.workspace = "m:/Documents/Programming2/Prac4/"

if arcpy.Exists("crime.shp"):
    arcpy.Delete_management ("crime.shp")

Burglaries = arcpy.GetParameterAsText(0)
Distance = arcpy.GetParameterAsText(1)
Buildings = arcpy.GetParameterAsText(2)
Out = "crime.shp"

arcpy.ImportToolbox("m:/Documents/Programming2/Prac1/Models.tbx", "models")
arcpy.TraffordModel_models(Burglaries, Distance, Buildings, Out)

if arcpy.Exists("crime_sorted.shp"):
    arcpy.Delete_management ("crime_sorted.shp")
arcpy.Sort_management(Out, "crime_sorted", [["Join_Count", "DESCENDING"]])

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame 
newlayer = arcpy.mapping.Layer("crime_sorted.shp")
layerFile = arcpy.mapping.Layer("m:/Documents/Programming2/Prac4/albertsquare/buildings.lyr")
arcpy.mapping.UpdateLayer(df, newlayer, layerFile, True)
newlayer.symbology.valueField = "Join_Count"
newlayer.symbology.addAllValues() 
arcpy.mapping.AddLayer(df, newlayer,"TOP")