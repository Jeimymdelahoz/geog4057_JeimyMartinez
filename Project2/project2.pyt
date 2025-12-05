# -*- coding: utf-8 -*-

import arcpy
from project import project2


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "project 2 Toolbox"
        self.alias = "project2"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Extract Elevation from Google Earth Engine"
        self.description = "Converts CSV to shapefile and adds elevation values from USGS 3DEP."

    def getParameterInfo(self):
        """Define the tool parameters."""
        param0 = arcpy.Parameter(
            displayName="CSV File", 
            name="csv_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        
        #param1 is a shafile name
        param1 = arcpy.Parameter(
            displayName="Shapefile", 
            name="shapefile",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output")
        
        #param2 is a raster dataset
        param2 = arcpy.Parameter(
            displayName="Raster Data", 
            name="raster_data",
            datatype="DERasterDataset",
            parameterType="Required",
            direction="Input")
        
        #param3 is a project name
        param3 = arcpy.Parameter(
            displayName="Project Name", 
            name="project_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")   
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        csv_path = parameters[0].valueAsText
        shapefile = parameters[1].valueAsText
        raster_path = parameters[2].valueAsText 
        project_name = parameters[3].valueAsText
        project2(project_name,csv_path,raster_path,shapefile)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
