import arcpy
arcpy.env.overwriteOutput = True   

arcpy.analysis.Buffer(
    in_features="no_retail.shp",
    out_feature_class="./retail_buffer_1.shp",  # ← new name
    buffer_distance_or_field="500 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)

print("Created:", arcpy.Describe("./retail_buffer_1.shp").catalogPath)

